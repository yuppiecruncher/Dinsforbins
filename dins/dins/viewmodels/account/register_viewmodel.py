
from pyramid.request import Request
from dins.viewmodels.shared.viewmodel_base import ViewModelBase

class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.email = self.request_dict.get('email')
        self.name = self.request_dict.get('name', '').strip()
        self.password = self.request_dict.get('password')
        self.role = self.request_dict.get('role')

        if self.email:
            self.email = self.email.strip().lower()

    def validate(self):
        if not self.role:
            self.error = 'You must specify a role.'
        if not self.password:
            self.error = 'You must specify a password.'
        if not self.email:
            self.error = 'You must specify an email address.'
        if not self.name:
            self.error = 'You must specify your name.'
