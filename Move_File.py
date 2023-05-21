import os
import shutil 

from_dir = "C:/Users/ajith/Downloads" 
to_dir = "C:/Users/ajith/OneDrive/Desktop/Document_Files"


list_of_files = os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:

     
     name,extension = os.path.splittext(file_name)