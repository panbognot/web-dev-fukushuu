while True:
    print('Who are you?')
    name = input()
    if name != 'Rad':
        continue
    print('Hello, Rad. What is the password? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
