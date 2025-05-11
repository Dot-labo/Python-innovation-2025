import streamlit as st
import pandas as pd

st.title("🎨 マイプロフィール作成アプリ 🎨")

# 問題1：名前を入力しよう！
# ヒント：st.text_input()を使おう
# name = st.text_input(label="名前を入力")

# 問題2：自分の誕生日を選択するために、日付入力欄を表示しよう！
# ヒント：st.date_input()を使おう

# 問題3：好きな色を選ぶために、カラーピッカーを設置しよう！
# ヒント：st.color_picker()を使おう

# 問題4：自己紹介文を入力しよう！
# ヒント: st.text_area()を使おう


show_profile = st.button("プロフィールをまとめて表示")
if show_profile:
	  st.header("✨あなたのプロフィール✨")
    st.write("**名前**:", name)
    st.write("**誕生日**:", birthday)
    st.write("**好きな色**:", favorite_color)
    st.write("**自己紹介**:", introduction)
