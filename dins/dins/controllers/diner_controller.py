from pyramid.view import view_config

@view_config(route_name='diner', renderer='dins:templates/roles/diner.pt')
def diner_page(request):
    return {
        'meals': get_meal_options()
    }

def get_meal_options():
    return [
        {'name': 'Steak and Broccoli', 'date': 'Jan 3rd'},
        {'name': 'Asian Chopped Salad', 'date': 'Jan 4th'},
        {'name': 'Pot Roast with potatoes', 'date': None},
    ]
