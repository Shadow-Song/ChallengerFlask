from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'  # 上传文件到这里
ALLOWED_EXTENSIONS = {'csv'}  # 允许的格式,保证安全性
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制文件大小
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Sj990808',
    db='virus'
)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aVirus')
def a_virus():
    return render_template('aVirus.html')


@app.route('/defence')
def defence():
    return render_template('defence.html')


@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')


@app.route('/treat')
def treat():
    return render_template('treat.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/analyze')
def analyze():
    return render_template('analyze.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        if request.method == 'POST':
            list_file = request.files['file']
            if list_file and allowed_file(list_file.filename):
                list_filename = 'file.' + list_file.filename.rsplit('.', 1)[1]
                list_file.save(os.path.join(app.config['UPLOAD_FOLDER'], list_filename))
                redirect(url_for('analyze'))
        return render_template("upload.html")
    except:
        return "未选择上传文件或文件类型不支持"


@app.route('/database')
def database():
    return render_template('virus_database.html')


@app.route('/database/h1n1')
def h1n1_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h1n1 ha`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h3n2')
def h3n2_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h3n2 ha`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h5n1')
def h5n1_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h5n1ha`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n7')
def h7n7_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n7 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h7n9')
def h7n9_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h7n7 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h9n2')
def h9n2_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h9n2 ha cds`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/database/h10n8')
def h10n8_database():
    cur = conn.cursor()
    cur.execute("SELECT * FROM `h10n8 ha gc content`")
    data = cur.fetchall()
    column_names = [col[0] for col in cur.description]
    cur.close()
    return render_template('virus_data.html', data=data, column_names=column_names)


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    file = request.files['file']
    file.save('./static/uploads')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
