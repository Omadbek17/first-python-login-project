users = [
    {
        'username': 'bek06',
        'password': 'omad2006'
    },
    {
        'username': 'user1',
        'password': 'abcd77'
    }
]

def get_user_by_username(username):
    for user in users:
        if user['username'] == username:
            return user
    return None

def login():
    username = input('Enter your Username: ')
    password = input('Enter your Password: ')
    user = get_user_by_username(username)
    if not user:
        print('Invalid Username')
    else:
        if user ['password'] == password:
            print('Logged In')
        else: print('Invalid Password')


if __name__ == '__main__':
    login()