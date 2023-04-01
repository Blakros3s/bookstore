"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # categories
    path('category/add/', views.category_add, name='add-category'),
    path('category/', views.category_index, name='list-category'),
    path('category/update/', views.category_update, name='update-category'),
    path('category/edit/<int:id>/', views.category_edit, name='edit-category'),
    path('category/delete/<int:id>/', views.category_delete, name='delete-category'),

    # products
    path('book/add/', views.book_add, name='add-book'),
    path('book/', views.book_index, name='list-book'),
    path('book/update/', views.book_update, name='update-book'),
    path('book/view/<int:id>/', views.book_view, name='view-book'),
    path('book/edit/<int:id>/', views.book_edit, name='edit-book'),
    path('book/delete/<int:id>/', views.book_delete, name='delete-book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)