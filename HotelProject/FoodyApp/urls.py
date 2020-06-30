from django.urls import path
from . import views
from .views import Index, recipes1, contact, about, reserve

urlpatterns=[
    path('', views.Index, name="home"),

    path('contact/', views.contact,name="contact"),

    path('show/',views.showresult,name="showresult"),

    path('recipes/', views.recipes1,name="recipes"),

    path('about/', views.about,name="about"),

    # path('reserve/', views.ReserveForm,name="reserve"),

    # path('showSession', views.showSession, name='showSession'),

    path('signup/',views.signup,name="signup"),

    path('login/',views.login,name="login"),

    # path('acknowledge',views.acknowledge,name="acknowledge"),
    
    path('saved/',views.registered,name="registered"),

    path('register',views.register)

]