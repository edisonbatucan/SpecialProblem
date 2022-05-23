import os
path ='C:/Users/batuc/Desktop/json_masking'
json_file = os.listdir(path)
for file in json_file: 
    os.system("C:/Users/batuc/AppData/Local/Programs/Python/Python39/Scripts/labelme_json_to_dataset.exe %s"%(path +'/' + file))