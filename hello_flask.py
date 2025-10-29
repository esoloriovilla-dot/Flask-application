from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2 - Hello World
@app.route('/')
def hello():
    return '''
        <h1>Hello world!</h1>
        <p>Genevieve M. : afaik</p>  
        <p>Estrella S. : lol</p>
        <p>Kaissy A. : asap</p>
    '''

# Task 3 - Add Templates
@app.route('/estrella')
def estrella_page(): 
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)

# Task 5 - GitHub repository
# https://github.com/esoloriovilla-dot/Flask-application