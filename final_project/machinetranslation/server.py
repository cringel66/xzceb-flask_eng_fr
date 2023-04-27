from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Language Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext=translator.englishToFrench(textToTranslate)
    return "Translated to French" %frenchtext

@app.route("/frenchToEnglish")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    englishtext=translator.frenchToEnglish(textToTranslate)
    return "Translated to English" %englishtext

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
