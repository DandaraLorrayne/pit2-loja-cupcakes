# PIT II — Loja de Cupcakes

Projeto Integrador Transdisciplinar em Engenharia de Software II.

**Aluno:** Maicon Furtado  
**RGM:** 36588709  
**GitHub:** DandaraLorrayne

## Objetivo
Aplicação web para uma loja de cupcakes. O cliente consulta cardápio com foto, preço, descrição e variedade, adiciona itens ao carrinho e finaliza um pedido. A área administrativa permite cadastrar, editar e ativar/desativar produtos e consultar pedidos.

## Arquitetura e tecnologias
- Front-end: HTML5 + CSS3 (templates Jinja)
- Back-end: Python + Flask
- Persistência: Flask-SQLAlchemy + SQLite
- Organização: MVC adaptado ao Flask (Models, Templates/Views e Routes/Controllers)
- Testes: pytest

## Executar no Windows
```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python run.py
```
Abra `http://127.0.0.1:5000`.

## Testes automatizados
```bash
pytest -q
```

## GitHub
Crie um repositório vazio chamado `pit2-loja-cupcakes` na conta `DandaraLorrayne` e execute na pasta do projeto:
```bash
git init
git add .
git commit -m "PIT II - Loja de Cupcakes"
git branch -M main
git remote add origin https://github.com/DandaraLorrayne/pit2-loja-cupcakes.git
git push -u origin main
```

## Evidências que dependem de execução real
A pasta `evidencias/testes_usuarios` contém o formulário para registrar os cinco testes reais. Os links de repositório, aplicação hospedada e vídeos devem ser confirmados após publicação/gravação; não foram simulados.
