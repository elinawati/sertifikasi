from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_CONNECTION_STRING = 'mongodb://elinawati785:jadiorangsukses78@ac-al2njcq-shard-00-00.3lv71ny.mongodb.net:27017,ac-al2njcq-shard-00-01.3lv71ny.mongodb.net:27017,ac-al2njcq-shard-00-02.3lv71ny.mongodb.net:27017/?ssl=true&replicaSet=atlas-h1v4n0-shard-0&authSource=admin&retryWrites=true&w=majority'

client = MongoClient(MONGODB_CONNECTION_STRING)

db = client.dbSertifikasiEli

@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        jurusan = request.form['jurusan']
        motivasi = request.form['motivasi']

        db.regis.insert_one({
            'nim': nim,
            'nama': nama,
            'jenis_kelamin': jenis_kelamin,
            'jurusan': jurusan,
            'motivasi': motivasi
        })

        return redirect('/dashboard')
    
    return render_template('registration.html')


@app.route('/dashboard')
def dashboard():
    registrations = db.regis.find()
    return render_template('dashboard.html', registrations=registrations)

@app.route('/delete/<nim>')
def delete(nim):
    db.regis.delete_one({'nim': nim})
    
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
