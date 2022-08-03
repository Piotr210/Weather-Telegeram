import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }


    try:
        wr = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={open_weather_token}"
        )
        datka = wr.json()
        # pprint(datka)
        lat = datka[0]["lat"]
        lon = datka[0]["lon"]
        # print(lat,'- широта')
        # print(lon,'- долгота')
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Более подробный прогноз погоды смотри в интернете!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nВетер: {wind}м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def prob(city):
    counter = True
    # city = main()
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        if i in city:
            counter = False
            break

    while True:
        if counter == False:
            print("Вы ввели название города с использованем английских букв, введите название заново")
            city = main()
            break
        else:
            if city.istitle():
                print("Всё верно")
                get_weather(city, open_weather_token)
                break
            else:
                print("Вы ввели город с маленькой буквы, введите название заново")
                city = main()
                break

def main():
    city = input("Введите название города: ")
    prob(city)
    # get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
