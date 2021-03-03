# globant_test
prueba técnica

Api desarrollada en Python - Flask con las siguientes caracteristicas:

1. Consumo de API Externa
2. Adecuación de datos
3. Caché de lado del servidor de 2 minutos (a menos que cambien los parámetros)
4. Respuesta con el header solicitado ("Apllication/Json")
5. Prueba básica verificando algunos de los datos, realizando un Mock de la funciona de procesamientos de datos

como correr:
1. Clonar el repositorio con el comando "git clone https://github.com/ingcoty/globant_test.git"
2. Entrar en el directorio creado "globant_test" con los comandos "cd globant_test"
3. Crear un ambiente virtual con Virtualenv 
4. Instalar todos los paquetenes necesarios con el comando "pip install -r requirements.txt"
5. Salir de la carpeta con el comando "cd .."
6. Exportar el Token para consumo del API con el comando "export TOKEN=1508a9a4840a5574c822d70ca2132032"
7. Para correr el servicio ejecutar la carpeta como módulo "python -m globant_test.weather"
8. Probar su funcionamiento con los parametros entregados ej: GET localhost:5000/weather?city=$City&country=$Country&
9. Para probar el test correr el comando "pytest globant_test"

Por falta de tiempo no alcancé a realizar todas las pruebas, pero se muestra una de las pruebas mas completas.
