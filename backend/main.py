from fastapi import FastAPI, Request
import os
import openai

app = FastAPI()

# Chave da API do OpenAI (use variável de ambiente)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat_with_ai(request: Request):
    body = await request.json()
    user_message = body.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente inteligente."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message["content"]
    return {"reply": reply}
