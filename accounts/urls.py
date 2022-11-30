from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',views.home, name = 'home'),
    path('signup/login/', views.login, name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('about/',login_required(views.about), name = 'about'),
    path('blog/',views.blog, name = 'blog'),
    path('contact/',views.contact, name = 'contact'),
    path('contact/success/',views.contactres, name = 'success'),
    path('feature/',views.feature, name = 'feature'),
    path('login/admindashboard',views.index, name = 'dashboard'),
    path('login/newproject',views.newproject, name = 'newproject'),
    path('login/newproject/success',views.addproject, name = 'addproject'),
    path('login/displayprojects',views.displayprojects, name = 'displayprojects'),
    path('login/removeproject',views.removeproject, name = 'removeproject'),
    path('login/login/removeproject/<int:prj_id>',views.removeproject, name = 'removeproject'),
    path('login/dashboard',views.index, name = 'dashboardhome'),
    path('login/kanban',views.kanban,name = 'kanban'),
]
