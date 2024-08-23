"""import requests

# Insira a sua chave de API da ElevenLabs aqui
API_KEY = '797ccf834e6e157ff1354554b2e93f12'

# URL para listar as vozes
url = "https://api.elevenlabs.io/v1/voices"

# Cabeçalho da requisição, incluindo a chave da API
headers = {
    "xi-api-key": API_KEY
}

# Faz a requisição para a API
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    voices = response.json()['voices']
    
    # Procurar por vozes específicas, como "James"
    james_legacy = [voice for voice in voices if "James (Legacy)" in voice['name']]
    
    if james_legacy:
        print("Voz 'James' encontrada:")
        for voice in james_legacy:
            print(f"Nome: {voice['name']}, ID: {voice['voice_id']}")
    else:
        print("A voz 'James' não foi encontrada na lista.")
else:
    print(f"Erro: {response.status_code} - {response.text}")"""
    
import requests

API_KEY = '797ccf834e6e157ff1354554b2e93f12'
url = "https://api.elevenlabs.io/v1/voices"

headers = {
    "xi-api-key": API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    voices = response.json()['voices']
    for voice in voices:
        print(f"{voice['name']}")
else:
    print(f"Erro: {response.status_code} - {response.text}")