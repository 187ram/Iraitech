from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
  
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username} !')
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, user)
            return redirect('home')
    context = { 'form' : form}
    return render(request,'accounts/register.html', context)




@login_required
def profile(request):
    if request.method == 'POST':
        userupdateform = UserUpdateForm(request.POST, instance = request.user)
        profileupdateform = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        
        if userupdateform.is_valid() and profileupdateform.is_valid():
            userupdateform.save()
            profileupdateform.save()
            messages.success(request, f'Your Profile is updated!')
            return redirect('profile')
    else:
        userupdateform = UserUpdateForm(instance = request.user)
        profileupdateform = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'userupdateform' : userupdateform,
        'profileupdateform' : profileupdateform
    }
    return render(request,'accounts/profile.html', context)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context
