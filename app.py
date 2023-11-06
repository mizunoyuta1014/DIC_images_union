import streamlit as st
import os
from matome import gather_images
from count_file import count_files_in_folder,count_files_in_subfolders

def gather(parent,output):
    gather_images(parent, output)

st.title('DIC画像をまとめる')

parent_directory = st.text_input('親フォルダのパスを入力してください。')
output_directory = st.text_input('出力先のフォルダを入力してください。')

button = st.button('ファイルをまとめます')
if button:
    st.spinner('処理中です...')
    gather(parent_directory, output_directory)
    st.write("処理が完了しました。" + output_directory + "に出力されました。")
