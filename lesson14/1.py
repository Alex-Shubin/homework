"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import random
import string
import re
from datetime import date, timedelta, datetime

class User:
    
	def __init__(self, name:str, login:str, password=""):
		self.validate_name(name)
		self.validate_login(login)
		self.validate_password(password)

		self.name = name
		self.login = login
		self.is_blocked = False

		# 30 дневная подписка, если дата подписки не передавалась
		self.subscription_date = date.today() + timedelta(days=30)

		# видп подписки - free или paid
		self.subscription_mode = "free"

	# проверка имени
	def validate_name(self, name):
		if not name:
			raise ValueError("Имя не может быть пустым")
		
		if not re.match("^[а-яА-Я]{2,}$", name):
			raise ValueError("Имя может содержать только символы русского алфавита", \
					"и не может быть меньше 2 символов")

	# проверка логина
	def validate_login(self, login):
		if not login:
			raise ValueError("Логин не может быть пустым")
		
		if not re.match("^[a-zA-Z0-9_]{6,}$", login):
			raise ValueError("Логин может содержать только англ буквы, цифры и _,"
					"и не может быть менее 6 символов")
		
	# проверка пароля на валидность
	def validate_password(self, password):
		if password:
			if not re.match(
					r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9]{6,}$", 
					password):
				raise ValueError("""
Пароль должен содержать минимум 1 строчную,1 заглавную и 1 цифру
Пароль может содержать только англ буквы и цифры, и не может быть менее 6 символов
					 """)
			else:
				self.password = password
		else:
			self.password = self.gen_password()
			print(f"Ваш новый пароль: {self.password}")

	def bloc(self, blocked=False):
		if blocked:
			if self.is_blocked:
				raise ValueError("Пользователь уже заблокирован")
			else:
				self.is_blocked = True
				print("Пользователь успешно заблокирован")
		else:
			if not self.is_blocked:
				raise ValueError("Пользователь уже разблокирован")
			else:
				self.is_blocked = False
				print("Пользователь успешно разблокирован")

	def gen_password(self, length=8):
		# используемые символы
		chars = string.ascii_letters + string.digits
		# требование: 1 стр, 1 проп, 1 цифра
		password = [random.choice(string.ascii_lowercase),
			  		random.choice(string.ascii_uppercase),
					random.choice(string.digits)]
		
		# заполняем до нужной длины
		for _ in range(length - 3):
			password.append(random.choice(chars))

		# перемешиваем символы в строке
		random.shuffle(password)

		# преобразуем в строку и возвращаем
		return ''.join(password)
	
	def change_pass(self, password=''):
		self.validate_password(password)

	def check_subscr(self, some_date=None):
		if some_date is None:
			some_date = date.today()
		else:
			try:
				some_date = datetime.strptime(some_date, '%Y-%m-%d').date()
			except ValueError:
				raise ValueError("Некорректный формат даты. Используйте YYYY-MM-DD")
			
		if some_date <= self.subscription_date:
			days_left = (self.subscription_date - some_date).days
			return {
				'active': not(self.is_blocked),
				'mode': self.subscription_mode,
				'days_left': days_left
			}
		else:
			return{
				'active': not(self.is_blocked),
				'mode': None,
				'days_left': None
			}
		
	def update_subscription(self, new_date=None):
		if new_date is None: # если даты нет - то + 30 дней платной подписки
			self.subscription_date = date.today() + timedelta(days=30)
			self.subscription_mode = "paid"
		else:
			try:
				new_date = datetime.strptime(new_date, '%Y-%m-%d').date()
				self.subscription_date = new_date
				self.subscription_mode = "paid"
			except ValueError:
				raise ValueError("Некорректный формат даты. Используйте YYYY-MM-DD")
		
	def get_info(self):
		if self.is_blocked:
			print(f"Пользователь {self.name} ({self.login}) заблокирован")
		else:
			print(f"Имя: {self.name}")
			print(f"Логин: {self.login}")
			print(f"Статус подписки: {self.subscription_mode}")
			print(f"Дата окончания подписки: {self.subscription_date}")
			print(f"Пароль: {self.password}")

# Создали пользователя
user1 = User("Иван", "ivan123")
print(user1.check_subscr())

# Сменили дату окончания и тип подписки
user1.update_subscription("2025-04-04")
print(user1.check_subscr())

# Заблокировали
user1.bloc(True)
print(user1.check_subscr())

# Сменили пароль
user1.change_pass("12vS3456")
print(user1.password)

# получили инфу
user1.get_info()

# Разблокировали и еще раз получили инфу)
user1.bloc()
user1.get_info()