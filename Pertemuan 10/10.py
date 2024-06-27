from flask import Flask, request, jsonify


app = Flask(__name__)


data_mhs = [
    {"id": 0,
     "nama": "Ucok",
     "nim": "369",
     "ipk": "0.1"},
    {"id": 1,
     "nama": "Joni",
     "nim": "333",
     "ipk": "0.5"},
    {"id": 2,
     "nama": "Cici",
     "nim": "300",
     "ipk": "1.5"},
    {"id": 3,
     "nama": "Ara",
     "nim": "396",
     "ipk": "3.0"}
]


@app.route('/home')
def page_home():
    return "Selamat Datang, " + data_mhs[0]['nama']


@app.route('/mahasiswa', methods = ['GET', 'POST'])
def page_mahasiswa():
    if request.method == 'GET':
        if len(data_mhs) > 0:
            return jsonify(data_mhs)
        else:
            return "Data Kosong"


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 105)