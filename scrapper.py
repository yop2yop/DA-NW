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