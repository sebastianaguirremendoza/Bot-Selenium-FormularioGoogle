import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Antes de leer los datos del CSV debes asegurarte que la lectura del CSV esta libre de errores
# Es recomendable limpiar el CSV antes de mandarlo a leer
# Esto ya que mayormente no se leen bien las tildes del CSV
# Es por ello que lo mas recomendable es limpiar el CSV con el LimpiardorCSV.py

# Coloca el archivo CSV a leer 
# Dentro de este CSV debe contener
#   nombre, correo, sexo
# En ese orden en especifico para la correcta ejecucion del bot
# (Bueno eso es dependiendo del formulario que se vaya a utilizar)
archivocsv = './CSV/datos_limpios.csv'

# Se lee el CSV
with open(archivocsv, 'r') as file:
    reader = csv.reader(file)
    # Se omite la primera fila si contiene encabezados (Solo si tienen alguno, sino pueden quitar esta funcion)
    next(reader) 
    datos = list(reader)

# Ruta del controlador de Firefox (geckodriver)
# Este driver debe estar siempre actualizado, ya que sino les saldra error en la ejecucion del driver
# Este driver es la ultima version que salio, es la verson 0.33.0
# El driver debe ser correspondiente a  su sistema operativo no confundir las version
# Un ejemplo de ello es el win-aarch64 que no es lo mismo que el win-64
driver_path = './Driver/geckodriver.exe'

# Se inicia el navegador Firefox
driver = webdriver.Firefox(executable_path=driver_path)

# Aqui se debe colocar la URL de su formulario
url = 'googleform.com'
driver.get(url)

# Esperar para cargar todo el formulario, dependiendo de su velocidad de carga se puede variar el tiempo
time.sleep(10)

