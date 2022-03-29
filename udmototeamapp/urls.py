from django.urls import path
from . import views
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView

urlpatterns = [
    path('index/', views.inicio, name='inicio'),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]