from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome!. Go to puppy_latin/name to see your name in puppy latin!</h1>"

@app.route('/puppy_latin/<variable>')
def convert(variable):
    name=""
    if(variable[-1]!='y'):
        name=variable+'y'
    else:
        name=variable[:-1]+'iful'

    return f"<h1>Hi {variable} ! Your puppylatin name is {name}"

if __name__=="__main__":
    app.run(debug=True)