from flask import Flask

#Flask 객체 생성 // 이렇게 하면 이름이 바뀌어도 파일 이름으로 들어가게 되어 있음
#__name__ 파일 이름
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/first">Go first</a>
        <a href="/second">Go Second</a>
    '''
@app.route("/first")
def first():
    return '''
        <p>First Page</p>
        <a href="/">Go Home</a>
    ''' 
@app.route("/second")
def second():
    return '''
        <p>Second Page</p>
        <a href="/">Go Home</a>
    '''

if __name__=="__main__":
    app.run(host="0.0.0.0")
