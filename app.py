from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news-detail')
def news():
    return render_template('news-detail.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")