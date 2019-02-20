import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import diner_services
from dins.data_services import email_service
from dins.infrastructure import request_dict
from dins.viewmodels.account.diner_form_viewmodel import DinerFormViewModel

################ ROLES ################

@view_config(route_name='diner', renderer='dins:templates/roles/diner.pt')
def diner_page(request):
    vm = DinerFormViewModel(request)
    return vm.to_dict()

    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Chef' in vm.user.role:
        return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
        return x.HTTPUnauthorized()

@view_config(route_name='diner_request', renderer='dins:templates/roles/diner_request.pt', request_method="GET")
def diner_request_get(request):
    vm = DinerFormViewModel(request)
    return vm.to_dict()

    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Diner' in vm.user.role:
        return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
        return x.HTTPUnauthorized()

@view_config(route_name='diner_request', renderer='dins:templates/roles/diner_request.pt', request_method='POST')
def diner_request_post(request):
    vm = DinerFormViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    #request meal
    diner_services.request_meal(vm.title, vm.menudescription, vm.available, vm.user_id, vm.chef_email)

    return x.HTTPFound('/diner/request')
