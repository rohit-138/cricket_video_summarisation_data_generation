import os
import shutil
def get_txt_files(folder_path):
    txt_files = []
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".txt"):
                txt_files.append(file_name[:-4])
    else:
        print(f"The folder path '{folder_path}' does not exist.")
    return txt_files

def copy_images(source_folder, destination_folder, image_names, file_extension=".jpg"):
    if not os.path.exists(source_folder):
        print(f"The source folder '{source_folder}' does not exist.")
        return    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for image_name in image_names:
        source_path = os.path.join(source_folder, f"{image_name}{file_extension}")
        destination_path = os.path.join(destination_folder, f"{image_name}{file_extension}")
        if os.path.exists(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"Image '{image_name}' copied to '{destination_folder}'.")
        else:
            print(f"Image '{image_name}' not found in '{source_folder}'.")

img_source_folder = "D:\BE Final Year Project\Data_extraction\output_frames"#output path of frame exrraction
annotation_folder_path=folder_path = r'D:/BE Final Year Project/Data_extraction/annotations'#annotations
copy_images(img_source_folder, annotation_folder_path, get_txt_files(annotation_folder_path))
