from flask import Flask, render_template, request

app = Flask("SuperScraper")

# @ : 데코레이터 - 아래의 함수를 꾸미는 역할
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get("word")
    return render_template("report.html", searchingBy=word)

app.run(host="localhost")