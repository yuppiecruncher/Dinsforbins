from pyramid.view import view_config
from dins.infrastructure import cookie_auth
from dins.viewmodels.account.account_home_viewmodel import AccountHomeViewModel


@view_config(route_name='index', renderer='dins:templates/home/index.pt')
def home_index(request):
    vm = AccountHomeViewModel(request)

    return {
        'project': 'Dins for Bins',
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
