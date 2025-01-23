user_seconds = int(input("Введите количество секунд: "))

hours = str("{:02}".format(user_seconds // 3600))
minutes = str("{:02}".format(user_seconds // 60 % 60))
seconds = str("{:02}".format(user_seconds % 60))

print(hours + ":" + minutes + ":" + seconds)
print(f"{hours}:{minutes}:{seconds}")


