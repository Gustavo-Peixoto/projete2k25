import ollama
import json

PROMPT_BASE = """
Você é um especialista em nutrição canina.
Sua tarefa é buscar e recomendar rações seguras para um cachorro com alergias alimentares específicas.

🦴 Sites confiáveis (buscar APENAS nestes domínios):
1. https://www.purina.com.br
2. https://www.royalcanin.com.br
3. https://www.premierpet.com.br
4. https://www.golden.com.br
5. https://www.petzone.com.br

⚙️ Instruções:
- Pesquise apenas nesses sites.
- Responda em português.
- Liste no máximo 5 opções de rações seguras.
- Sem comentários externos.
- Listar a ração somente se souber que existe e se existe nos parametros de nescessidade do cachorro, caso tenha algum comentario, adicionar no local message do json. 
- Sempre adicionar comentarios em message no json, dizendo sobre as raçoes que achou, sobre a confiabilidade e dizer de forma clara o por que cada raçao é boa para o animal.
- Inclua:
    - Nome da ração
    - Marca
- Ignore resultados de fóruns, blogs ou anúncios.
- Se não houver opções seguras, diga claramente que não encontrou.

🐶 Alergias do cachorro:
{alergias}

⚠️ IMPORTANTE:
- Responda **apenas** com JSON válido.
- Não inclua aspas externas, \n ou notas.
- Não adicione comentários fora do JSON.
- Sempre o nome do array deve ser "racoes".
- Sempre JSON com formato correto.

Responda **somente** no formato JSON **chamado racoes** **com a chave racoes** apontando para a lista de rações. Por exemplo:

{{
  "racoes": [
    {{
      "nome": "",
      "marca": "",
      "mensagem": ""
    }}
  ]
}}

- Sempre use essa estrutura, sem aspas externas, sem notas, sem explicações.

"""

def buscar(alergias: dict):
    alergias_str = ", ".join([f"{k}: {v}" for k, v in alergias.items()])
    prompt_formatado = PROMPT_BASE.format(alergias=alergias_str)
    resposta = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "Você é um assistente útil e especialista em rações caninas."},
            {"role": "system", "content": "Você só pode responder JSON. Nada mais. Sem aspas externas, sem notas, sem explicações."},
            {"role": "user", "content": prompt_formatado}
        ]
    )

    conteudo = resposta["mensagem"]["content"]
    return conteudo



result = buscar({"cenoura" : "positivo", "beterraba" : "negativo"})
print(result)