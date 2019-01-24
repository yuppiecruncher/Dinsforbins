import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import user_services
from dins.data_services import meals_services
from dins.infrastructure import cookie_auth
from dins.infrastructure import request_dict
from dins.viewmodels.account.account_home_viewmodel import AccountHomeViewModel

################ REGISTRATION ################

@view_config(route_name='register', renderer='dins:templates/account/register.pt', request_method='GET')
def register_get(request):
    return {
        'email': None,
        'name': None,
        'password': None,
        'role': None,
        'error' : None,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)

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
            'error': 'Some required fields are missing.',
            'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
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
def login_get(request):
    return {
        'email': None,
        'password': None,
        'error' : None,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }

@view_config(route_name='login', renderer='dins:templates/account/login.pt', request_method='POST')
def login_post(request):
    data = request_dict.create(request)
    email = data.email
    password = data.password
    user = user_services.login_user(email, password)

    if not user:
        return {
            'email': email,
            'password': password,
            'error': 'The user could not be found or the password is incorrect.',
            'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
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

################ ACCOUNT_REDIRECT ################

@view_config(route_name='account_home')
def account_redirect(request):
    vm = AccountHomeViewModel(request)

    if 'Chef' in vm.user.role:
        return x.HTTPFound('/chef')
    elif 'Analyst' in vm.user.role:
        return x.HTTPFound('/analyst')
    elif 'Diner' in vm.user.role:
        return x.HTTPFound('/diner')

################ ROLES ################

@view_config(route_name='diner', renderer='dins:templates/roles/diner.pt')
def diner_page(request):
    vm = AccountHomeViewModel(request)
    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Chef' in vm.user.role:
        return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
        return x.HTTPUnauthorized()
    return {
        'user': vm.user,
        'titles': meals_services.get_meals(),
        'user_id': vm.user.id
    }

@view_config(route_name='analyst', renderer='dins:templates/roles/analyst.pt')
def analyst_page(request):
    vm = AccountHomeViewModel(request)
    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Chef' in vm.user.role:
            return x.HTTPUnauthorized()
    if 'Diner' in vm.user.role:
            return x.HTTPUnauthorized()
    return {
        'user': vm.user,
        'titles': meals_services.get_meals(),
        'user_id': vm.user.id

    }

@view_config(route_name='chef', renderer='dins:templates/roles/chef.pt')
def chef_page(request):
    vm = AccountHomeViewModel(request)
    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Diner' in vm.user.role:
            return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
            return x.HTTPUnauthorized()
    return {
        'user': vm.user,
        'titles': meals_services.get_meals(),
        'user_id': vm.user.id
    }

################ ABOUT ################

@view_config(route_name='about', renderer='dins:templates/home/about.pt')
def about_page(request):

    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
