import numpy as np
def convolve2d(image,kernel,n_filters=1,padding='valid',strides=(1,1)):
    img_channels=image.shape[2] if len(image.shape)>2 else 1
    ker_channels=kernel.shape[2] if len(kernel.shape)>2 else 1
    #yet to resolve for more than one filter
    #could use a helper 2d function to reduce the lines!!
    #could be optimized
    result=[] 
    #working with padding later
    if padding=='valid':
        width=(image.shape[0]-kernel.shape[0])//strides[0]+1 #The number of rows act as the height of the image 
        height=(image.shape[1]-kernel.shape[1])//strides[1]+1 #The number of columns act as the width of the image
        print(width)
        print(height)
        for n in range(n_filters):
            feature_map=[]  
            for c in range(img_channels):
                feature=[]
                for i in range(0,width*strides[0],strides[0]):
                    row=[]
                    for j in range(0,height*strides[1],strides[1]):
                        row.append((image[i:i+kernel.shape[0],j:j+kernel.shape[1],c]*kernel).sum())
                    feature.append(row)
                feature_map.append(feature)
            feature_map=np.dstack(feature_map)
            result.append(np.uint8(np.floor(feature_map))) #since default type is 32 bit signed and integer grayscale only takes unsigned 8 bit(2^8-1=255) or unsigned 16 bit          
    elif padding=='same':
        padding_width=(image.shape[0]*(strides[0]-1)+kernel.shape[0])//2 
        padding_height=(image.shape[1]*(strides[1]-1)+kernel.shape[1])//2
        padded_image=cv2.copyMakeBorder(image,padding_width,padding_width,padding_height,padding_height,borderType=cv2.BORDER_CONSTANT,value=0x00)
        width=(padded_image.shape[0]-kernel.shape[0])//strides[0]+1 #The number of rows act as the height of the image 
        height=(padded_image.shape[1]-kernel.shape[1])//strides[1]+1 #The number of columns act as the width of the image
        for n in range(n_filters):
            feature_map=[]  
            for c in range(img_channels):
                feature=[]
                for i in range(0,width*strides[0],strides[0]):
                    row=[]
                    for j in range(0,height*strides[1],strides[1]):
                        row.append((padded_image[i:i+kernel.shape[0],j:j+kernel.shape[1],c]*kernel).sum())
                    feature.append(row)
                feature_map.append(feature)
            feature_map=np.dstack(feature_map)
            print("convoluted image shape",feature_map.shape)
            result.append(np.uint8(np.floor(feature_map))) #since default type is 32 bit signed and integer grayscale only takes unsigned 8 bit(2^8-1=255) or unsigned 16 bit 
    return result

# #test array
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
ker=np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
# print(convolve2d(image=a,kernel=ker))

import cv2
image=cv2.imread('test_images/test4.webp',flags=cv2.IMREAD_COLOR)
image=np.array(image)
cv2.imshow(winname="image",mat=image)
cv2.waitKey(0)
cv2.imshow(winname="convoluted_image",mat=convolve2d(image,kernel=ker,padding='same')[0])
cv2.waitKey(0)
