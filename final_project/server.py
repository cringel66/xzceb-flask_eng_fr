""" server.py for translation program """
from flask import Flask, render_template, request
from machinetranslation import translator
import json

app = Flask("Language Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """ translate english to french """
    textToTranslate = request.args.get('textToTranslate')
    frenchtext=translator.englishToFrench(textToTranslate)
    return frenchtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """ translate french to english """
    textToTranslate = request.args.get('textToTranslate')
    englishtext=translator.frenchToEnglish(textToTranslate)
    return englishtext

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)  # When no port is specified, starts at default port 5000
