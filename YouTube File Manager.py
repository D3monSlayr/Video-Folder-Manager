import os

sudo = input("Enable sudo(y/N)? ")

directory = input("Enter the exact directory for the files: ")

number = input("Enter the number of the video: ")

full_dir = f"{directory}\\{number}"

# Sudo text feature
if sudo == "y":
    export_folder = input("Enter the export folder name: ")
    background = input("Enter the background folder name: ")
    music = input("Enter the music folder name: ")
    
    os.mkdir(full_dir)
    
    os.mkdir(f"{full_dir}\\{export_folder}")
    os.mkdir(f"{full_dir}\\{background}")
    os.mkdir(f"{full_dir}\\{music}")
    
    i = 1
    for i in range(20):
        add_folder = input("Is there any folders you want to add (y/N)? ") 
        
        if add_folder == "y":
            added_folder = input("Enter another folder: ")
            
            os.system(f"cd {full_dir}")
            
            os.mkdir(f"{full_dir}\\{added_folder}")
        else:
            break;
else: 
    #Main Stream
    os.mkdir(full_dir)
    os.system(f"cd {full_dir}")

    # File System
    os.mkdir(f"{full_dir}\\exported")
    os.mkdir(f"{full_dir}\\background")
    os.mkdir(f"{full_dir}\\music")

    #Finish
    os.close(0)
    os.abort()

print("The folders have been made. You can now proceed...")
input("")