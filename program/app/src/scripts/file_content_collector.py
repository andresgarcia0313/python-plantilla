"""Captura todos los archivos en un unico archivo"""
import os


def save_file_content_to_txt(folder_path):
    """
    Save content from all files in a folder
    """
    current_folder = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(current_folder, 'file_contents.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_file_path = os.path.relpath(file_path, folder_path)
                output_file.write(f'File: {relative_file_path}\n')
                try:
                    with open(file_path, 'r', encoding='utf-8') as input_file:
                        content = input_file.read()
                        output_file.write(f'File Content: \n{content}\n\n')
                except UnicodeDecodeError:
                    output_file.write(f'File Content: (Non-UTF-8 encoding, unable to read)\n\n')
    print("Proceso finalizado de captura de contenido de archivos.")


def save_folders_and_files_to_txt(folder_path):
    """
    Save list of folders and files in a folder
    """
    print(folder_path)
    current_folder = os.path.dirname(os.path.abspath(__file__))    
    output_file_path = os.path.join(current_folder, 'folders_and_files.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(folder_path):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                relative_dir_path = os.path.relpath(dir_path, folder_path)
                output_file.write(f'Directory: {relative_dir_path}\n')
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_file_path = os.path.relpath(file_path, folder_path)
                output_file.write(f'File: {relative_file_path}\n')
    print("Proceso de captura de carpetas y archivos finalizado.")


if __name__ == "__main__":
    project_folder = os.path.join(os.path.dirname(__file__),"..", "..", "..", "..")
    save_file_content_to_txt(project_folder)
    save_folders_and_files_to_txt(project_folder)
