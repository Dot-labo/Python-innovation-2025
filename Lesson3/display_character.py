# --- キャラクター表示 ---
# 問題で作ったコードの後ろにこのコードを張り付けてね
# 変数名は自分で作ったものにしてね

# ボタン
show_profile = st.button("キャラクタープロフィールを表示")

# ボタンが押されたらプロフィール表示
if show_profile:
    st.markdown("---")
    st.markdown("## 🧙‍♂️ あなたのキャラクタープロフィール")

    cols = st.columns(3)

    cols[0].markdown("#### 🛡️ クラス")
    cols[0].markdown(
        f"<div style='background-color:#f0f2f6;padding:10px;border-radius:10px;text-align:center'>\
        <b>{問題３で作った変数（クラス）}</b></div>",
        unsafe_allow_html=True
    )

    cols[1].markdown("#### 🗺️ 出身地")
    cols[1].markdown(
        f"<div style='background-color:#f0f2f6;padding:10px;border-radius:10px;text-align:center'>\
        <b>{問題４で作った変数（出身地）}</b></div>",
        unsafe_allow_html=True
    )

    cols[2].markdown("#### 🎚️ レベル")
    cols[2].markdown(
        f"<div style='background-color:#f0f2f6;padding:10px;border-radius:10px;text-align:center'>\
        <b>{問題１で作った変数（レベル）}</b></div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✨ 特徴・能力")
    if 問題２で作った変数（特殊能力）:
        st.success("✅ 特殊能力あり！")
    else:
        st.error("❌ 特殊能力なし")

    st.markdown("---")

    st.markdown("### ⚔️ 得意な武器")
    if 問題５で作った変数（武器）:
        st.info("**装備できる武器：**")
        weapons_html = "<div style='background-color:#e0f7fa;padding:10px;border-radius:10px'>"
        weapons_html += "<br>".join([f"🔹 {weapon}" for weapon in selected_weapons])
        weapons_html += "</div>"
        st.markdown(weapons_html, unsafe_allow_html=True)
    else:
        st.warning("武器は選ばれていません。")

    st.markdown("---")
