#https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(35), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    cargo = db.Column(db.String(35), nullable=False)

    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo


class FuncSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'nome', 'idade', 'cargo')


Func_schema = FuncSchema()
Funcs_schema = FuncSchema(many=True)


# endpoint to create new funcionario
@app.route("/funcionario", methods=["POST"])
def add_func():
    nome = request.json['nome']
    idade = request.json['idade']
    cargo = request.json['cargo']

    new_func = Funcionario(nome, idade, cargo)

    db.session.add(new_func)
    db.session.commit()

    return jsonify(new_func)


# endpoint to show all funcionarios
@app.route("/funcionario", methods=["GET"])
def get_func():
    all_funcs = Funcionario.query.all()
    result = Funcs_schema.dump(all_funcs)
    return jsonify(result.data)


# endpoint to get funcionario detail by id
@app.route("/funcionario/<id>", methods=["GET"])
def func_detail(id):
    func = Funcionario.query.get(id)
    return Func_schema.jsonify(Funcionario)


# endpoint to update funcionario
@app.route("/funcionario/<id>", methods=["PUT"])
def func_update(id):
    func = Funcionario.query.get(id)
    nome = request.json['nome']
    idade = request.json['idade']
    cargo = request.json['cargo']

    funcionario.nome = nome
    funcionario.idade = idade
    funcionario.cargo = cargo

    db.session.commit()
    return Func_schema.jsonify(funcionario)


# endpoint to delete funcionario
@app.route("/funcionario/<id>", methods=["DELETE"])
def func_delete(id):
    func = Funcionario.query.get(id)
    db.session.delete(func)
    db.session.commit()

    return Func_schema.jsonify(func)


if __name__ == '__main__':
    app.run(debug=True)