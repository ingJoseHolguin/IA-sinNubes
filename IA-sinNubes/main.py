import requests

def query_llm(user_input):
    # ✨ PROMPT DE CONTEXTO ESENCIAL ✨
    # Formato específico para Qwen2 (CRÍTICO para buenos resultados):
    prompt = (
        "<|im_start|>system\n"
        "Eres un asistente útil llamado Astra. Responde de forma clara y concisa.<|im_end|>\n"
        "<|im_start|>user\n"
        f"{user_input}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )
    
    response = requests.post(
        "http://localhost:1234/v1/completions",
        json={
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.3,
            "stop": ["<|im_end|>"]  # Detener en token específico
        },
        headers={"Content-Type": "application/json"}
    )
    return response.json()["choices"][0]["text"].strip()

# Chat interactivo
print("Escribe 'salir' para terminar")
while True:
    user_msg = input("\nTú: ")
    if user_msg.lower() == "salir": break
    
    response = query_llm(user_msg)
    print(f"Astra: {response}")