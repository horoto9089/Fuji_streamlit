import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import skmob
import os
from PIL import Image
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

df = pd.read_csv('./data/tdf_data.csv')
tdf = skmob.TrajDataFrame(df, latitude='lat', longitude='lng',
                             datetime='time', user_id='user_id')

image_path = "./picture/yamap.jfif"
img1 = Image.open(image_path)

# HTMLファイルの内容を読み込み
with open("./picture/trajectory_map.html", "r") as f:
    html_data = f.read()
















# Sidebar menu with links to each section by using HTML anchor tags
st.sidebar.markdown('''
# MENU
- [生データ](#row_data)
- [データの整形・加工](#data_processing)
- [ハイキング関数](#hiking_function)
- [時系列歩行速度データ](#pace)
''', unsafe_allow_html=True)


st.title("富士登山者のGPSデータ分析")
st.image(img1)

st.header("生データ", anchor="row_data")
st.markdown("---")
st.text("yamapアプリから富士山に登る登山者のGPSデータを2024年8月10,11日の96の活動データをスクレイピング")

st.text("")
st.write(df)

st.components.v1.html(
    html_data,
    height=600,  # 初期の高さを設定、画面サイズに合わせて調整される
    width=None,  # 幅を指定しないことで画面幅に応じて調整される
    scrolling=True
)

with st.expander("pythonコード"):
    st.write("")






st.header("データの整形・加工", anchor="data_processing")
st.markdown("---")


with st.expander("pythonコード"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")










st.header("ハイキング関数", anchor='hiking_function')
st.markdown("---")



with st.expander("pythonコード"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")










st.header("時系列歩行速度データ", anchor='pace')
st.markdown("---")




with st.expander("pythonコード"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")









