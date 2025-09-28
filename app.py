from flask import Flask, render_template
from data.routes import data

app = Flask(__name__)
app.secret_key = 'notsosecretkey'

#app.register_blueprint(data)

@app.route('/')
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
