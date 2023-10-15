# Import Module
import os
# Folder Path
path = r"C:\Users\HP\OneDrive - Universitas Diponegoro\Documents\Kuliah STIS V\Information Retrieval\Praktik\berita"
# List all files in a directory using os.listdir
for file in os.listdir(path):
 if os.path.isfile(os.path.join(path, file)):
  print(file)

 
import re

def read_text_file(file_path):
 with open(file_path, 'r') as f:
  a = f.read()
  query="corona"
  if re.search(query,a):
        print(a)
        
        print("nama file"+file_path)
        print("")
  
#iterate through all file

for file in os.listdir(path):
 #check whether file is in text format or not 
 if file.endswith(".txt"):
  file_path=f"{path}\{file}"
  
  #call read text function
  read_text_file(file_path)
 

