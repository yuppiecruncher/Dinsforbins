
from pyramid.request import Request
from dins.viewmodels.shared.viewmodel_base import ViewModelBase
from dins.data_services import user_services
from dins.data_services import chef_services

class ChefFormViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        #### GLOBAL ####
        self.user = user_services.find_user_by_id(self.user_id)

        #### WEEKLY MEAL CALENDAR####
        self.today = chef_services.query_today(self.user_id)
        self.tp1 = chef_services.query_tp1(self.user_id)
        self.tp2 = chef_services.query_tp2(self.user_id)
        self.tp3 = chef_services.query_tp3(self.user_id)
        self.tp4 = chef_services.query_tp4(self.user_id)
        self.tp5 = chef_services.query_tp5(self.user_id)
        self.tp6 = chef_services.query_tp6(self.user_id)

        #### ASSIGNED DINER DISPLAY ####
        self.dinerlist = chef_services.query_assigned_diner(self.user_id)

        #### FORM INPUTS ############
        self.title = self.request_dict.get('title')
        self.menudescription = self.request_dict.get('itemdescription')
        self.diner_email = self.request_dict.get('diner_email')
        self.available = self.request_dict.get('available')

        #### ERROR HANDLING ####
    def validate(self):
        if not self.diner_email:
            self.error = 'Check your diners information and try again.'
        if not self.available:
            self.error = 'You must specify an availability date.'
        if not self.menudescription:
            self.error = 'You must provide a description.'
        if not self.title:
            self.error = 'You must provide a title for this meal.'

    def assign_diner_validate(self):
        if not self.diner_email:
            self.error = 'Check your diners information and try again.'
