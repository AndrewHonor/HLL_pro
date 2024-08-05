from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    variable1 = "Hello"
    variable2 = "World"
    return render_template('index.html', var1=variable1, var2=variable2)

if __name__ == '__main__':
    app.run(debug=True)
