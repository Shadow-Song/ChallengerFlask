from flask import Flask, render_template, request, redirect, url_for
import werkzeug
import sqlite3
import os

app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'  # 上传文件到这里
ALLOWED_EXTENSIONS = {'csv'}  # 允许的格式,保证安全性
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制文件大小


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
    except :
        return "未选择上传文件或文件类型不支持"


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    file = request.files['file']
    file.save('./static/uploads')
    # 处理上传的文件
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
