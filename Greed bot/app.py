"""Personal Finance Chatbot Flask Application with User Profile Support."""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Render the homepage."""
    return render_template("app.html")  # make sure this matches your file name


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages and user profile."""
    user_message = request.form.get("message", "").lower()
    income = request.form.get("income", "")
    age = request.form.get("age", "")
    risk = request.form.get("risk", "")

    # Short and simple replies
    if "save" in user_message and income.isdigit():
        savings = int(income) * 0.2
        reply = f"💰 Save about 20% of your income (~₹{int(savings)})."
    elif "tax" in user_message:
        reply = f"🧾 At age {age}, consider ELSS, NPS, or retirement plans for tax savings."
    elif "invest" in user_message:
        if risk == "low":
            reply = "📉 Low risk: FDs, PPF, or government bonds."
        elif risk == "medium":
            reply = "📊 Medium risk: Index funds + balanced mutual funds."
        elif risk == "high":
            reply = "🚀 High risk: Stocks, crypto, or growth funds."
        else:
            reply = "📈 Diversify with stocks and bonds."
    else:
        reply = "🤖 Ask me about savings, taxes, or investments!"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
