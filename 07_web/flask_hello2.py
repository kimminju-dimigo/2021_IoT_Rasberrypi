from flask import Flask, render_template

#Flask 객체 생성 // 이렇게 하면 이름이 바뀌어도 파일 이름으로 들어가게 되어 있음
#__name__ 파일 이름
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(
        "hello.html",
        title="Hello, Flask!!")

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/second")
def second():
    return render_template("second.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")
