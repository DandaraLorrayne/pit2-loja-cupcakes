# Plano de Verificação e Validação

## Verificação automatizada
1. Cardápio retorna HTTP 200 e exibe produto inicial.
2. Produto pode ser adicionado ao carrinho.
3. Checkout rejeita e-mail inválido.
4. Checkout válido cria pedido e exibe confirmação.
5. Administração cadastra novo cupcake válido.

Execute `pytest -q`. O resultado deve ser registrado como evidência da execução no computador do aluno.

## Validação por usuários
A atividade exige cinco pessoas reais. Use `evidencias/testes_usuarios/FORMULARIO_TESTES.md`, colete nome/data/feedback e prints. Não substitua essa etapa por dados simulados.
