import requests
import json
import asyncio
import config

HEADERS = {
    'X-Key': f'Key {config.API_KEY}',
    'X-Secret': f'Secret {config.SECRET_KEY}',
}
URL = 'https://api-key.fusionbrain.ai/'


async def generate(prompt):
    params = {
        "type": "GENERATE",
        "style": "ANIME",
        "width": 1024,
        "height": 1024,
        "numImages": 1,
        "generateParams": {"query": prompt}
    }
    files = {
        'pipeline_id': (None, 'a17740da-e8a0-4816-876a-74326c5c4cef'),
        'params': (None, json.dumps(params), 'application/json')
    }
    response = requests.post(URL + 'key/api/v1/pipeline/run', headers=HEADERS, files=files)
    data = response.json()
    print(data)
    attempts = 0
    while attempts < 80:
        response = requests.get(URL + 'key/api/v1/pipeline/status/' + data['uuid'], headers=HEADERS)
        data = response.json()
        print(data)
        if data['status'] == 'DONE':
            return data['result']['files']

        attempts += 1
        await asyncio.sleep(3)  