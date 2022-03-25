import mimetypes
from flask import Flask, render_template

mimetypes.add_type('text/javascript', '.js')

app = Flask(__name__, static_folder='src/static', template_folder='src')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/github')
def github():
    return render_template('github.html')

@app.route('/spigot')
def spigot():
    return render_template('spigot.html')

@app.errorhandler(404)
def error(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(port=81, debug=True)
