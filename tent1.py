from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Funcionario(db.Model):
	Id = db.Column(db.Integer, primary_key=True)
	Nome = db.Column(db.String(35), nullable=False)
	Idade = db.Column(db.Integer, nullable=False)
	Cargo = db.Column(db.String(35), nullable=False)


def __repr__(self):
	return f"Funcionario('{self.Id}', '{self.Nome}', '{self.Idade}', '{self.Cargo}')"