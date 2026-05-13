import streamlit as st

# --- 1. 見た目の設定（UI） ---
st.title("🚀 LLMOコンテンツ生成システム")
st.caption("AI（ChatGPT等）に引用されやすい最強のコンテンツを設計します")

# 入力エリア
st.subheader("① 情報を入力してください")
user_query = st.text_input("ユーザーがAIに聞きそうな「悩み・質問」", placeholder="例：プロジェクト管理ツールの選び方は？")
company_data = st.text_area("自社の独自データ・事例・強み", placeholder="例：弊社は100社以上の導入実績があり、特に製造業に強い...")

# 実行ボタン
if st.button("診断・提案を開始する"):
    if user_query and company_data:
        # --- 2. 診断（壁打ち）機能 ---
        st.divider()
        st.subheader("🔍 AIによる診断（壁打ちアドバイス）")
        st.info(f"「{user_query}」に対して、今の情報では『具体的な失敗事例』が不足しています。ここを追加すると引用率が上がります。")

        # --- 3. タイトル案の提案 ---
        st.subheader("💡 LLMO最適化タイトル案")
        titles = [
            f"AIが教える！{user_query}の正解と、弊社の独自事例",
            f"【最新調査】引用されるための{user_query}活用ガイド",
            f"なぜあなたの記事はAIに無視されるのか？解決策を公開"
        ]
        selected_title = st.selectbox("気に入ったタイトルを選んでください", titles)

        # --- 4. 構成案の生成（デモ用） ---
        st.subheader("📝 記事構成案 ＆ FAQ")
        st.success(f"選ばれたタイトル：{selected_title}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **【記事構成】**
            1. 導入（なぜ今この情報が必要か）
            2. 結論（AIが好む要約）
            3. 独自データ（他社にはない強み）
            4. まとめ
            """)
        with col2:
            st.markdown("""
            **【想定されるFAQ】**
            - Q: 導入コストは？
            - A: 〇〇円から可能です。
            """)
            
        st.subheader("🛠️ 技術的解説・コード")
        st.code("\n<meta name='description' content='...'>", language="html")

    else:
        st.warning("質問内容と独自データの両方を入力してください。")