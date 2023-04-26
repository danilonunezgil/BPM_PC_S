import requests
import json


# Coloca aquí tu cliente ID
client_id = '26090'

# Coloca aquí tu clave secreta
client_secret = '2ZFXm*Bm*bkBVe)d3ZUzVw(('

# Realiza la autenticación OAuth para obtener un token de acceso
auth_url = 'https://stackoverflow.com/oauth/dialog'
auth_params = {'client_id': client_id, 'scope': 'read_inbox', 'redirect_uri': 'https://stackexchange.com/oauth/login_success'}
auth_response = requests.get(auth_url, params=auth_params)
auth_token = auth_response.url.split('access_token=')[1].split('&')[0]

# Realiza una solicitud GET para obtener las preguntas relacionadas a BPM
api_url = 'https://api.stackexchange.com/2.3/questions'
api_params = {'order': 'desc', 'sort': 'activity', 'tagged': 'bpm', 'site': 'stackoverflow', 'access_token': auth_token}
api_response = requests.get(api_url, params=api_params)

# Analiza la respuesta JSON y muestra el título de cada pregunta
json_response = json.loads(api_response.text)
for item in json_response['items']:
    print(item['title'])