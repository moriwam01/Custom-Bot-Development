from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Use an environment variable for the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debug print
        user_message = data.get("message")
        print("User message:", user_message)  # Debug print

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
        )

        last_reply = (
            response.choices[0].message["content"]
            if response.choices
            else "Sorry, I couldn't process that."
        )
        print("Reply:", last_reply)  # Debug print
        return jsonify({"message": last_reply})
    except Exception as e:
        print("Error:", e)  # Debug print
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
