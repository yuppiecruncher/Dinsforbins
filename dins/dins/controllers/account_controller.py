from pyramid.view import view_config
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
def register_get(request):
    return {}

@view_config(route_name='register', renderer='dins:templates/account/register.pt', request_method='POST')
def register_post(request):
    return {}

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

def get_meals():
    titles = meals_services.meal_title()
    desc = meals_services.meal_desc()
    date = meals_services.meal_date()
    return [
        {'name': titles[0], 'description': desc[0], 'date': date[0].strftime("%A, %B, %d"),},
        {'name': titles[1], 'description': desc[1], 'date': date[1].strftime("%A, %B, %d"),},
        {'name': titles[2], 'description': desc[2], 'date': date[2].strftime("%A, %B, %d"),},
    ]
