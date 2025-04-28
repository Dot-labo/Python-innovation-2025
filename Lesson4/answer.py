import streamlit as st
import pandas as pd

st.title("🎨 マイプロフィール作成アプリ 🎨")

# 問題1：自己紹介を書く
introduction = st.text_area("自己紹介を書いてください")

# 問題2：誕生日を選ぶ
birthday = st.date_input("誕生日を選んでください")

# 問題3：好きな色を選ぶ
favorite_color = st.color_picker("好きな色を選んでください")

# 問題4：サンプルプロフィール一覧を表示
sample_data = {
    "名前": ["さくら", "たろう", "はるか"],
    "誕生日": ["2008-03-15", "2007-07-09", "2008-11-02"],
    "好きな色": ["#FF69B4", "#1E90FF", "#32CD32"]
}

sample_data = pd.DataFrame(sample_data)
st.dataframe(sample_data)

# 問題5：自分の特技リストを作る
my_skills = st.data_editor(
    {
        "特技": ["", "", ""],  # 空欄スタート
    },
    num_rows="dynamic",  # 行数を自由に追加可能
    use_container_width=True
)

my_skills = pd.DataFrame(my_skills)

# 問題6：プロフィールをまとめて表示するボタン
show_profile = st.button("プロフィールをまとめて表示")