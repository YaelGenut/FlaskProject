from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from intract_with_DB import interact_db


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


##assignment11
@app.route('/assignment11/users', methods=['GET'])
def get_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = jsonify(query_result)
    return response


@app.route('/assignment11/external',  methods=['GET', 'POST'])
def assignment11_external():
    return render_template('assignment11/external.html')


@app.route('/external_front', methods=['post'])
def external_front_func():
     user_id = request.form['user_id']
     return render_template('assignment11/external.html', id=user_id)

@app.route('/external_backend')
def get_user_data():
    if request.args['user_id'] != '':
        id = request.args['user_id']
        res = request.get('https://reqres.in/api/users/%s' % id)
        user = res.json()
        return render_template('assignment11/external.html', user=user)
    return render_template('assignment11/external.html')

## Assignment 12

@app.route('/assignment12/restapi_users', defaults ={'user_id': 1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_users_func(user_id):
    query = 'select * from users where id=%s' %user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users)==0:
        return_dict= {
            'status' : 'failed',
            'message' : 'User does not exist'
        }
    else:
         return_dict= {
            'status': 'success',
            'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
        }
    return jsonify(return_dict)
