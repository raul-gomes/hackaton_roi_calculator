import json
import openai

response = openai.ChatCompletion.create(
    model="gpt-4-mini",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"}
)

relatorio_gerado = json.loads(response.choices[0].message.content)

# salva automaticamente no output.json:
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(relatorio_gerado, f, ensure_ascii=False, indent=4)
