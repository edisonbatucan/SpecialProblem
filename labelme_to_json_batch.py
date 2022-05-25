import os
path ='./json'
json_file = os.listdir(path)
for file in json_file: 
    os.system("../Python/Python39/Scripts/labelme_json_to_dataset.exe %s"%(path +'/' + file))