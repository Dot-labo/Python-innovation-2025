# 問題１から問題５までの解答例

import streamlit as st

st.title("🎮 オリジナルキャラクター作成 🎮")

# 問題1：レベルをスライダーで選択
level = st.slider("キャラクターのレベルを選んでください", 1, 100)
st.write(f"選んだレベル：{level}")

# 問題2：特殊能力を持っているかチェックボックスで選択
special_power = st.checkbox("特殊能力を持っている")
st.write(f"特殊能力あり：{'はい' if special_power else 'いいえ'}")

# 問題3：職業（クラス）をラジオボタンで選択
selected_class = st.radio(
    "キャラクターの職業を選んでください",
    ["戦士", "魔法使い", "盗賊"]
)
st.write(f"選んだ職業：{selected_class}")

# 問題4：出身地をドロップダウンで選択
selected_origin = st.selectbox(
    "出身地を選んでください",
    ["砂漠", "森", "雪国", "都市"]
)
st.write(f"選んだ出身地：{selected_origin}")

# 問題5：得意な武器をマルチセレクトで選択
selected_weapons = st.multiselect(
    "得意な武器を選んでください（複数選択可）",
    ["剣", "弓", "魔法杖", "ナイフ"]
)

if selected_weapons:
    st.write("選んだ武器：")
    for weapon in selected_weapons:
        st.write(f"・{weapon}")
else:
    st.write("武器は選ばれていません。")
