users = ['Nished', 'Kedar']
userRole = 'admin'

def validate(role):
    def wrapper_func(input_func):
        def ret_func(name):
            if userRole not in role:
                print('you do not have access to the function')
                return None
            return input_func(name)
        return ret_func
    return wrapper_func

@validate(['admin'])
def create_user(name):
    if name in users:
        print(name, ' => name already exists')
        return
    users.append(name)
    return name

@validate(['admin'])
def delete_user(name):
    users.remove(name)
    return users

@validate(['user', 'admin'])
def view_user(name):
    print(users)


create_user('Nished1')
create_user('Kedar1')
view_user('')