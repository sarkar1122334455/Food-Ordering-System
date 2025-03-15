from django.urls import path
from . import views
urlpatterns=[
    path('burger',views.burger),
    path('book',views.book),
    path('menu',views.menu),
    path('about',views.about),
    path('login',views.login),
    path('registration',views.registration),
    path('log',views.log),
    path('reg',views.reg),
    path('show',views.show),
    path('edit',views.edit),
    path('del/<int:id>', views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    path('logout',views.logout),
    path('ind',views.ind),
    
]