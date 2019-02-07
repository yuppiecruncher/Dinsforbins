
from pyramid.request import Request
from dins.viewmodels.shared.viewmodel_base import ViewModelBase
from dins.data_services import user_services
from dins.data_services import diner_services

class DinerFormViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        #### GLOBAL ####
        self.user = user_services.find_user_by_id(self.user_id)

        #### WEEKLY MEAL CALENDAR####
        self.today = diner_services.query_today(self.user_id)
        self.tp1 = diner_services.query_tp1(self.user_id)
        self.tp2 = diner_services.query_tp2(self.user_id)
        self.tp3 = diner_services.query_tp3(self.user_id)
        self.tp4 = diner_services.query_tp4(self.user_id)
        self.tp5 = diner_services.query_tp5(self.user_id)
        self.tp6 = diner_services.query_tp6(self.user_id)
