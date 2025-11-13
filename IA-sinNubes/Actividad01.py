import requests

def query_llm(prompt):
    url = "http://localhost:1234/v1/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["text"]

# Prueba
respuesta = query_llm("¿Qué es la inteligencia artificial?")
print("Respuesta del modelo:")
print(respuesta)