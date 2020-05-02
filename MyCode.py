data = [2, 3, 5, 6, 7, 8]

# du_list = [i * 2 for i in data if i in data]

# print(du_list)


data.extend(([8, 6, 8, 9, 10]))
del(data[0])
print(data)

d = {'name': 'Nitesh'}

for k, v in d.items():
    print(k, v)
del(d['name'])
print(d)

name = 'Nitesh'
age = 29
state = 'Bihar'

print('I am {} , I am {} years old and I am from {}.'.format(name, age, state))

