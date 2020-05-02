list1 = [1, 2, 3, 4, 5, 6]
list2 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

zipped = list(zip(list1, list2))

print(zipped)

unzipped = list(zip(*zipped));

print(unzipped)

items = ['Apple', 'Banana', 'Orange']
counts = [3, 6, 7]
prices = [0.89, 0.25, 0.55]

serntences = []

for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = 'I bought ' + count + ' ' + item + 's at ' + price + ' cents each.'
    serntences.append(sentence)

print(serntences)
