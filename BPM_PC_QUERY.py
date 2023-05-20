import requests
import time
from datetime import datetime
import psycopg2

# Define los parámetros de conexión a la base de datos
conn_params = {
    "host":"localhost",
    "database":"pc_stackoverflow",
    "user": "postgres",
    "password":"4032"
}

# Establece una conexión con la base de datos
conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

url = "https://api.stackexchange.com/2.3/search"

params = {
    "key": "ahhBNdmxDJ5zP2dxaJvCHw((",
    "order": "desc",
    "sort": "votes",
    "site": "stackoverflow",
    "intitle": "jbpm",
}

questions = []

page = 1
while True:
    params["page"] = page
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        questions.extend(data["items"])
        has_more = data["has_more"]
        if not has_more:
            break
        page += 1
        if page % 30 == 0:
            print("esperando")
            time.sleep(1) # Espera 1 segundo después de cada 30 solicitudes
    else:
        print("Error al realizar la solicitud HTTP:", response.status_code)
        break

for question in questions:
    id_discussion = question["question_id"]
    topic = params["intitle"]
    title = question["title"]
    link = question["link"]
    score = question["score"]
    answer_count = question["answer_count"]
    view_count = question["view_count"]
    creation_date = datetime.fromtimestamp(question["creation_date"]).strftime("%Y-%m-%d")
    tags = ", ".join(question["tags"])
    
    if(score >= 0):
        insert_query = "INSERT INTO BPM_PC_QUERY (id_discusion,topic, title, link, score, answer_count, view_count, creation_date, tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (id_discussion,topic, title, link, score, answer_count, view_count, creation_date, tags))
        print(f"Se ha insertado la siguiente discusión en la base de datos:\nTema: {topic}\nTítulo: {title}\nLink: {link}\nNum. Votos: {score}\nNum. Respuestas: {answer_count}\nNum. Vistas: {view_count}\nFecha de creación: {creation_date}\nTags: {tags}\n{'-'*50}")
    else:
        print(f"No se ha insertado la siguiente discusión dado su votación negativa:\nTema: {topic}\nTítulo: {title}\nLink: {link}\nNum. Votos: {score}\nNum. Respuestas: {answer_count}\nNum. Vistas: {view_count}\nFecha de creación: {creation_date}\nTags: {tags}\n{'-'*50}")

# Confirma los cambios en la base de datos
conn.commit()

# Cierra la conexión con la base de datos
cursor.close()
conn.close()

print("Total discusiones encontradas: ", len(questions))
