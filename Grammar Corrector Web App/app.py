from flask import Flask, render_template, request, jsonify
import language_tool_python # type: ignore

app = Flask(__name__)
tool = language_tool_python.LanguageTool('en-US')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    text = request.form['text']
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