# Se iteran los datos del CSV
for dato in datos:
    # Se obteniene nombre, correo y sexo del CSV
    # Esto dependera de como lo tienen estructura su CSV
    nombre = dato[0]
    correo = dato[1]
    sexo = dato[2]

    # Algunas de estas variables son opciones pero recomiendo igualmente usarlas para ahorrar codigo
    # Las variables opcionales estaran marcadas con un (O.O)
    # Para que las respuestas del formulario se vean mas "humanas" opte por randomizarlas
    # Esto ya que cada "persona" que responde el formulario tiene diferentes criterios y puntos de vista
    # Las variables opcionales (O.O) estan en intervales dependiendo de las respuetas que se puedan realizar
    # Por ejemplo las carreras universitarias que pueden ver, en mi formulario hay para seleecionar entre 14 carreras
    # Es por ello que coloque un intervalo entre el 1 y el 14 ya que sera la que se seleccionara aleatoriamente
    # Como se puede ver las variables estan en str, esto es para que puedan ser leidas y colocadas dentro de los campos
    #Variables-----------------------
    #Edad - edad promedio de los encuestados
    edad = random.randint(18, 32)
    edad_str = str(edad)
    #Carrera (O.O)
    carrera = random.randint(1, 14)
    carrera_str = str(carrera)
    #Ciclo (O.O)
    ciclo = random.randint(1, 10)
    ciclo_str = str(ciclo)
    #Si o no 1 (O.O)
    siono = random.randint(1, 2)
    siono_str = str(siono)
    #Si o no 2 (O.O)
    siono2 = random.randint(1, 2)
    siono2_str = str(siono2)
    #Monto gastado (O.O)
    monto = random.randint(1, 5)
    monto_str = str(monto)
    #Tiempo de compra (O.O)
    tiempo = random.randint(1,4)
    tiempo_str = str(tiempo)
    #Si o no 3 (O.O)
    siono3 = random.randint(1, 2)
    siono3_str = str(siono3)
    #Si o no 4 (O.O)
    siono4 = random.randint(1, 2)
    siono4_str = str(siono4)
    #Calificacion (O.O)
    cali = random.randint(1, 4)
    cali_str = str(cali)
    #Si o no 5 (O.O)
    siono5 = random.randint(1, 2)
    siono5_str = str(siono5)
    #Probable (O.O)
    prob = random.randint(1, 3)
    prob_str = str(prob)

    # Aqui se rellenaran los datos según los datos del CSV obtenidos
    # Los elementos PATH se obtienen facilmente, solo deben entrar al formulario e inspeccionar los elementos
    # Como ejemplo el correo es un input, asi que se debe seleccionar ese input y dentro del codigo del inspeccionar
    # Se debe dar en copiar y en las opciones, seleccionar copiar como PATH y les dara la dirección exacta del input
    # Esto se hace con cada opcion a rellenar

    # Rellenar el campo de correo
    print("Correo - "+correo)
    WebDriverWait(driver, 10)
    correo_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    correo_input.send_keys(correo)

    # Rellenar el campo de correo
    print("Nombre - "+nombre)
    WebDriverWait(driver, 10)
    nombre_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nombre_input.send_keys(nombre)

    # Para la seleccion del sexo es un poco diferente ya que ese apartado no debe ser aleatorio
    # Es por eso que agregue un IF y ELSE que dependera como esta en el CSV
    #   Ejemplo: sebastian,sebas@gmail.com,hombre
    # En este ejemplo se obtendra los datos de sexo y se compara para luego seleccionar la casilla con la opción de hombre

    # Aqui tambien hay un ejemplo de las casillas de radiobutton para seleccionar, en este caso como se puede ver son muy similares los PATH pero hay un numero que los diferencia
    # Gracias a este numero se podra diferenciar y seleccionar el correcto
    # Esta funcion tambien se puede abreviar colocando una variable de genero y si es hombre es 1, mujer es 2 y otro es 3
    # Pero en esta funcion se puede observar mejor como son las selecciones

    # Seleccionar sexo
    print("Sexo - "+sexo)
    WebDriverWait(driver, 10)
    if sexo == "hombre":
        boton_sexo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')))
    elif sexo == "mujer":
        boton_sexo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')))
    else:
        boton_sexo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')))

    # Este boton es para seleccionar el radio button simulando un click en el radio 
    boton_sexo.click()

    # Aqui se ven las variables donde dentor de las variables se randomizo la edad dentro de un intervalo
    # Esta edad se colocara dentro del input del formulario y para eso siempre las variables deben estar en str
    print("Edad - "+edad_str)
    WebDriverWait(driver, 10)
    edad_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    edad_input.send_keys(edad_str)

    # Aqui se ve el ejemplo de resumir el codigo por medio de los intervalos que se aleatorizaron
    # Como dentro de los radio button solo se puede seleccionar una opcion lo mas eficaz para ahorrar codigo
    # Es aleatorizar el radio que se seleccionara (siempre en str)
    # Este intervalo siempre debe estar entre los radio que tenga la pregunta
    # En este caso mi pregunta tiene 14 opciones es por ello que en las variables se pueden ver el intervalo entre 1 y 14
    # Si no fuera por la variable que coloque tendria que colocar las 14 opciones y eso me tomaria mas tiempo

    # Dentro de las funciones se pueden ver un print, esto lo coloque para que se pueda obervar en la terminal los datos que se colocan
    # Ademas hay un wait, este lo que hace es parar el bot por unos segundos para que pueda responder, esto recomiendo siempre colocarlo

    # Carrera
    print("Seleccionando carrera - "+carrera_str)
    WebDriverWait(driver, 10)
    carrera_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div['+carrera_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Se selecciona aleatoriamente la respuesta
    selec_carrera = random.choice(carrera_selec)
    # Se simula el click
    btn_carrera = driver.find_element(By.XPATH, selec_carrera)
    btn_carrera.click()

    # Esto igualmente se ve en las demas funciones donde las respuestas son en radio button
    # Ciclo
    print("Seleccionando ciclo - "+ciclo_str)
    WebDriverWait(driver, 10)
    ciclo_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div['+ciclo_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Selecciona aleatoriamente la respuesta
    selec_ciclo = random.choice(ciclo_selec)
    #  Simula click
    btn_ciclo = driver.find_element(By.XPATH, selec_ciclo)
    btn_ciclo.click()

    
    # Si o no
    print("Respondiendo si o no - "+siono_str)
    WebDriverWait(driver, 10)
    siono_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div['+siono_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Selecciona aleatoriamente la respuesta
    selec_siono = random.choice(siono_selec)
    #  Simula click
    btn_siono = driver.find_element(By.XPATH, selec_siono)
    btn_siono.click()

    
    # Si o no 2
    print("Respondiendo si o no - "+siono2_str)
    WebDriverWait(driver, 10)
    siono2_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div['+siono2_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Selecciona aleatoriamente la respuesta
    selec_siono2 = random.choice(siono2_selec)
    #  Simula click
    btn_siono2 = driver.find_element(By.XPATH, selec_siono2)
    btn_siono2.click()


    # Monto gastado
    print("Cuanto gastas - "+monto_str)
    WebDriverWait(driver, 10)
    monto_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div['+monto_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Selecciona aleatoriamente la respuesta
    selec_monto = random.choice(monto_selec)
    #  Simula click
    btn_monto = driver.find_element(By.XPATH, selec_monto)
    btn_monto.click()

    # Aqui hay ejemplo de como se varia si no usara las variables para randomizar las respuestas
    # En este caso para la seleccion multiples de casillas tuve que colocar todas las casillas que tenia mi pregunta
    # Esta parte se puede mejorar pero la deje asi aqui y en los demas xd

    #Seleccionar casillas - productos
    print("Seleccionando productos")
    WebDriverWait(driver, 10)
    producto_xpath = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[7]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[8]/label/div/div[1]/div[2]'
    ]
    # Se mide la longitud de las variables
    cantidad_selec = random.randint(1, len(producto_xpath))
    # Se selecciona aleatoriamente
    productos_seleccionados = random.sample(producto_xpath, cantidad_selec)
    # Se usa un try para capturar posibles erroes que puedan ver
    for producto_xpath in productos_seleccionados:
        try:
            producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, producto_xpath)))
            producto.click()
        except (TimeoutException, NoSuchElementException):
            print(f"No se pudo encontrar o hacer clic en el producto con XPath: {producto_xpath}")


    # Tiempo en comprar
    print("Tiempo en comprar - "+tiempo_str)
    WebDriverWait(driver, 10)
    tiempo_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div['+tiempo_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Seleccionar aleatoriamente la respuesta
    selec_tiempo = random.choice(tiempo_selec)
    # Hacer clic en el botón seleccionado
    btn_tiempo = driver.find_element(By.XPATH, selec_tiempo)
    btn_tiempo.click()


    #Seleccionar casillas - productos
    print("Seleccionando productos a añadir")
    WebDriverWait(driver, 10)
    productadd_xpath = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]'
    ]
    cantidadproduct_selec = random.randint(1, len(productadd_xpath))
    addproductos_seleccionados = random.sample(productadd_xpath, cantidadproduct_selec)
    for productadd_xpath in addproductos_seleccionados:
        try:
            producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, productadd_xpath)))
            producto.click()
        except (TimeoutException, NoSuchElementException):
            print(f"No se pudo encontrar o hacer clic en el producto con XPath: {productadd_xpath}")

    # Si o no 3
    print("Respondiendo si o no - "+siono3_str)
    WebDriverWait(driver, 10)
    siono3_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div['+siono3_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Seleccionar aleatoriamente un botón de respuesta
    selec_siono3 = random.choice(siono3_selec)
    # Hacer clic en el botón seleccionado
    btn_siono3 = driver.find_element(By.XPATH, selec_siono3)
    btn_siono3.click()


    # Si o no 4
    print("Respondiendo si o no - "+siono4_str)
    WebDriverWait(driver, 10)
    siono4_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div['+siono4_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Seleccionar aleatoriamente un botón de respuesta
    selec_siono4 = random.choice(siono4_selec)
    # Hacer clic en el botón seleccionado
    btn_siono4 = driver.find_element(By.XPATH, selec_siono4)
    btn_siono4.click()


    # Calificar
    print("Calicacion - "+cali_str)
    WebDriverWait(driver, 10)
    cali_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div['+cali_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Seleccionar aleatoriamente un botón de respuesta
    selec_cali = random.choice(cali_selec)
    # Hacer clic en el botón seleccionado
    btn_cali = driver.find_element(By.XPATH, selec_cali)
    btn_cali.click()


    #Aspectos a mejorar
    print("Seleccionando mejoras")
    WebDriverWait(driver, 10)
    mejora_xpath = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]',
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]'
    ]
    cantidadmejora_selec = random.randint(1, len(mejora_xpath))
    mejora_seleccionados = random.sample(mejora_xpath, cantidadmejora_selec)
    for mejora_xpath in mejora_seleccionados:
        try:
            producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, mejora_xpath)))
            producto.click()
        except (TimeoutException, NoSuchElementException):
            print(f"No se pudo encontrar o hacer clic en el producto con XPath: {mejora_xpath}")


    # Si o no 5
    print("Respondiendo si o no - "+siono5_str)
    WebDriverWait(driver, 10)
    siono5_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div['+siono5_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Seleccionar aleatoriamente un botón de respuesta
    selec_siono5 = random.choice(siono5_selec)
    # Hacer clic en el botón seleccionado
    btn_siono5 = driver.find_element(By.XPATH, selec_siono5)
    btn_siono5.click()


    # Probabilidad de usar el cafetin
    print("Probabilidad - "+prob_str)
    WebDriverWait(driver, 10)
    prob_selec = [
        '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div['+prob_str+']/label/div/div[1]/div/div[3]/div'
    ]
    # Seleccionar aleatoriamente un botón de respuesta
    selec_prob = random.choice(prob_selec)
    # Hacer clic en el botón seleccionado
    btn_prob = driver.find_element(By.XPATH, selec_prob)
    btn_prob.click()

    # Una vez respondidas todas las respuestas solo queda enviar el formularia donde igualemnte se buscara su PATH

    # Enviar el formulario
    enviar_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
    enviar_button.click()

    # Una vez enviardo el formulario, debemos de volver nueavamente al formulario es por ello que se debe
    # simular hacer click en "Enviar otra respueta" (Esto depende de como esta configurado tu formulario)

    # Volver al formulario
    volver_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    volver_button.click()

    # Una vez de vuelta al formulario nuevamente hacemos "descansar" al bot para que se pueda volver a cargar todos los parametros nuevamente

    #Duerme
    WebDriverWait(driver,100)
    print("--------------------------Formulario ok--------------------------")
    time.sleep(3)

    #Una vez que "despierte" el bot se formulario se volvera a responder hasta acabar todos los campos del CSV

# Una vez que el bot termine de consumir todos los campos del CSV se cerrara automaticamente el firefox
driver.quit()
