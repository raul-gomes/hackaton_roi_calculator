import json


# Ler estrutura básica (opcional, para referência)
with open('input.json', 'r', encoding='utf-8') as f:
    estrutura_basica = json.load(f)

# Aqui, você teria a variável recebida dinamicamente do seu app:
# Exemplo: json_input_recebido_pelo_app vem da interface Streamlit
dados_usuario = json.loads(json_input_recebido_pelo_app)

# Carrega o prompt genérico (main_prompt.md)
with open('main_prompt.md', 'r', encoding='utf-8') as file:
    prompt = file.read()

# Substitui dinamicamente no prompt os valores fornecidos pelo usuário
for key, value in dados_usuario.items():
    placeholder = f'{{{{{key}}}}}'
    if value in [None, [], ""]:
        substituicao = "Usuário não forneceu; precisa de sugestões adequadas."
    else:
        substituicao = ', '.join(value) if isinstance(value, list) else str(value)

    prompt = prompt.replace(placeholder, substituicao)

# Agora você pode usar a variável 'prompt' para enviar à API da OpenAI
