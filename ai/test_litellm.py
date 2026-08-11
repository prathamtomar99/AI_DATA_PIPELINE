import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LITELLM_MASTER_KEY"),
    base_url="http://localhost:4000"  # use "http://litellm:4000" if run inside docker network
)

response = client.chat.completions.create(
    model="groq-oss120",
    messages=[{"role": "user", "content": "HI"}]
)

print(response.choices[0].message.content)