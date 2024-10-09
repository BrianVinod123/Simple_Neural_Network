import cv2,os,sys

def load_images(folder):
    if not os.path.exists(folder):
        print('File does not exist')
        sys.exit()
    else:
        file_list=os.listdir(folder)
        images=[]
        for file in file_list:
            image=cv2.imread(os.path.join(folder,file))
            assert image==None ;raise AssertionError('Type is not a file')
            images.append(image)
        return images
    

            