from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm, UserCreateForm, UserUpdateForm
from django import views
from django.contrib import messages

# Create your views here.

def GetUsers(request):
    users = User.objects.filter(is_superuser=False)
    template_name="users/list.html"
    context = {
        'users' : users
    }
    return render(request,template_name,context)


def GetUser(request,id):
    user = User.objects.get(pk=id)
    print(user.profile.image)
    template_name='users/detail.html'
    context={
    'user' : user
    }
    return render(request,template_name,context)


        
        
class CreateUser(views.View):
    def get(self,request):
        user_form = UserForm()
        profile_form = ProfileForm()
        template_name = 'users/form.html'
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request,template_name,context)
    def post(self, request):
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,'Usuario creado con exito ')
            return redirect('users:detail', user.id)
        else:
            template_name= "users/form.html"
            context = {
                'user_form' : new_form,
                'profile_form' : profile_form
            }
            messages.error(request,'Algo fallo al crear el usuario')
            return render(request,template_name,context)

class UpdateUser(views.View):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
        template_name = 'users/form.html'
        context = {
                'user_form' : user_form,
                'profile_form': profile_form,
                'id' : id,
                'image' : user.profile.image
        }
        messages.success(request,'Usuario actualizado con exito ')
        return render(request,template_name,context)
    
    def post(self,request,id):
        user = User.objects.get(pk=id)
        user_form = UserUpdateForm(request.POST,instance=user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            return redirect('users:detail',id)
        else:
            template_name = 'user_form.html'
        context = {
                'user_form' : user_form,
                'profile_form' : profile_form,
                'id' : id,
                'image': user.profile.image
        }
        messages.error(request,'Algo fallo al actualizar el usuario')
        return render(request,template_name,context)


def DeleteUser(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.info(request,'Se elimino usuario')
    return redirect('users:list')
