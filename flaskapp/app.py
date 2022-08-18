from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('indexaa.html')

@app.route('/analysis')
def home():
    return render_template('analysis.html')

@app.route('/results')
def home():
    return render_template('Results.html')

@app.route('/tech')
def home():
    return render_template('Tech.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)