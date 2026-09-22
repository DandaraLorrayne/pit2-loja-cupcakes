from flask import Flask
from .models import db


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="pit2-cupcakes-dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///cupcakes.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    from .routes import bp
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
        from .models import Cupcake
        if Cupcake.query.count() == 0:
            db.session.add_all([
                Cupcake(nome="Chocolate Supremo", sabor="Chocolate", descricao="Massa de chocolate, cobertura cremosa e confeitos.", preco=8.50, imagem="chocolate.svg"),
                Cupcake(nome="Morango Encantado", sabor="Morango", descricao="Massa de baunilha com cobertura de morango.", preco=9.00, imagem="morango.svg"),
                Cupcake(nome="Baunilha Clássica", sabor="Baunilha", descricao="Massa leve de baunilha com buttercream.", preco=7.50, imagem="baunilha.svg"),
                Cupcake(nome="Red Velvet", sabor="Red Velvet", descricao="Massa aveludada com cobertura suave de cream cheese.", preco=10.00, imagem="redvelvet.svg"),
            ])
            db.session.commit()
    return app
