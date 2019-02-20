import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import user_services
from dins.infrastructure import cookie_auth
from dins.infrastructure import request_dict
from dins.viewmodels.account.account_home_viewmodel import AccountHomeViewModel
from dins.viewmodels.account.register_viewmodel import RegisterViewModel
from dins.viewmodels.account.login_viewmodel import LoginViewModel

################ REGISTRATION ################

@view_config(route_name='register', renderer='dins:templates/account/register.pt', request_method='GET')
def register_get(request):
    vm = RegisterViewModel(request)
    return vm.to_dict()

@view_config(route_name='register', renderer='dins:templates/account/register.pt', request_method='POST')
def register_post(request):
    vm = RegisterViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    # create user
    user = user_services.create_user(vm.email, vm.name, vm.password, vm.role)
    #set cookie for new user
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
    vm = LoginViewModel(request)
    return vm.to_dict()

@view_config(route_name='login', renderer='dins:templates/account/login.pt', request_method='POST')
def login_post(request):
    vm = LoginViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    # create cookie session
    cookie_auth.set_auth(request, vm.user.id)

    if 'Chef' in vm.user.role:
        return x.HTTPFound('/chef')
    elif 'Analyst' in vm.user.role:
        return x.HTTPFound('/analyst')
    elif 'Diner' in vm.user.role:
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

################ ABOUT ################

@view_config(route_name='about', renderer='dins:templates/home/about.pt')
def about_page(request):

    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
