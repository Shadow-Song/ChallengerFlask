from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import pymysql
from src import sklearn_neural_network_classification

app = Flask(__name__)
mail = Mail(app)
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='example',
    db='virus'
)
serial = ''
app.config['MAIL_SERVER'] = 'smtp.mail.me.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'example@icloud.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aVirus')
def a_virus():
    return render_template('a_virus.html')


@app.route('/defence')
def defence():
    return render_template('defence.html')


@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')


@app.route('/treat')
def treat():
    return render_template('treat.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        msg = Message(f'Name:{name}, 1', sender='sender@icloud.com', recipients=['recipients@icloud.com'])
        msg.body = message
        mail.send(msg)
    else:
        return render_template('about.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        text = request.form['text']
        global serial
        serial = text
        return redirect(url_for('analyze'))

    else:
        return render_template('upload.html')


@app.route('/analyze')
def analyze():
    global serial
    try:
        result = sklearn_neural_network_classification.run(serial)
        prediction = result[0]
        r = result[1]
        if prediction == ['H1N1']:
            return render_template('h1n1.html', r=r)
        elif prediction == ['H3N2']:
            return render_template('h3n2.html', r=r)
        elif prediction == ['H5N1']:
            return render_template('h5n1.html', r=r)
        elif prediction == ['H7N7']:
            return render_template('h7n7.html', r=r)
        elif prediction == ['H7N9']:
            return render_template('h7n9.html', r=r)
        elif prediction == ['H9N2']:
            return render_template('h9n2.html', r=r)
        elif prediction == ['H10N8']:
            return render_template('h10n8.html', r=r)
        else:
            return '分析不成功，请重新输入数据。'
    except ValueError:
        return '输入的值不够，应该输入1775个。'


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/database')
def database():
    return render_template('virus_database.html')


@app.route('/database/h1n1ha')
def h1n1ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h1n1 ha`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h1n1na')
def h1n1na_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h1n1 na`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h3n2ha')
def h3n2ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h3n2 ha`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()


@app.route('/database/h3n2na')
def h3n2na_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h3n2 na`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h5n1ha')
def h5n1ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h5n1ha`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h5n1na')
def h5n1na_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h5n1 nagc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n7ha')
def h7n7ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n7 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n7na')
def h7n7na_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n7 na gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n9ha')
def h7n9ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n9 ha cds`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n9ha_gc')
def h7n9ha_gc_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n9 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n9na')
def h7n9na_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n9 na cds`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h9n2ha')
def h9n2ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h9n2 ha cds`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h9n2ha_gc')
def h9n2ha_gc_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h9n2 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h9n2na_gc')
def h9n2na_gc_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h9n2 na gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h10n8ha')
def h10n8ha_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h10n8 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h10n8na')
def h10n8na_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h10n8 na gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


if __name__ == '__main__':
    app.run()
