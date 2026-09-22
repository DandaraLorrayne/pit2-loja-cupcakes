# Dicionário de Dados

| Tabela | Campo | Tipo | Regra |
|---|---|---|---|
| cupcake | id | INTEGER | PK, identificador |
| cupcake | nome | VARCHAR(100) | obrigatório |
| cupcake | sabor | VARCHAR(80) | obrigatório |
| cupcake | descricao | VARCHAR(255) | obrigatório |
| cupcake | preco | FLOAT | obrigatório, > 0 na aplicação |
| cupcake | imagem | VARCHAR(120) | nome do arquivo |
| cupcake | ativo | BOOLEAN | disponibilidade |
| pedido | id | INTEGER | PK |
| pedido | cliente_nome | VARCHAR(100) | obrigatório |
| pedido | cliente_email | VARCHAR(120) | obrigatório e validado |
| pedido | criado_em | DATETIME | preenchimento automático |
| pedido | status | VARCHAR(30) | padrão: Recebido |
| item_pedido | id | INTEGER | PK |
| item_pedido | pedido_id | INTEGER | FK -> pedido.id |
| item_pedido | cupcake_id | INTEGER | FK -> cupcake.id |
| item_pedido | nome_cupcake | VARCHAR(100) | snapshot do nome |
| item_pedido | quantidade | INTEGER | 1 a 20 na aplicação |
| item_pedido | preco_unitario | FLOAT | preço no momento da compra |
