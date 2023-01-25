import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

@app.route("/", methods=("GET", "POST"))
def index():
    chat_input = "Ask Question"
    if request.method == "POST":
        chat_input = request.form["chat_input"]
        response = openai.Completion.create(
            engine="text-ada-001",
            prompt=chat_input,
            max_tokens=1024,
            n = 10,
            stop=None,
            temperature=0.5
        )
        print(chat_input)
        print(str(response))
        return redirect(url_for("index", result=response.choices[0].text, chat_input=chat_input))

    result = request.args.get("result")
    animal = request.args.get("chat_input")
    print(result)
    return render_template("index.html", result=result, chat_input=chat_input)


def generate_prompt(chat_input):
    return "".format(
        chat_input.capitalize()
    )
