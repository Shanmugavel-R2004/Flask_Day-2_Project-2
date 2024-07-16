from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>Hello </h1>"

@app.route('/<name>')
def hello1(name):
    return "<h1>Hello {}</h1>".format(name)


if __name__=='__main__':
    app.run(debug=True)