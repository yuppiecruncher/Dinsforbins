import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import user_services
from dins.data_services import meals_services
from dins.infrastructure import cookie_auth

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
    cookie_auth.set_auth(request, user.id)

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
    cookie_auth.set_auth(request, user.id)

    if 'Chef' in user.role:
        return x.HTTPFound('/chef')
    elif 'Analyst' in user.role:
        return x.HTTPFound('/analyst')
    elif 'Diner' in user.role:
        return x.HTTPFound('/diner')

################ LOGOUT ################

@view_config(route_name='logout')
def logout(request):
    cookie_auth.logout(request)

    return x.HTTPFound('/')

################ ROLES ################

@view_config(route_name='diner', renderer='dins:templates/roles/diner.pt')
def diner_page(request):
    user_id = cookie_auth.get_user_id_via_auth_cookie(request)
    user = user_services.find_user_by_id(user_id)
    if not user:
        return x.HTTPFound('/account/login')
    return {
        'user': user,
        'titles': get_meals()
    }

@view_config(route_name='analyst', renderer='dins:templates/roles/analyst.pt')
def analyst_page(request):
    user_id = cookie_auth.get_user_id_via_auth_cookie(request)
    user = user_services.find_user_by_id(user_id)
    if not user:
        return x.HTTPFound('/account/login')
    return {
        'user': user,
        'titles': get_meals()
    }

@view_config(route_name='chef', renderer='dins:templates/roles/chef.pt')
def chef_page(request):
    user_id = cookie_auth.get_user_id_via_auth_cookie(request)
    user = user_services.find_user_by_id(user_id)
    if not user:
        return x.HTTPFound('/account/login')
    return {
        'user': user,
        'titles': get_meals()
    }

def get_meals():
    titles = meals_services.meal_title()
    desc = meals_services.meal_desc()
    date = meals_services.meal_date()
    return [
        {'name': titles[0], 'description': desc[0], 'date': date[0].strftime("%A, %B, %d"),},
        {'name': titles[1], 'description': desc[1], 'date': date[1].strftime("%A, %B, %d"),},
        {'name': titles[2], 'description': desc[2], 'date': date[2].strftime("%A, %B, %d"),},
    ]

################ about ################

@view_config(route_name='about', renderer='dins:templates/home/about.pt')
def about_page(_):

    return {}
