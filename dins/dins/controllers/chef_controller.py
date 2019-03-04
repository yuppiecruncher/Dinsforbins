import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import chef_services
from dins.data_services import email_service
from dins.infrastructure import request_dict
from dins.viewmodels.account.chef_form_viewmodel import ChefFormViewModel

@view_config(route_name='chef', renderer='dins:templates/roles/chef.pt', request_method="GET")
def chef_get(request):
    vm = ChefFormViewModel(request)
    return vm.to_dict()

    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Diner' in vm.user.role:
        return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
        return x.HTTPUnauthorized()

        # remove all references to other pages.

@view_config(route_name='chef_add', renderer='dins:templates/roles/chef_add.pt', request_method="GET")
def chef_add_get(request):
    vm = ChefFormViewModel(request)
    return vm.to_dict()

    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Diner' in vm.user.role:
        return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
        return x.HTTPUnauthorized()

@view_config(route_name='chef_add', renderer='dins:templates/roles/chef_add.pt', request_method='POST')
def chef__add_post(request):
    vm = ChefFormViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    #create meal
    chef_services.create_meal(vm.title, vm.menudescription, vm.available, vm.user_id, vm.diner_email)

    return x.HTTPFound('/chef/add')

@view_config(route_name='chef_diners', renderer='dins:templates/roles/chef_diners.pt', request_method="GET")
def chef_diners_get(request):
    vm = ChefFormViewModel(request)
    return vm.to_dict()

    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Diner' in vm.user.role:
        return x.HTTPUnauthorized()
    if 'Analyst' in vm.user.role:
        return x.HTTPUnauthorized()

@view_config(route_name='chef_diners', renderer='dins:templates/roles/chef_diners.pt', request_method='POST')
def chef__diners_post(request):
    vm = ChefFormViewModel(request)
    vm.assign_diner_validate()
    if vm.error:
        return vm.to_dict()

    #create meal
    chef_services.assigned_diner(vm.user_id, vm.diner_email)

    return x.HTTPFound('/chef/diners')
