from django.shortcuts import render, render_to_response
from django.template import RequestContext
from accounts.forms import UserForm, UserProfileForm
# Create your views here.

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
            print user_form.errors, profile_form.errors
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
