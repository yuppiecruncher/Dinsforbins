import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import user_services
from dins.data_services import meals_services

################ LOGIN ################

@view_config(route_name='account_home', renderer='dins:templates/account/login.pt', request_method='GET')
def login_get(request):
    return {}

@view_config(route_name='account_home', renderer='dins:templates/account/login.pt', request_method='POST')
def login_post(request):
    return {}

################ REGISTRATION ################

@view_config(route_name='register', renderer='dins:templates/account/register.pt', request_method='GET')
def register_get(_):
    return {
        'email': None,
        'name': None,
        'password': None,
        'role': None,
        'error' : None
    }

@view_config(route_name='register', renderer='dins:templates/account/register.pt', request_method='POST')
def register_post(request):

    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')
    role = request.POST.get('role')

    if not email or not name or not password or not role:
        return {
            'email': email,
            'name': name,
            'password': password,
            'role': role,
            'error': 'Some required fields are missing.'
        }
    # create user
    user = user_services.create_user(email, name, password, role)
    
    if 'Chef' in user.role:
        return x.HTTPFound('/chef')
    elif 'Analyst' in user.role:
        return x.HTTPFound('/analyst')
    elif 'Diner' in user.role:
        return x.HTTPFound('/diner')

################ LOGIN ################

@view_config(route_name='login', renderer='dins:templates/account/login.pt', request_method='GET')
def login_get(_):
    return {
        'email': None,
        'password': None,
        'error' : None
    }

@view_config(route_name='login', renderer='dins:templates/account/login.pt', request_method='POST')
def login_post(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = user_services.login_user(email, password)

    if not user:
        return {
            'email': email,
            'password': password,
            'error': 'The user could not be found or the password is incorrect.'
        }
    # create cookie session
    if 'Chef' in user.role:
        return x.HTTPFound('/chef')
    elif 'Analyst' in user.role:
        return x.HTTPFound('/analyst')
    elif 'Diner' in user.role:
        return x.HTTPFound('/diner')

################ LOGOUT ################

@view_config(route_name='logout')
def logout(request):
    return {}

################ ROLES ################

@view_config(route_name='diner', renderer='dins:templates/roles/diner.pt')
def diner_page(request):
    return {
        'titles': get_meals()
    }

#note for future: if table meals_services has no data, page will crash.
#Need some placeholder to display until chef puts data in
def get_meals():
    titles = meals_services.meal_title()
    desc = meals_services.meal_desc()
    date = meals_services.meal_date()
    return [
        {'name': titles[0], 'description': desc[0], 'date': date[0].strftime("%A, %B, %d"),},
        {'name': titles[1], 'description': desc[1], 'date': date[1].strftime("%A, %B, %d"),},
        {'name': titles[2], 'description': desc[2], 'date': date[2].strftime("%A, %B, %d"),},
    ]
