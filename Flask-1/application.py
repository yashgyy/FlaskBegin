from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route')
def report():
    name=request.args.get('Search')
    checks=['You did not have an Uppercase Letter','You did not have a lowercase letter','You did not have a number at the end']

    if(any(filter(lambda x: x.islower(),name))):
        checks.remove('You did not have a lowercase letter')
    
    if(any(filter(lambda x: x.isupper(),name))):
        checks.remove('You did not have an Uppercase Letter')

    try:
        int(name[-1])
        checks.remove('You did not have a number at the end')
    except:
        pass

    return render_template('report.html',checks=checks)



if __name__=="__main__":
    app.run(debug=True)