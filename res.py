import os
# read img path and label path and write to txt file
def read_dataset(data_dir, trainpath, testpath):
    
    import random

    random_list = []

    for i in range(10):
        random_list.append(random.randint(0, 100))

    folders = os.listdir(data_dir)
    # print(folders)

    count = 0

    for fol in folders:
        fol_path = os.path.join(data_dir, fol)
        directories = os.listdir(fol_path)

        dir_path1 = os.path.join(fol_path, directories[0])
        dir_path2 = os.path.join(fol_path, directories[1])
        
        file_path1 = os.path.join("jianfeng",fol_path, dir_path1)
        file_path2 = os.path.join("jianfeng",fol_path, dir_path2)

        if (count in random_list):

            with open(testpath, 'a') as f:
                f.write(file_path1 + '  ' + file_path2)
                f.write('\n')

        else :
             with open(trainpath, 'a') as f:
                f.write(file_path1 + '  ' + file_path2)
                f.write('\n')     

        count = count + 1      
    
    return trainpath, testpath

read_dataset('AtrialSeg-slice', 'train_AtrialSeg.txt', 'test_AtrialSeg.txt')