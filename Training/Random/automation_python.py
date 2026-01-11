# Folder,directory interaction plus any additional OS interaction
import os
#file moves
import shutil

download_dir = r'/Users/wamckei/Downloads'
extensions = []

def find_extension(folder_name):
    for filename in os.listdir(folder_name):
        extension = os.path.splitext(filename)
        if extension[1] not in extensions:
            extensions.append(extension[1])
    print("Extensions are : ", extensions)

def rename_files(folder_name):
    for ext in extensions:
         for filename in os.listdir(folder_name):
            extension = os.path.splitext(filename)
            if extension[1] == ext:
                count = 1
                old_name = os.path.join(folder_name,filename)
                new_name = os.path.join(folder_name, ext + "_" + str(count) + ext)
                if os.path.exists(new_name) == False:

                    os.rename(old_name, new_name)
                    os.makedirs(folder_name + "\\" +ext,exist_ok=True)
                    if os.path.exists(folder_name + "\\" +ext):
                        shutil.move(new_name,folder_name + "\\" + ext)


find_extension(download_dir)
rename_files(download_dir)