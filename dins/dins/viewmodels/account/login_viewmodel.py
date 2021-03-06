
from pyramid.request import Request
from dins.viewmodels.shared.viewmodel_base import ViewModelBase
from dins.data_services import user_services

class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.email = self.request_dict.get('email')
        self.password = self.request_dict.get('password')
        self.user = None

        if self.email:
            self.email = self.email.strip().lower()

        if self.email and self.password:
            self.user = user_services.login_user(self.email, self.password)

    def validate(self):
        if not self.user:
            self.error = 'The user could not found or the password is incorrect.'
        if not self.password:
            self.error = 'You must specify a password.'
        if not self.email:
            self.error = 'You must specify an email address.'
