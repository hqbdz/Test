from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Facebook Post Scheduler (Demo)"

if __name__ == '__main__':
    app.run(debug=True)
