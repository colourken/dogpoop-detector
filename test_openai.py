import httpx, os

for line in open('C:/DogPoopAI/.env').read().splitlines():
    if line.startswith('OPENAI_API_KEY='):
        os.environ['OPENAI_API_KEY'] = line.split('=', 1)[1].strip()

from openai import OpenAI
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    http_client=httpx.Client()
)
print(client.models.list().data[0].id)