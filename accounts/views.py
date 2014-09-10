from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from accounts.forms import UserForm, UserProfileForm, LoginForm
# Create your views here.
from accounts.models import UserProfile
from django.forms.util import ErrorList, ErrorDict


def register(request):
    # gets request context
    context = RequestContext(request)

    # boolean value for code to see if registering was successful
    registered = False

    # checks if the HTTP is a post, so then we can process form data
    if (request.method == 'POST'):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # check if forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # saves new user
            user = user_form.save()

            # hash password
            user.set_password(user.password)
            user.save()
            # sort user profile commit=False avoids integrity problems
            profile = profile_form.save(commit=False)
            profile.user = user;
            profile.save()

            registered = True;
        else:
            # errors for invalid forms or mistakes
            # print user_form._errors, profile_form._errors
            pass
    # not a post method, unbinds user and profile forms
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    template = 'accounts/register.html'
    return render_to_response(template,
                              {'user_form': user_form,
                               'profile_form': profile_form,
                               'registered': registered},
                              context)

def user_login(request):
    context = RequestContext(request)
    successfull = False
    # if http is post take form data and login
    if request.method == 'POST':
        # get form data
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            ra = request.POST['ra']
            password = request.POST['password']
            user = None
            flag = False
            try:
                username = UserProfile.objects.get(ra=ra).user.username
                user = authenticate(username=username, password=password)
            except UserProfile.DoesNotExist:
                login_form._errors['inexistente'] = login_form.error_class([u'Ra inexistente'])
                flag = True
            finally:
                # pass into django authentication
                # if returned object from authenticate is not none (found the user)
                if user:
                    #checks if account was disabled
                    if user.is_active:
                        login(request, user)
                        # log the user in and successfull is set
                        successfull = True
                    else:
                        # error messages for the form
                        login_form._errors['desabilidata'] = login_form.error_class([u'Sua conta foi desabilitada, entre com contato '
                                                             u'com o administrador'])
                elif not flag:
                    # error messages for the form
                    login_form._errors['invalidos'] = login_form.error_class([u'Login ou senha invalidos'])

        else:
            # errors on the form validation
            pass
    else:
        # generates a blank unbound form
        login_form = LoginForm()
    template = 'accounts/login.html'
    return render_to_response(template, {'login_form': login_form,
                                         'successfull': successfull}, context)



