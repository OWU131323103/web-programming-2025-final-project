import streamlit as st
from datetime import date
import google.generativeai as genai

# --- Gemini API設定 ---
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Streamlit設定 ---
st.set_page_config(page_title="少女漫画イケメン診断♡")
st.title("少女漫画キャラ診断 ＆ イケメン自己紹介カード")
st.markdown("**「もし少女漫画の中で、あなたがイケメンだったら？」**\n診断して、理想のイケメン自己紹介カードを作ろう！")

# --- ステップ1：性格診断 ---
st.header("ステップ1：性格診断")

q1 = st.radio("Q1. 朝のテンションは？", ["静かに始めたい", "テンションMAX", "眠すぎて無理", "ぼーっとしてる", "とりあえず二度寝"])
q2 = st.radio("Q2. 好きな言葉は？", ["努力", "自由", "友情", "ドキドキ", "秘密", "運命"])
q3 = st.radio("Q3. 周りからの印象は？", ["クールって言われる", "天然って言われる", "うるさいって言われる", "よく分からないって言われる", "頼りになると言われる", "面白いと言われる"])
q4 = st.radio("Q4. 暇な時間の過ごし方は？", ["読書や勉強", "外で体を動かす", "友達と遊ぶ", "音楽を聴く", "一人で考え事"])
q5 = st.radio("Q5. 困っている人がいたら？", ["そっと助ける", "正面から声をかける", "見て見ぬふりをする", "誰かに任せる"])

# --- ステップ2：プロフィール入力 ---
st.header("ステップ2：プロフィールを入力")

your_name = st.text_input("あなたの名前（ニックネームOK）")
birthday = st.date_input("誕生日", value=date(2000, 1, 1))
blood_type = st.selectbox("血液型", ["A型", "B型", "O型", "AB型"])
fav_item = st.text_input("好きなもの（例：猫／ギター／チョコなど）")

# --- 診断ボタン ---
if st.button("🎀 イケメン診断する！"):

    # イケメンタイプの診断ロジック
    # より複雑な組み合わせで多様なキャラを生成
    if q1 == "静かに始めたい" and q2 == "努力" and q4 == "読書や勉強":
        chara_type = "孤高の完璧主義者イケメン"
        catchphrase = "無駄なことはしない。君もそうだろ？"
        theme_color = "#b8cce4" # クールな青系

    elif q2 == "自由" and q3 == "天然って言われる" and q5 == "そっと助ける":
        chara_type = "癒し系ふんわり年下男子"
        catchphrase = "先輩、頑張りすぎですよ。ほら、一緒に休憩しよ？"
        theme_color = "#ffe1f0" # 優しいピンク系

    elif q1 == "テンションMAX" and q3 == "うるさいって言われる" and q4 == "外で体を動かす":
        chara_type = "太陽みたいな熱血スポーツ男子"
        catchphrase = "いくぞ！オレと一緒に、テッペン目指そうぜ！"
        theme_color = "#fff2cc" # 明るい黄色系

    elif q1 == "ぼーっとしてる" and q2 == "自由" and q4 == "一人で考え事":
        chara_type = "掴みどころのないミステリアス王子"
        catchphrase = "この世界は、もっと面白いもので溢れてる。"
        theme_color = "#d9ead3" # 神秘的な緑系

    elif q2 == "ドキドキ" and q3 == "よく分からないって言われる" and q4 == "音楽を聴く":
        chara_type = "芸術肌の影ある天才肌イケメン"
        catchphrase = "君の存在が、僕の創作意欲を掻き立てる。"
        theme_color = "#c9daf8" # 芸術的な水色系

    elif q3 == "頼りになると言われる" and q5 == "正面から声をかける" and q2 == "友情":
        chara_type = "みんなの頼れる兄貴分イケメン"
        catchphrase = "何かあったら、いつでも俺を頼れよ。"
        theme_color = "#ffddcc" # 温かいオレンジ系

    elif q1 == "とりあえず二度寝" and q3 == "面白いと言われる" and q4 == "友達と遊ぶ":
        chara_type = "お調子者のお祭り騒ぎ男子"
        catchphrase = "人生は楽しまなきゃ損だろ？さ、次は何して遊ぶ？"
        theme_color = "#ccf2ff" # 楽しい水色系

    elif q2 == "秘密" and q5 == "見て見ぬふりをする":
        chara_type = "クールな一匹狼イケメン"
        catchphrase = "俺に構うな。巻き込まれても知らないぞ。"
        theme_color = "#e6e6e6" # 無機質なグレー系

    elif q2 == "運命" and q5 == "誰かに任せる":
        chara_type = "予測不能な変人型イケメン"
        catchphrase = "君と出会ったのは、運命のイタズラかな？"
        theme_color = "#f2ccff" # 個性的な紫系

    else: # どのパターンにも当てはまらない場合のデフォルト
        chara_type = "王道！学園の王子様イケメン"
        catchphrase = "君の笑顔は、僕の太陽だ。"
        theme_color = "#e2c4f9" # 王道な紫系

    # --- 自己紹介カード表示 ---
    st.subheader("💌 あなたのイケメン自己紹介カード")

    card_html = f"""
    <div style='
        background-color:{theme_color};
        padding:25px;
        border-radius:20px;
        font-family:serif;
        text-align:left;
    '>
        <h2> {chara_type}</h2>
        <h3>「{catchphrase}」</h3>
        <p><b>名前：</b>{your_name if your_name else "？？？"}</p>
        <p><b>誕生日：</b>{birthday.strftime('%Y年%m月%d日')}</p>
        <p><b>血液型：</b>{blood_type}</p>
        <p><b>好きなもの：</b>{fav_item if fav_item else "？？？"}</p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    # --- Geminiによる少女漫画解説 ---
    st.subheader("📖 少女漫画風キャラ解説")
    prompt = f"""
    「{chara_type}」というタイプのイケメンが少女漫画に登場するとしたら、どんな特徴があって、
    どんなストーリーやシーンで活躍するか、読者にキュンとされるポイントと一緒に100文字以内で教えてください。
    """

    with st.spinner("少女漫画の世界を描いています...💭"):
        try:
            response = model.generate_content(prompt)
            st.markdown(f"_{response.text.strip()}_")
        except Exception as e:
            st.error(f"Gemini APIの呼び出しに失敗しました: {e}")