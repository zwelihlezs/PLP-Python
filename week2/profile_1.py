profile = {'Name': '', 'Surnmane':'', 'Age':'', 'colour': ''}

inp = input('Enter your name: ')
profile['Name'] = inp
inp = input('Enter your surnmane: ')
profile['Surnmane'] = inp
inp = input('Enter your age: ')
profile['Age'] = inp
inp = input('Enter your favourite colour: ')
profile['colour'] = inp


print('\n\n')
print(f'Name: {profile.get('Name')}')
print(f'Surname: {profile.get('Surname')}')
print(f'Age: {profile.get('Age')}')
print(f'favourite colour: {profile.get('colour')}')