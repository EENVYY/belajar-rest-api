from flask import Flask, request
from flask_restful import Resource,Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

identitas = {}

class contohResourse(Resource):
    def get(self):
        # response = {"msg":"Halo dunia ini restful pertama"}

        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg":"Sukses"}
        return response


api.add_resource(contohResourse, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)