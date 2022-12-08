# Postulación NeuralWorks

## Adjunto va un archivo .sqlite, comienza por crear una base de datos con este archivo y familiarízate con la data.

Bueno revisando los datos, y familiarizandome con cada tabla que se encuentra en el archivo. 

### Información de tablas
Se tiene la tabla de paises, donde se contienen 11 países de Europa.
```zh
Country(id, name)
```
Se tiene la tabla de Ligas, donde se contienen 11 ligas distintas, (una liga por país).
```zh 
League(id, country_id, name)
```

Se tiene la tabla de Partidos, donde se contienen 25979 partidas, se pueden ver información de los partidos, los goles hechos por cada equipo, los jugadores que tiene cada equipo y el ID de cada jugador (que se relaciona con la tabla de Player, principalmente). Tambien se tienen estadisticas de tiros, faltas, corner. Y por ultimo se tienen la información de las casas de apuestas en cual en el siguiente link se puede tener más información [link](https://github.com/woobe/footballytics/blob/master/data/notes.txt) el significado de cada sigla.
```zh 
Match(id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, away_team_api_id, home_team_goal, away_team_goal, home_player_X1, home_player_X2, home_player_X3, home_player_X4, home_player_X5, home_player_X6, home_player_X7, home_player_X8, home_player_X9, home_player_X10, home_player_X11, away_player_X1, away_player_X2, away_player_X3, away_player_X4, away_player_X5, away_player_X6, away_player_X7, away_player_X8, away_player_X9, away_player_X10, away_player_X11, home_player_Y1, home_player_Y2, home_player_Y3, home_player_Y4, home_player_Y5, home_player_Y6, home_player_Y7, home_player_Y8, home_player_Y9, home_player_Y10, home_player_Y11, away_player_Y1, away_player_Y2, away_player_Y3, away_player_Y4, away_player_Y5, away_player_Y6, away_player_Y7, away_player_Y8, away_player_Y9, away_player_Y10, away_player_Y11, home_player_1, home_player_2, home_player_3, home_p, layer_4, home_player_5, home_player_6, home_player_7, home_player_8, home_player_9, home_player_10, home_player_11, away_player_1, away_player_2, away_player_3, away_player_4, away_player_5, away_player_6, away_player_7, away_player_8, away_player_9, away_player_10, away_player_11, goal, shoton, shotoff, foulcommit, card, `cross`, corner, possession, B365H, B365D, B365A, BWH, BWD, BWA, IWH, IWD, IWA, LBH, LBD, LBA, PSH, PSD, PSA, WHH, WHD, WHA, SJH, SJD, SJA, VCH, VCD, VCA, GBH, GBD, GBA, BSH, BSD, BSA)
```


Se tiene la tabla de Player,  existe información de 11060
```zh 
Player(id, player_api_id, player_name, player_fifa_api_id, birthday, height, weight) 
```

Se tiene la tabla de Atributos de los jugadores, existen 183978 datos, dado que es información de los jugadores por año, ya que con el transcurso de los años pueden mejorar o bajar su rendimiento.  Aquí se tiene la información se tienen estadisticas proveidas por fifa que pueden dar un mejor desempeño a cada jugador.
```zh 
Player_Attributes(id, player_fifa_api_id, player_api_id, date, overall_rating, potential, preferred_foot, attacking_work_rate, defensive_work_rate, crossing, finishing, heading_accuracy, short_passing, volleys, dribbling, curve, free_kick_accuracy, long_passing, ball_control, acceleration, sprint_speed, agility, reactions, balance, shot_power, jumping, stamina, strength, long_shots, aggression, interceptions, positioning, vision, penalties, marking, standing_tackle, sliding_tackle, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes)
```

Se tiene la información de los equipos, en total hay 299, que podemos obtener tener los nombres de cada equipo y sus abreviaciones. 
```zh 
Team(id, team_api_id, team_fifa_api_id, team_long_name, team_short_name)
```

Se tiene la información de los equipos, en total hay 1458.  Aquí se tiene la información se tienen estadisticas proveidas por fifa que pueden dar un mejor desempeño a cada Equipo a lo largo de los años.
Personalmente digo que falta la columna que diga de que país perteneve cada equipo, pero se puede obtener directamente sabiendo en que Match juega, a que Liga pertenece el partido y luego relacionar con el país perteneciente a la Liga.
```zh 
Team_Attributes(id, team_fifa_api_id, team_api_id, date, buildUpPlaySpeed, buildUpPlaySpeedClass, buildUpPlayDribbling, buildUpPlayDribblingClass, buildUpPlayPassing, buildUpPlayPassingClass, buildUpPlayPositioningClass, chanceCreationPassing, chanceCreationPassingClass, chanceCreationCrossing, chanceCreationCrossingClass, chanceCreationShooting, chanceCreationShootingClass, chanceCreationPositioningClass, defencePressure, defencePressureClass, defenceAggression, defenceAggressionClass, defenceTeamWidth, defenceTeamWidthClass, defenceDefenderLineClass)
```


## Las tablas de Match, League, Country y Team tiene toda la información para describir un partido detalladamente. Crea una query SQL para obtener la información detallada por partido uniendo las tablas Match, League, Country y Team.

Se realiza la siguiente query, para unir las tablas **Match, League, Country y Team.** Utilizo la tabla Match como la principal, y luego las uno con la tabla League según su ID, Country según su ID y utilizo la tabla Team para unirla dos veces como equipos que juegan en local y equipos que juegan de visita.

```sql
SELECT m.id, m.country_id, c.name as CountryName, m.league_id, l.name as LeagueName ,m.season, m.stage, m.date, m.match_api_id, m.home_team_api_id, ht.team_long_name as home_team_LongName, ht.team_short_name as home_team_Short_name, m.away_team_api_id, at.team_long_name as away_team_LongName, at.team_short_name as away_team_Short_name, m.home_team_goal, m.away_team_goal, m.home_player_X1, m.home_player_X2, m.home_player_X3, m.home_player_X4, m.home_player_X5, m.home_player_X6, m.home_player_X7, m.home_player_X8, m.home_player_X9, m.home_player_X10, m.home_player_X11, m.away_player_X1, m.away_player_X2, m.away_player_X3, m.away_player_X4, m.away_player_X5, m.away_player_X6, m.away_player_X7, m.away_player_X8, m.away_player_X9, m.away_player_X10, m.away_player_X11, m.home_player_Y1, m.home_player_Y2, m.home_player_Y3, m.home_player_Y4, m.home_player_Y5, m.home_player_Y6, m.home_player_Y7, m.home_player_Y8, m.home_player_Y9, m.home_player_Y10, m.home_player_Y11, m.away_player_Y1, m.away_player_Y2, m.away_player_Y3, m.away_player_Y4, m.away_player_Y5, m.away_player_Y6, m.away_player_Y7, m.away_player_Y8, m.away_player_Y9, m.away_player_Y10, m.away_player_Y11, m.home_player_1, m.home_player_2, m.home_player_3, m.home_player_4, m.home_player_5, m.home_player_6, m.home_player_7, m.home_player_8, m.home_player_9, m.home_player_10, m.home_player_11, m.away_player_1, m.away_player_2, m.away_player_3, m.away_player_4, m.away_player_5, m.away_player_6, m.away_player_7, m.away_player_8, m.away_player_9, m.away_player_10, m.away_player_11, m.goal, m.shoton, m.shotoff, m.foulcommit, m.card, m.cross, m.corner, m.possession, m.B365H, m.B365D, m.B365A, m.BWH, m.BWD, m.BWA, m.IWH, m.IWD, m.IWA, m.LBH, m.LBD, m.LBA, m.PSH, m.PSD, m.PSA, m.WHH, m.WHD, m.WHA, m.SJH, m.SJD, m.SJA, m.VCH, m.VCD, m.VCA, m.GBH, m.GBD, m.GBA, m.BSH, m.BSD, m.BSA
FROM Match m
LEFT JOIN League l ON m.league_id = l.id
LEFT JOIN Country c ON m.country_id = c.id
LEFT JOIN Team ht ON m.home_team_api_id = ht.team_api_id
LEFT JOIN Team at ON m.away_team_api_id = at.team_api_id
```

## ¿Qué insights ves en la información detallada del partido?
 Con estos datos, podría proporcionar información sobre el rendimiento de cada equipo en cada temporada, los equipos más exitosos de cada liga y las puntuaciones más comunes. También podría analizar el promedio de goles anotados por partido, el promedio de goles concedidos por partido y el promedio de puntos obtenidos por cada equipo. Además, podría comparar el rendimiento de las ligas de diferentes países y los rendimientos de las ligas durante el período de tiempo dado. Con los datos de apuestas, podría proporcionar información sobre los equipos más exitosos en términos de cuotas de apuestas, así como qué equipos fueron consistentemente subvalorados o sobrevalorados por el mercado. También podría comparar el rendimiento de diferentes países y ligas durante el período de tiempo dado en términos de cuotas de apuestas. Además, podría analizar la precisión de los diversos mercados de apuestas para predecir los resultados de los partidos.

## Dado que queremos armar un equipo maravilloso nos interesa tener un perfil por cada jugador. Ocupa SQL y/o Python para crear un Dataframe que tenga un jugador por fila con toda la información que creas relevante

Aquí voy a juntar las tablas de los jugadores con la tabla de sus atributos, sin necesidad de filtrar por años

```sql
SELECT pa.id, p.player_api_id, p.player_name, p.player_fifa_api_id, p.birthday, p.height, p.weight, pa.player_fifa_api_id, pa.player_api_id, pa.date, pa.overall_rating, pa.potential, pa.preferred_foot, pa.attacking_work_rate, pa.defensive_work_rate, pa.crossing, pa.finishing, pa.heading_accuracy, pa.short_passing, pa.volleys, pa.dribbling, pa.curve, pa.free_kick_accuracy, pa.long_passing, pa.ball_control, pa.acceleration, pa.sprint_speed, pa.agility, pa.reactions, pa.balance, pa.shot_power, pa.jumping, pa.stamina, pa.strength, pa.long_shots, pa.aggression, pa.interceptions, pa.positioning, pa.vision, pa.penalties, pa.marking, pa.standing_tackle, pa.sliding_tackle, pa.gk_diving, pa.gk_handling, pa.gk_kicking, pa.gk_positioning, pa.gk_reflexes
FROM Player_Attributes pa
LEFT JOIN Player p ON pa.player_fifa_api_id = p.player_fifa_api_id
```

## ¿Qué insights ves en el perfil por jugador? ¿Qué data crees que es relevante para elegir a los mejores jugadores?

Con los datos de los atributos del jugador, podría formar mi propio equipo de fútbol seleccionando jugadores que tengan los mejores atributos generales para las posiciones que necesito llenar. También podría analizar los índices de trabajo ofensivo y defensivo de cada jugador para determinar qué jugadores son los más eficaces en sus respectivos roles. Además, podría usar los atributos del GK para seleccionar un portero que se adapte mejor al estilo de juego de mi equipo. 
Al realizar este filtro se elige a Julio Cesar como el mejor arquero del set de datos. Posteriormente se selecciona a 10 jugadores, pero filtrando las estadisticas de portero por lo que mi equipo ideal sería Steven Gerrard, Pavel Nedved, Frank Lampard, Maicon,Michael Essien, Daniele De Rossi, Daniel Alves,Wayne Rooney, Michael Ballack y Cesc Fabrega. Esta selección se puede ver mejor en el notebook, donde promedio sus estadisticas y elijo a los mejores 10 (asumiendo que el equipo es de 11 y no debo elegir a la bancada).


## ¿Cuál es tu sugerencia de jugadores para armar el mejor equipo de la historia? Argumenta tu respuesta.

Primero, podemos hacer un filtro por cada año, para elegir al mejor equipo de cada año.

Luego los datos más importantes de MCD en un jugador de fútbol son los atributos físicos del jugador, como la velocidad, la agilidad, la fuerza y la resistencia. Además, los atributos técnicos del jugador, como el control de la pelota, la precisión en el pase y la precisión en el disparo, también son importantes. Por último, los atributos mentales del jugador, como la toma de decisiones, la concentración y la compostura, también son factores importantes a la hora de determinar el rendimiento global de un jugador.

Uno de los atributos mentales que podemos agregar es la posición Favorita de cada jugador, y que pueda jugar a esa posición:

 - POR – Portero
 - LI – Lateral izquierdo
 - LD – Lateral derecho
 - CAD – Carrilero derecho
 - CAI – Carrilero izquierdo
 - DFC – Defensa central
 - MCD – Mediocentro defensivo
 - MC – Mediocentro
 - MI – Medio izquierdo
 - MD – Medio derecho
 - MCO – Mediocentro ofensivo
 - ED – Exterior derecho
 - EI – Exterior izquierdo
 - MP – Mediapunta
 - SDD – Segundo delantero derecho
 - SDI – Segundo delanterio izquierdo
 - DC – Delantero centro


```python
import requests
import bs4 as bs
import sqlite3

con = sqlite3.connect('database.sqlite')

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS player_value (
                ID varchar(15) NOT NULL,
                POSITION varchar(255),
                VALUE int,
                WAGE int
            );""")

def status_extraccion():
    generator_player_ID = cur.execute("SELECT player_fifa_api_id FROM Player;")
    list_player_ID = [str(id[0]) for id in generator_player_ID]
    print("Hay {} jugadores en total".format(len(list_player_ID)))
    generator_value_ID = cur.execute("SELECT ID FROM player_value;")
    list_value_ID = [str(id[0]) for id in generator_value_ID]
    print("Hay {} jugadores con sus valores".format(len(list_value_ID)))
    list_ID = list(set(list_player_ID) - set(list_value_ID))
    print("Faltan extraer datos de {} jugadores.".format(len(list_ID)))
    return list_ID

list_ID = status_extraccion()

insert_player = "INSERT INTO player_value VALUES (?,?,?,?)"

for index, id_jugador_fifa in enumerate(list_ID):
    r = requests.get("https://www.fifaindex.com/es/player/{}/".format(id_jugador_fifa))
    soup = bs.BeautifulSoup(r.text,'html')
    try:
        post = soup.find("a", attrs = {"class":"link-position"}).text
    except:
        post = "None"
    try:
        value = soup.find("p", attrs = {"class":"data-currency-dollar"}).find("span").text[1:].replace(".","")
        wage = soup.find_all("p", attrs = {"class":"data-currency-dollar"})[1].find("span").text[1:].replace(".","")
    except:
        value, wage = 0, 0
    cur.execute( insert_player, ( id_jugador_fifa , post,  value, wage))
    if index%50==0:
        print(( id_jugador_fifa , post,  value, wage))
        print(index/len(list_ID)*100)
        status_extraccion()
        con.commit()
```

Con eso podemos generar la siguiente tabla.

|Index| ID| 	POSITION| 	VALUE| 	WAGE
| ---| --|---|-----|--- |
|0	|2	|MI	|675000	|7000
|1	|6	|POR	|3000	|8000
|2	|163848	|LI	|110000	|1700
|3	|11	|MC	|300000	|5000
|4	|163852	|MCD	|160000	|1700
|...	|...	|...	|...	|...

Con esa tabla podemos poner a los jugadores en sus prosiciones favoritas, y además podemos hasta tener el equipo que no supere un valor o costo de sueldo mayor a un límite, así podemos construir equipos buenos y baratos.