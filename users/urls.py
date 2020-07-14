from django.urls import path
from .views import GetUsers,GetUser,CreateUser,UpdateUser,DeleteUser
app_name='movies'

app_name='users'
urlpatterns = [
    path('', GetUsers, name='list'),
    path('<int:id>',GetUser,name="detail"),
    path('create/',CreateUser.as_view(),name="create"),
    path('update/<int:id>/',UpdateUser.as_view(),name="update"),
    path('delete/<int:id>/',DeleteUser,name ="delete")
]