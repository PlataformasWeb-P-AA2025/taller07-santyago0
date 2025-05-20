from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# OBTENCION DE DATOS - CLUB
clubs = [] # Lista para almacenar los objetos de tipo Club
with open('data/datos_clubs.txt', 'r', encoding='utf-8') as data_clubs:
    for c in data_clubs:
        row_clubs = c.strip().split(';') # Lectura de las lineas, seprandolas por ;
        # Crear un objeto de tipo Club
        # Pasarle los parametros obtenidos
        # como todos los datos son cadenas, la fundacion la transformamos a entero
        club = Club(nombre=row_clubs[0],deporte=row_clubs[1],fundacion=int(row_clubs[2]))
        print(club)
        clubs.append(club)
        session.add(club)

club1 = "" # Barcelona
club2 = "" # Independiente del Valle
club3 = "" # Mushuc Runa
club4 = "" # Universidad Católica

for c in clubs:
    if c.nombre == "Barcelona":
        club1 = c
    elif c.nombre == "Independiente del Valle":
        club2 = c
    elif c.nombre == "Mushuc Runa":
        club3 = c
    elif c.nombre == "Universidad Católica":
        club4 = c

# OBTENCION DE DATOS - CLUB
with open('data/datos_jugadores.txt', 'r', encoding='utf-8') as data_jugadores:
    for j in data_jugadores:
        row_jugadores = j.strip().split(';') # Lectura de las lineas, seprandolas por ;
        # Crear un objeto de tipo Jugador
        # En los datos de los jugadores tenemos el club por su nombre
        # y para añadirlos a la base de datos necesitamos el club como objeto
        # Pasarle los parametros obtenidos
        # como todos los datos son cadenas, el dorsal la transformamos a entero
        jugador = Jugador(nombre=row_jugadores[3],dorsal=int(row_jugadores[2]),posicion=row_jugadores[1])
        print(jugador)
        session.add(jugador)