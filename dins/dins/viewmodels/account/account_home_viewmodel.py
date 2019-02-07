
from pyramid.request import Request
from dins.viewmodels.shared.viewmodel_base import ViewModelBase
from dins.data_services import user_services

class AccountHomeViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.user = user_services.find_user_by_id(self.user_id)
