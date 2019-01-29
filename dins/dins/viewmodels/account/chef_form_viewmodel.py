
from pyramid.request import Request
from dins.viewmodels.shared.viewmodel_base import ViewModelBase
from dins.data_services import user_services
from dins.data_services import meals_services

class ChefFormViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.title = self.request_dict.get('title')
        self.menudescription = self.request_dict.get('itemdescription')
        self.available = self.request_dict.get('available')
        self.user = user_services.find_user_by_id(self.user_id)
        self.titles = meals_services.get_meals()

    def validate(self):
        if not self.available:
            self.error = 'You must specify an availability date.'
        if not self.menudescription:
            self.error = 'You must provide a description.'
        if not self.title:
            self.error = 'You must provide a title for this meal.'
