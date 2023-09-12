from app import app, sqlite3
from flask import render_template, request


@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        print(request.form)
        # exit()
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']
        # obj = { **request.form }
        
        with sqlite3.connect('my_db.db') as _:
            cur = _.cursor()
            cur.execute(
                "INSERT INTO PARTICIPANTS(\
                name, email, city, country, phone) \
                VALUES (?, ?, ?, ?, ?)",
                (name, email, city, country, phone)
            )
            _.commit()
            
        return render_template('index.html')
    else:
        return render_template('join.html')
        
        
@app.route('/participants')
def participants():
    with sqlite3.connect('my_db.db') as _:
        cur = _.cursor()
        cur.execute('select * from participants')
        participants = cur.fetchall()
        # print(participants)
    return render_template('participants.html', participants = participants)



@app.route('/')
def index():
    return render_template('index.html')