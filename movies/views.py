from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import views
from .models import Movie
from .forms import MovieForm
# Create your views here.


def GetMovies(request):
    movies = Movie.objects.all()
    #print(movies)
    #return HttpResponse("Funciona") 
    template_name= 'movies/list.html'
    context={
        'movies':movies
    }
    return render(request,template_name,context)

def GetMovie(request,id):
    movie = Movie.objects.get(pk=id)
    template_name='movies/detail.html'
    context={
    'movie' : movie
    }
    return render(request,template_name,context)

class CreateMovie(views.View):
    def get(self,request):
        template_name='movies/form.html'
        return render(request,template_name)
    def post(self,request):
        data = request.POST
        new_movie = Movie.objects.create(
            title = data['title'],
            sinopsis = data['sinopsis'],
            duration = data['duration'],
            calif = data['calif'],
            gender = data['gender']
        )
        if new_movie: 
            print("Pelicula creada con exito")
            return redirect('movies:list')
        else:
            return redirect('movies:create')

        
        
class CreateMovieEasy(views.View):
    def get(self,request):
        form = MovieForm()
        template_name = 'movies/form_easy.html'
        context = {
            'form': form
        }
        return render(request,template_name,context)
    def post(self, request):
        new_form = MovieForm(request.POST)
        if new_form.is_valid():
            new_movie = new_form.save()
            print("Se creo la pelicula correctamente", new_movie)
            return redirect('movies:list')
        else:
            template_name= "movies/form_easy.html"
            context = {
                'form' : new_form

            }
           
            return render(request,template_name,context)

class UpdateMovie(views.View):
    def get(self,request,id):
        movie = Movie.objects.get(pk=id)
        form = MovieForm(instance=movie)
        template_name = 'movies/form_easy.html'
        context = {
                'form' : form,
                'id' : id 
        }
        return render(request,template_name,context)
    
    def post(self,request,id):
        movie = Movie.objects.get(pk=id)
        update_form = MovieForm(request.POST,instance=movie)
        if update_form.is_valid():
            form_updated = update_form.save()
            return redirect('movies:detail',id)
        else:
            template_name = 'movies/form_easy.html'
        context = {
                'form' : form,
                'id' : id 
        }
        return render(request,template_name,context)


def DeleteMovie(request,id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('movies:list')

