from .forms import UserLoginForm, UserRegistrationForm

def get_login_form(request):
    login_form = UserLoginForm
    return {'login_form':login_form}
    
def get_registration_form(request):
    reg_form = UserRegistrationForm
    return {'reg_form':reg_form}
    