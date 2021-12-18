from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/main')
@app.route('/')
def cv():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():

    return render_template('assignment8.html', hobbies=['Sport', 'Piano', 'Guitar', 'Puzzles'],
                           )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cat')
def maple():
    return render_template('cat.html')

if __name__ == '__main__':
    app.run(debug=True)
