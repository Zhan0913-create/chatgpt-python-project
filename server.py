from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY жоқ.\n"
        "Терминалға енгізіңіз:\n"
        "export OPENAI_API_KEY='your_api_key_here'\n"
        "Windows үшін: set OPENAI_API_KEY=your_api_key_here"
    )

client = OpenAI(api_key=api_key)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = (data or {}).get("question", "").strip()

    if not question:
        return jsonify({"error": "Сұрақ енгі��іңіз."}), 400

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Сіз пайдалы, қысқа және нақты жауап беретін AI-сіз."},
            {"role": "user", "content": question},
        ],
        temperature=0.7,
    )

    answer = response.choices[0].message.content.strip()
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
