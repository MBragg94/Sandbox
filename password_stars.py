

user_attempt = input('Enter your password: ')
while len(user_attempt) != 10:
    print('Password must be at least 10 characters long')
    user_attempt = input('Enter your password: ')
for i in range(len(user_attempt)):
    print("*", end=" ")
