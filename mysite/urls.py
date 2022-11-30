from unicodedata import name
from django.contrib import admin
from django.urls import path,include

# from accounts import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('accounts.urls')),
    # path('',views.home,name='home'),
    # path('signup/',views.signup,name='signup'),
    # path('signup/login/',views.login,name='login'),
    # path('home/',views.home,name='home'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    # path('/about',views.about,name='about'),
    # path('/blog',views.blog,name='blog'),
    # path('/feature',views.feature,name='feature'),
    # path('/contact',views.contact,name='contact'),
    # path('admindashboard/',include('Dashboard.urls'))
]