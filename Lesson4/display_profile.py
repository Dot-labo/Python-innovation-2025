if show_profile:
    st.markdown("---")
    st.header("🧙‍♀️ あなたのプロフィール")

    # 基本情報を3列で整列
    cols = st.columns(3)
    cols[0].subheader("📝 自己紹介")
    cols[0].write(問題1で作った変数 if introduction else "（未入力）")

    cols[1].subheader("🎂 誕生日")
    cols[1].write(問題2で作った変数.strftime("%Y年%m月%d日"))

    cols[2].subheader("🎨 好きな色")
    cols[2].color_picker("あなたの選んだ色", 問題3で作った変数, disabled=True)

    st.markdown("---")

    st.subheader("💪 自分の特技リスト")
    if not 問題4で作った変数.empty and 問題4で作った変数["特技"].str.strip().any():
        st.dataframe(問題4で作った変数)
    else:
        st.warning("特技が入力されていません。")

    st.markdown("---")