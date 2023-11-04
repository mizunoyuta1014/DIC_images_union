#フォルダの数とフォルダ内のファイルの数を数える

import os

def count_files_in_folder(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return len(files)
    except OSError:
        return -1  # エラーが発生した場合

def count_files_in_subfolders(parent_folder):
    subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]
    result = {}

    for subfolder in subfolders:
        subfolder_path = os.path.join(parent_folder, subfolder)
        file_count = count_files_in_folder(subfolder_path)
        result[subfolder] = file_count
    
    return result

def main():
    parent_folder_path = r'G:\AFRP\fatigue_test\no13\No13'

    subfolder_count = len(os.listdir(parent_folder_path))
    # print(f"子フォルダの数: {subfolder_count}")

    subfolder_file_counts = count_files_in_subfolders(parent_folder_path)
    
    file_counts_list = []
    for subfolder, file_count in subfolder_file_counts.items():
        file_counts_list.append((subfolder, file_count))
        print(f"{subfolder}: ファイルの数 - {file_count}")

    # print("\n各子フォルダのファイル数:")
    # for subfolder, file_count in file_counts_list:
    #     print(file_count)

if __name__ == "__main__":
    main()
