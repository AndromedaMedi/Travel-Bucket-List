from flask import Flask, render_template
from controllers.travel_controller import destination_blueprint

app = Flask(__name__)

app.register_blueprint(destination_blueprint)

if __name__ == '__name__':
    app.run(debug=True)