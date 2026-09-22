import pytest
from app import create_app
from app.models import db, Cupcake, Pedido

@pytest.fixture()
def client():
    app=create_app({"TESTING":True,"SQLALCHEMY_DATABASE_URI":"sqlite:///:memory:","SECRET_KEY":"test"})
    with app.test_client() as client:
        yield client

def test_cardapio_carrega(client):
    r=client.get("/")
    assert r.status_code==200
    assert "Chocolate Supremo".encode() in r.data

def test_adiciona_carrinho(client):
    r=client.post("/carrinho/adicionar/1",follow_redirects=True)
    assert r.status_code==200
    r=client.get("/carrinho")
    assert b"Chocolate Supremo" in r.data

def test_checkout_valida_email(client):
    client.post("/carrinho/adicionar/1")
    r=client.post("/checkout",data={"nome":"Maicon","email":"invalido"},follow_redirects=True)
    assert "e-mail".encode() in r.data

def test_checkout_cria_pedido(client):
    client.post("/carrinho/adicionar/1")
    r=client.post("/checkout",data={"nome":"Maicon Furtado","email":"maicon@example.com"},follow_redirects=True)
    assert r.status_code==200
    assert "Pedido confirmado".encode() in r.data

def test_admin_cadastra_produto(client):
    r=client.post("/admin/cupcakes",data={"nome":"Limão","sabor":"Limão","descricao":"Cupcake cítrico","preco":"8.90"},follow_redirects=True)
    assert r.status_code==200
    assert "Cupcake cadastrado".encode() in r.data
