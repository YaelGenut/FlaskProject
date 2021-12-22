from flask import Flask, redirect, url_for, render_template, request , session

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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    users = {'user1': {'name': 'Yael', 'age': '26', 'email': 'yaelgenut@gmail.com'},
             'user2': {'name': 'Adi', 'age': '19', 'email': 'adi@gmail.com'},
             'user3': {'name': 'Michal', 'age': '80', 'email': 'Michal@gmail.com'},
             'user4': {'name': 'Lian', 'age': '5', 'email': 'Lian@gmail.com'},
             'user5': {'name': 'Niv', 'age': '27', 'email': 'Niv@gmail.com'}}

    if request.method == 'POST':
        user_nickname= request.form['user_nickname']
        password= request.form['password']
        found= True
        if found :
            session['user_nickname'] = user_nickname
            session['user_password'] = password
            return render_template('assignment9.html')
        else:
            return render_template('assignment9.html')

    if request.method == 'GET':
        if 'user_key' in request.args:
            if request.args.get('user_key') != '':
                user_key = request.args['user_key']
                for key in users:
                    if key == user_key:
                        user_name = users[key]['name']
                        email = users[key]['email']
                        age = users[key]['age']
                        return render_template('assignment9.html', u_name=user_name, email=email, age=age
                                               )
                return render_template('assignment9.html',not_in='not')
            return render_template('assignment9.html',  users=users)

        return render_template('assignment9.html')


@app.route('/logout')
def logout_func():
    session['user_nickname'] = ''
    session['user_password'] = ''
    return render_template('assignment9.html')