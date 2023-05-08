from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    '''Returns the text translated into French'''
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return  translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    '''Returns the text translated into English'''
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)