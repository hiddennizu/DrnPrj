from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from . import forms


# Create your views here.


def user_login(request):
    if request.user.is_authenticated():
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = forms.LoginForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'welcome %s !' % user)
                return redirect('accounts:dashboard')

            else:
                messages.error(request, 'Disabled account')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Invalid login')
            return redirect('accounts:login')

    else:
        form = forms.LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:home')


def user_register(request):
    if request.method == 'POST':
        user_form = forms.RegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # profile = Profile.objects.create(user=new_user)
            login(request, new_user)
            messages.success(request, "welcome %s" % new_user)
            return redirect('accounts:dashboard')
            # pass context new user here
    else:
        user_form = forms.RegisterForm()

    context = {'user_form': user_form, }
    return render(request, 'accounts/register.html', context)


@staff_member_required
def mod_register(request):
    if request.method == 'POST':
        user_form = forms.RegisterForm(request.POST)

        if user_form.is_valid():
            new_staff = user_form.save(commit=False)
            new_staff.set_password(user_form.cleaned_data['password'])
            new_staff.is_staff = True
            new_staff.save()
            # profile = Profile.objects.create(user=new_user)
            login(request, new_staff)
            messages.success(request, "welcome %s" % new_staff)
            return redirect('accounts:dashboard')
            # pass context new user here
    else:
        user_form = forms.RegisterForm()

    context = {'user_form': user_form, }
    return render(request, 'accounts/register.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, username):
    user = get_object_or_404(User, username=username)
    form = forms.ProfileForm(instance=user, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "user updated.")
            return redirect('users')

    context = {
        'form': form
    }

    return render(request, 'account/profile.html', context)


@staff_member_required
def user_list(request):
    users = User.objects.all().order_by('username')
    context = {
        'users': users,

    }
    return render(request, 'accounts/user_list.html', context)


@staff_member_required
def users_delete(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect('accounts:user_list')


@login_required
def chage_password(request):
    passform = forms.password_change_form(data=request.POST or None, user=request.user)
    if request.method == 'POST':
        if passform.is_valid():
            user = passform.save()
            messages.success(request, 'password changed')
            login(request, user)

    context = {
        'passform': passform
    }
    return render(request, 'accounts/password_change.html', context)


def home(request):
    if request.user.is_authenticated():
        return redirect('accounts:dashboard')
    return render(request, 'base.html')


@login_required
def dashboard(request):
    return render(request, 'home/index.html')
