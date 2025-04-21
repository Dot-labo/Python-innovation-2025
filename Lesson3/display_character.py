# --- キャラクター表示 ---
# 問題で作ったコードの後ろにこのコードを張り付けてね
# 変数名は自分で作ったものにしてね

# ボタン
show_profile = st.button("キャラクタープロフィールを表示")

# ボタンが押されたらプロフィール表示
if show_profile:
    st.markdown("---")
    st.header("🧙‍♂️ あなたのキャラクタープロフィール")

    st.subheader("📋 基本情報")
    cols = st.columns(3)
    cols[0].metric(label="🛡️ クラス", value=問題3で作った変数)
    cols[1].metric(label="🗺️ 出身地", value=問題4で釣った変数)
    cols[2].metric(label="🎚️ レベル", value=問題1で作った変数)

    st.markdown("---")

    st.subheader("✨ 特徴・能力")
    if 問題2で作った変数:
        st.success("✅ 特殊能力あり！")
    else:
        st.error("❌ 特殊能力なし")

    st.markdown("---")

    st.subheader("⚔️ 得意な武器")
    if 問題5で作った変数:
        st.info("選んだ武器：")
        for weapon in selected_weapons:
            st.write(f"・{weapon}")
    else:
        st.warning("武器は選ばれていません。")

    st.markdown("---")
