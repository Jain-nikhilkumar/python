from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure your GPT-3 API key here
openai.api_key='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'  # Replace with your actual GPT-3 API key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_content", methods=["POST"])
def generate_content():
    try:
        user_input = request.json["user_input"]

        # Call GPT-3 to generate educational content based on user input
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choose an appropriate engine
            prompt=user_input,
            max_tokens=10,  # Adjust as needed
            n=1  # Number of responses to generate
        )

        generated_content = response.choices[0].text

        return jsonify({"generated_content": generated_content}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
