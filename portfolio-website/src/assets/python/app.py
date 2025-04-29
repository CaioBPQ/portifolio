from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dynamic-content', methods=['POST'])
def dynamic_content():
    # Example of dynamically adding content
    return '<p>This content was dynamically added!</p>'

if __name__ == '__main__':
    app.run(debug=True)