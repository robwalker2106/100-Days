
names = []
letter = ""

with open('./Input/Names/invited_names.txt') as file:
    data_line = file.readlines()

    for name in data_line:
        names.append(name[:-1])

with open('./Input/Letters/starting_letter.txt') as data:
    letter = data.read()

for person in names:
    name = person
    new_letter = letter.replace('[name]', name)
    with open('./Output/ReadyToSend/' + name + '.txt', 'w') as data:
        data.write(new_letter)



