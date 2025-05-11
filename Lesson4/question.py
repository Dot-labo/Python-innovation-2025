import streamlit as st

st.title("🎨 マイプロフィール作成アプリ 🎨")

# 問題1：名前を入力しよう！

# 問題2：自分の誕生日を選択するために、日付入力欄を表示しよう！
# ヒント：st.date_input()を使おう

# 問題3：自分の年齢を入力するために数値入力用のスライダーを表示しよう！

# 問題4：好きな色を選ぶために、カラーピッカーを設置しよう！
# ヒント：st.color_picker()を使おう

# 問題5：自己紹介文を入力しよう！
# ヒント: st.text_area()を使おう


show_profile = st.button("プロフィールをまとめて表示")
if show_profile:
    st.header("✨あなたのプロフィール✨")
    st.write("**名前**:", name)
    st.write("**誕生日**:", birthday)
    st.write("**年齢**:", age)
    st.color_picker("**好きな色**:", value= favorite_color)
    st.write("**自己紹介**:", introduction)
