# import os
# folder_path="My_photos"
# files=os.listdir(folder_path)
# count=1
# for file in files:
#     file_path=os.path.join(folder_path,file)
    
#     if os.path.isdir(file_path):
#         continue
#     _,ext=os.path.splitext(file)
    
#     if ext.lower() not in [".jpg", ".jpeg", ".png"]:
#         continue


    
#     new_name="vacation"+str(count)+ext
#     new_path=os.path.join(folder_path,new_name)
#     if os.path.exists(new_path):
#         print(f'skipping already exist: {new_name}')
#         count+=1
#         continue
#     os.rename(file_path,new_path)
   
#     print(f"{file}-> {new_name}")
    
#     count+=1
# print(f"{count-1} file renamed successfully.")

import os

folder_path = "My_photos"
files = os.listdir(folder_path)
files.sort()

count = 1

for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(file)
    
    if ext.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    # agar file already renamed format me hai to skip (optional)


    # unique name generate karo
    while True:
        new_name = f"vacation{count}{ext}"
        new_path = os.path.join(folder_path, new_name)

        if not os.path.exists(new_path):
            break
        count += 1

    os.rename(file_path, new_path)
    print(f"{file} -> {new_name}")

    count += 1

print(f"{count-1} files renamed successfully.")