def categorical_cross_entropy(outputs,labels):
    for i in range(len(outputs)):
        if outputs[i]!=labels[i]:
            return False
    return True
