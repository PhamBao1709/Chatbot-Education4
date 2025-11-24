from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

API_URL = "https://api.openai.com/v1/chat/completions"

def build_prompt(style):
    if style == "short":
        return "Trả lời ngắn gọn, súc tích."
    if style == "detailed":
        return "Trả lời chi tiết, đầy đủ ý."
    if style == "example":
        return "Trả lời kèm ví dụ minh hoạ dễ hiểu."
    if style == "level":
        return "Trả lời theo 4 cấp độ: Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao."
    return ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    style = data.get("style", "short")

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": f"Bạn là chatbot hỗ trợ học sinh các môn Toán - Văn - Anh. {build_prompt(style)}"},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
