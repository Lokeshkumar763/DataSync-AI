from flask import Flask, render_template, request, jsonify

from src.rag_pipeline import answer_question


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "Please enter a question."
        }), 400

    try:
        answer = answer_question(question)

        return jsonify({
            "answer": answer
        })

    except Exception as e:
        print("\n========== RAG ERROR ==========")
        print(repr(e))
        print("===============================\n")

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)