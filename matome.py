import os
import shutil

def gather_images(parent_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 親ディレクトリ内のすべてのディレクトリを走査
    for dir_name in os.listdir(parent_dir):
        dir_path = os.path.join(parent_dir, dir_name)

        # ディレクトリでない場合はスキップ
        if not os.path.isdir(dir_path):
            continue

        # ディレクトリ内の画像ファイルを取得
        image_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        
        # 画像ファイルを出力ディレクトリにコピー
        for image_file in image_files:
            src_path = os.path.join(dir_path, image_file)
            dst_path = os.path.join(output_dir, image_file)
            shutil.copy(src_path, dst_path)
        
        print(dir_name + ' finish')
    print('全ての画像をまとめました')

# 記入欄-------------------------------------------------------------------------
# parent_directory = r'G:\AFRP\fatigue_test\no14\No14_rawdata'
# output_directory = r'G:\AFRP\fatigue_test\no14\matome_all'
# gather_images(parent_directory, output_directory)