import pyramid.httpexceptions as x
from pyramid.view import view_config
from dins.data_services import email_service
from dins.infrastructure import request_dict
from dins.viewmodels.account.analyst_form_viewmodel import AnalystFormViewModel

@view_config(route_name='analyst', renderer='dins:templates/roles/analyst.pt')
def analyst_page(request):
    vm = AnalystFormViewModel(request)
    return vm.to_dict()

    if not vm.user:
        return x.HTTPFound('/account/login')
    if 'Chef' in vm.user.role:
            return x.HTTPUnauthorized()
    if 'Diner' in vm.user.role:
            return x.HTTPUnauthorized()
