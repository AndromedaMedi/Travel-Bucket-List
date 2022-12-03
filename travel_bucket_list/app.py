from flask import Flask, render_template

app = Flask(__name__)

# app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__name__':
    app.run(debug=True)