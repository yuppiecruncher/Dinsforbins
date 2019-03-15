from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request
from dins.data_services import diner_services
from dins.viewmodels.account.diner_form_viewmodel import DinerFormViewModel


@view_config(route_name='api_diner_get',
                renderer='json',
                request_method='GET')
def diner_get(request):
    vm = DinerFormViewModel(request)
    uid = request.matchdict.get('uid')

    all_meals = diner_services.query(uid)
    assigned_chef = diner_services.find_chef(uid)
    diner_preferences =diner_services.diner_preferences(uid)

    if not all_meals:
        msg = "Could not load any meals for user id '{}'. There may be no meals to display.".format(uid)
        return Response(status=404, json_body={'error': msg})

    return all_meals, assigned_chef, diner_preferences
