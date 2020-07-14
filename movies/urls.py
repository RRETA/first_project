from django.urls import path
from .views import GetMovies,GetMovie,CreateMovie,CreateMovieEasy,UpdateMovie,DeleteMovie
app_name='movies'
urlpatterns = [
    path('',GetMovies, name="list"),
    path('<int:id>',GetMovie,name="detail"),
    path('create/',CreateMovieEasy.as_view(),name="create"),
    path('update/<int:id>/',UpdateMovie.as_view(),name="update"),
    path('delete/<int:id>/',DeleteMovie,name ="delete")
    
]

