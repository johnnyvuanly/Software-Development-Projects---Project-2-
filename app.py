from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/get-inventory')
def get_inventory:
    pass

if __name__ == '__main__':
    app.run()