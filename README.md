# BPM_PC_S
Program that consumes StackOverflow API about questions/answers related to BPM.
https://stackapps.com/apps/oauth/view/26090

# Para ejecutar el programa se necesita:

1. Realizar el registro en https://stackapps.com/users/login
2. Registrar la aplicación para obtener las credenciales que permiten usar la API de StackOverflow https://stackapps.com/apps/oauth/register
3. Obtener un cliente ID y una clave secreta de autenticación OAuth en Stack Overflow
4. Instalar el manejador de versiones GIT
5. Clonar el repositorio con: git clone https://github.com/danilonunezgil/BPM_PC_S.git
6. Reemplazar las credenciales en el código
7. Instalar Python en cualquier versión 
8. Instalar los siguientes módulos:

   pip install request (para hacer solicitudes HTTP)<br>
   pip install json (para trabajar con el formato JSON)<br>
   pip install psycopg2-binary (para conectarse y realizar operaciones con PostgreSQL)
   
7. Instalar PostgreSQL https://www.postgresql.org/download/windows/
8. Con la ayuda de pgAdmin 4, crear una base de datos llamada pc (abreviatura de platform comparison)
9. En esa misma BD, crear una tabla con la siguiente estructura:
   
   CREATE TABLE PC (
   id SERIAL PRIMARY KEY,
   title VARCHAR(255),
   link VARCHAR(255),
   score INTEGER,
   answer_count INTEGER,
   view_count INTEGER
   );
   
11. Ejecuta el programa (en este momento se encuentra en desarrollo).
    


# Limitaciones del uso de la API:
https://api.stackexchange.com/docs/throttle<br>
Máximo 30 peticiones por segundo<br>
Máximo 10.000 peticiones por día<br>
En caso de superar la máximas por día, saldrá un error HTTP 429.<br>
Se renueva cada media noche dado el caso se haya superado el límite diario.
