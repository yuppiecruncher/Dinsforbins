from pyramid.view import view_config

@view_config(route_name='home', renderer='dins:templates/home/index.pt')
def home_index(request):
    return {'project': 'Dins for Bins'}
