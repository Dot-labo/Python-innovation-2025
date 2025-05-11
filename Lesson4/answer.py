import streamlit as st

st.title("🎨 マイプロフィール作成アプリ 🎨")

# 問題1：名前を入力しよう！
name = st.text_input("名前の入力")

# 問題2：自分の誕生日を選択するために、日付入力欄を表示しよう！
# ヒント：st.date_input()を使おう
birthday = st.date_input("誕生日の入力")

# 問題3：自分の年齢を入力するために数値入力用のスライダーを表示しよう！
age = st.slider("年齢", 0, 100)

# 問題4：好きな色を選ぶために、カラーピッカーを設置しよう！
# ヒント：st.color_picker()を使おう
favorite_color = st.color_picker("好きな色")

# 問題5：自己紹介文を入力しよう！
# ヒント: st.text_area()を使おう
introduction = st.text_area("自己紹介文の入力")


show_profile = st.button("プロフィールをまとめて表示")
if show_profile:
    st.header("✨あなたのプロフィール✨")
    st.write("**名前**:", name)
    st.write("**誕生日**:", birthday)
    st.write("**年齢**:", age)
    st.color_picker("**好きな色**:", value= favorite_color)
    st.write("**自己紹介**:", introduction)
