from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Cupcake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sabor = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(120), nullable=False, default="baunilha.svg")
    ativo = db.Column(db.Boolean, default=True, nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_nome = db.Column(db.String(100), nullable=False)
    cliente_email = db.Column(db.String(120), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(30), default="Recebido", nullable=False)
    itens = db.relationship("ItemPedido", backref="pedido", cascade="all, delete-orphan")

    @property
    def total(self):
        return sum(i.preco_unitario * i.quantidade for i in self.itens)

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedido.id"), nullable=False)
    cupcake_id = db.Column(db.Integer, db.ForeignKey("cupcake.id"), nullable=False)
    nome_cupcake = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
