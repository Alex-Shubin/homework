"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""
from pyowm import OWM
from pprint import pprint

owm = OWM('f23199e2033f9af89297e10d7cec508d')
mgr = owm.weather_manager()

user_city = input("Введите город: ")
# user_city = 'Минск'
obs = mgr.weather_at_place(user_city)

w = obs.weather

print(dir(w))
print(f"""{user_city} погода сейчас:
      На небе: {w.detailed_status}
      Температура: {w.temperature('celsius').get('temp')}
      Ощущается как: {w.temperature('celsius').get('feels_like')}
      Скорость ветра: {w.wind().get('speed')}
      Влажность: {w.humidity}%
      Осадки: {w.rain}{w.snow}
      """)