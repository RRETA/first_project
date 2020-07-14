from django.shortcuts import render
from django.contrib.auth.models import User

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
    template_name='users/detail.html'
    context={
    'user' : user
    }
    return render(request,template_name,context)

        
        
class CreateMovieUser(views.View):
    def get(self,request):
        form = UserForm()
        template_name = 'users/form_easy.html'
        context = {
            'form': form
        }
        return render(request,template_name,context)
    def post(self, request):
        new_form = UserForm(request.POST)
        if new_form.is_valid():
            new_user = new_form.save()
            print("Se creo el usuario correctamente", new_user)
            return redirect('users:list')
        else:
            template_name= "users/form_easy.html"
            context = {
                'form' : new_form

            }
           
            return render(request,template_name,context)

class UpdateUser(views.View):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        form = MovieForm(instance=user)
        template_name = 'users/form_easy.html'
        context = {
                'form' : form,
                'id' : id 
        }
        return render(request,template_name,context)
    
    def post(self,request,id):
        user = User.objects.get(pk=id)
        update_form = UserForm(request.POST,instance=user)
        if update_form.is_valid():
            form_updated = update_form.save()
            return redirect('users:detail',id)
        else:
            template_name = 'users/form_easy.html'
        context = {
                'form' : form,
                'id' : id 
        }
        return render(request,template_name,context)


def DeleteUser(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('users:list')
