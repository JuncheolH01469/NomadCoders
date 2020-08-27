from flask import Flask, render_template

app = Flask("SuperScraper")

# @ : 데코레이터 - 아래의 함수를 꾸미는 역할
@app.route("/")
def home():
    return render_template("home.html")

app.run(host="localhost")