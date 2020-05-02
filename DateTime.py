import datetime

today = datetime.date.today()

print(today)

birthday = datetime.date(1991, 12, 7)

print(birthday)
days_since_birth = (today - birthday).days
print(days_since_birth)
print(datetime.datetime.now())
print(datetime.datetime.utcnow() + datetime.timedelta(hours=10))