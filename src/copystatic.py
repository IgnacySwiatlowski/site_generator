import os
import shutil

def delete_contents(destination_directory):
    if os.path.exists(destination_directory):
        for file in os.listdir(destination_directory):
            file_path = os.path.join(destination_directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                delete_contents(file_path)
                os.rmdir(file_path)

def copy_recursive(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        delete_contents(dest_dir)

    for name in os.listdir(src_dir):
        src_path = os.path.join(src_dir, name)
        dest_path = os.path.join(dest_dir, name)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_dir):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_recursive(src_path, dest_path)