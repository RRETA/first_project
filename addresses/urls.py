from django.urls import path


from .views import GetAddress, CreateAddress,UpdateAddress,DeleteAddress

app_name ='addresses'
urlpatterns =[

path('<int:id>/', GetAddress, name='detail'),
path('create/',CreateAddress.as_view(),name="create"),
path('update/<int:id>/',UpdateAddress.as_view(),name="update"),
path('delete/<int:id>/',DeleteAddress,name="delete"),
]