import os
def rename_file():
    file_list=os.listdir("/Users/kundan/Downloads/prank")
    print(file_list)
    saved_path=os.getcwd()
    print("The current directory is"+saved_path)
    os.chdir("/Users/kundan/Downloads/prank")
    for file_name in file_list:
        print("Old Name -"+file_name)
        print ("New Name -"+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_file()
