from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # request.post is the post data
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,  # display file data coming in with the request(image the user uploads)
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():  # check whether the form data are valid(the user and the profile)
            u_form.save()
            p_form.save()  # save the data if there valid(save the user and profile forms)
            messages.success(request, f'Your account has been updated!')  # send a success message if the forms are valid
            return redirect('profile')  # the page doesnt get a post-get reload

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form}

    return render(request, 'users/profile.html', context)

    # message types: messages.debug, messages.warning, messages.error, messages,success, messages.info