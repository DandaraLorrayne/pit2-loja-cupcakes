from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import db, Cupcake, Pedido, ItemPedido
import re

bp = Blueprint("main", __name__)

def carrinho():
    return session.setdefault("carrinho", {})

@bp.route("/")
def index():
    return render_template("index.html", cupcakes=Cupcake.query.filter_by(ativo=True).all())

@bp.post("/carrinho/adicionar/<int:cupcake_id>")
def adicionar(cupcake_id):
    cupcake = db.session.get(Cupcake, cupcake_id)
    if not cupcake or not cupcake.ativo:
        flash("Produto indisponível.", "erro")
        return redirect(url_for("main.index"))
    cart = carrinho()
    key = str(cupcake_id)
    cart[key] = min(int(cart.get(key, 0)) + 1, 20)
    session.modified = True
    flash(f"{cupcake.nome} adicionado ao carrinho.", "sucesso")
    return redirect(request.referrer or url_for("main.index"))

@bp.route("/carrinho")
def ver_carrinho():
    itens=[]; total=0
    for cid, qtd in carrinho().items():
        cupcake=db.session.get(Cupcake, int(cid))
        if cupcake:
            subtotal=cupcake.preco*int(qtd); total+=subtotal
            itens.append({"cupcake":cupcake,"quantidade":int(qtd),"subtotal":subtotal})
    return render_template("carrinho.html", itens=itens, total=total)

@bp.post("/carrinho/atualizar/<int:cupcake_id>")
def atualizar(cupcake_id):
    try: qtd=int(request.form.get("quantidade","1"))
    except ValueError: qtd=1
    cart=carrinho(); key=str(cupcake_id)
    if qtd <= 0: cart.pop(key, None)
    else: cart[key]=min(qtd,20)
    session.modified=True
    return redirect(url_for("main.ver_carrinho"))

@bp.post("/checkout")
def checkout():
    nome=request.form.get("nome","").strip(); email=request.form.get("email","").strip()
    if len(nome)<3 or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        flash("Informe nome válido e e-mail válido.", "erro")
        return redirect(url_for("main.ver_carrinho"))
    if not carrinho():
        flash("O carrinho está vazio.", "erro")
        return redirect(url_for("main.index"))
    pedido=Pedido(cliente_nome=nome, cliente_email=email)
    db.session.add(pedido)
    for cid,qtd in carrinho().items():
        cupcake=db.session.get(Cupcake,int(cid))
        if cupcake and cupcake.ativo:
            pedido.itens.append(ItemPedido(cupcake_id=cupcake.id,nome_cupcake=cupcake.nome,quantidade=int(qtd),preco_unitario=cupcake.preco))
    if not pedido.itens:
        db.session.rollback(); flash("Não há produtos válidos no pedido.", "erro")
        return redirect(url_for("main.index"))
    db.session.commit(); session["carrinho"]={}
    return render_template("sucesso.html", pedido=pedido)

@bp.route("/admin")
def admin():
    return render_template("admin.html", cupcakes=Cupcake.query.order_by(Cupcake.id).all(), pedidos=Pedido.query.order_by(Pedido.id.desc()).all())

@bp.post("/admin/cupcakes")
def criar_cupcake():
    nome=request.form.get("nome","").strip(); sabor=request.form.get("sabor","").strip(); desc=request.form.get("descricao","").strip()
    try: preco=float(request.form.get("preco","0").replace(",","."))
    except ValueError: preco=0
    if not nome or not sabor or not desc or preco<=0:
        flash("Preencha todos os campos e informe um preço maior que zero.", "erro")
        return redirect(url_for("main.admin"))
    db.session.add(Cupcake(nome=nome,sabor=sabor,descricao=desc,preco=preco,imagem="baunilha.svg"))
    db.session.commit(); flash("Cupcake cadastrado.", "sucesso")
    return redirect(url_for("main.admin"))

@bp.post("/admin/cupcakes/<int:cupcake_id>/editar")
def editar_cupcake(cupcake_id):
    c=db.session.get(Cupcake,cupcake_id)
    if not c: flash("Produto não encontrado.","erro"); return redirect(url_for("main.admin"))
    nome=request.form.get("nome","").strip(); sabor=request.form.get("sabor","").strip(); desc=request.form.get("descricao","").strip()
    try: preco=float(request.form.get("preco","0").replace(",","."))
    except ValueError: preco=0
    if not nome or not sabor or not desc or preco<=0:
        flash("Dados inválidos para atualização.","erro"); return redirect(url_for("main.admin"))
    c.nome=nome; c.sabor=sabor; c.descricao=desc; c.preco=preco
    db.session.commit(); flash("Cupcake atualizado.","sucesso"); return redirect(url_for("main.admin"))

@bp.post("/admin/cupcakes/<int:cupcake_id>/alternar")
def alternar_cupcake(cupcake_id):
    c=db.session.get(Cupcake,cupcake_id)
    if c: c.ativo=not c.ativo; db.session.commit(); flash("Disponibilidade alterada.","sucesso")
    else: flash("Produto não encontrado.","erro")
    return redirect(url_for("main.admin"))
