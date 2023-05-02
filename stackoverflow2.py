import requests
import psycopg2

# Define los parámetros de conexión a la base de datos
conn_params = {
    "host":"localhost",
    "database":"bpm",
    "user": "postgres",
    "password":"4032"
}
# Define el URL del endpoint de la API y los parámetros
url = "https://api.stackexchange.com/2.3/search"
params = {
    "site": "stackoverflow",
    "key": "ahhBNdmxDJ5zP2dxaJvCHw((",
    "intitle": "bpm",
    "sort": "creation",
    "order": "desc"
}

# Inicializar el contador de solicitudes
requests_count = 0

# Conecta a la base de datos
conn = psycopg2.connect(**conn_params)

# Crea un cursor para realizar operaciones en la BD
cur = conn.cursor()

# Envía la solicitud GET a la API y obtiene la respuesta
response = requests.get(url, params=params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener todas las preguntas de la respuesta
    questions = response.json()["items"]
    for question in questions:
        # Incrementa el contador de solicitudes
        requests_count += 1
        print("Title:", question["title"])
        print("Link:", question["link"])
        print("Votes:", question["score"])
        print("Answers:", question["answer_count"])
        print("Views:", question["view_count"])
        print()

        # Inserta los resultados en la tabla issues_bpm
        cur.execute("""
            INSERT INTO issues_bpm (title, link, score, answer_count, view_count)
            VALUES (%s, %s, %s, %s, %s)
        """, (question["title"], question["link"], question["score"], question["answer_count"], question["view_count"]))

    # Imprime el número total de solicitudes realizadas
    print(f"Requests count: {requests_count}")
    quota_remaining = response.json()['quota_remaining']
    print(f'You can do {quota_remaining} request more')

    # Confirma la transaccion en la BD
    conn.commit()
else:
    print("Error:", response.status_code)

# Cierra el cursor y la conexión a la base de datos
cur.close()
conn.close()