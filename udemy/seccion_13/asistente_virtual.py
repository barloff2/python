import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from os import system

system('cls')

''' Programación de asistente virtual'''

# Opción Voz
id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'


# Escucha microfono y devolver audio como texto
def transformar_audio_en_texto():
    # Almacenar el recognizer en una variable
    r = sr.Recognizer()

    # Configurar microfono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabación
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language='es-co')

            # prueba de que pudo ingresar
            print('Dijiste ' + pedido)

            # devolver pedido
            return pedido
        except sr.UnknownValueError:

            # Prueba de que no compendio el audio
            print('Ups no entendi')

            # devolver error
            return 'sigo esperando'

        # En caso de no resolver el pedido

        except sr.RequestError:

            # Prueba de que no compendio el audio
            print('Ups no hay servicio')

            # devolver error
            return 'sigo esperando'
        # Error inesperado
        except:
            # Prueba de que no compendio el audio
            print('Ups, algo ha salido mal')

            # devolver error
            return 'sigo esperando'


# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Setear voz
    engine.setProperty('voice', id)

    # Pronunciar mensaje y esperar
    engine.say(mensaje)
    engine.runAndWait()


# Informar dia de la semana
def pedir_dia():
    # Crear variable con datos hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres de dias
    dias_semana = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }

    # decir el día de la semana
    hablar(f'Hoy es {dias_semana[dia_semana]}')


# Informar Hora
def pedir_hora():
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    print(hora)

    # modificar hora 
    hora = f'En este momento son las: {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'

    # decir la hora
    hablar(hora)


# funcion saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    # decir saludo
    hablar(f'{momento}, soy Cortana, tu asistente personal, por favor, dime en que te puedo ayudar')


# Funcion central del asistente
def pedir_cosas():
    # Activar el saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True
    # Loop central
    while comenzar:
        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com.co')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f'Esto fue lo que encontre: {resultado}')
            continue
        elif 'busca en internet' in pedido:
            hablar('Estoy buscando en internet')
            pywhatkit.search(pedido.replace('busca en internet', ''))
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                precio_actual = yf.Ticker(accion_buscada).info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual} dolares')
                continue
            except:
                hablar('Perdon, pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Adios kre kk')
            break


pedir_cosas()
