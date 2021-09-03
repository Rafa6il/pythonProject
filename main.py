import requests
import sys

APIKEY = '67422af3a25ed304bc3f605989c25d03'  # your API Key here as string


def getTiempo(ciudad):
    url = f"https://api.openweathermap.org/data/2.5/weather?lang=es&q={ciudad}&appid={APIKEY}&units=metric"
    res = requests.get(url).json()
    temp = res['main']['temp']

    return {
        'temp': temp
    }


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ciudad = sys.argv[1]
    tiempo = getTiempo(ciudad)
    print("El tiempo en", ciudad, "es de", tiempo['temp'], "º")
