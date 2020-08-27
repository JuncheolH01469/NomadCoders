from flask import Flask

app = Flask("SuperScraper")

# @ : 데코레이터 - 아래의 함수를 꾸미는 역할
@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"

@app.route("/contact")
def contact():
    return "Contact me!"

app.run(host="localhost")