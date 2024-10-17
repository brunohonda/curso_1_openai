from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": "Listar apenas os nomes dos produtos, sem considerar a descrição."
    },
    {
      "role": "user",
      "content": "Liste 3 produtos sustentáveis."
    },
  ]
)

print(response.choices[0].message.content)