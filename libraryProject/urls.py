from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='index'),
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
]