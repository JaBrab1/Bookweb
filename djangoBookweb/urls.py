"""djangoBookweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Bookweb.views import MainView, AddBookView, RegisterView, LoginView, LogoutView, AddAuthorView, GenresListView, \
    GenreDetailView, AuthorListView, AuthorDetailView, BookDetailView, UserProfile, UserInterface, \
    UsersListView, ChangeDataAccount, PublishersListView, PublisherDetailView, PublicationDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('add_author/', AddAuthorView.as_view(), name='add_author'),
    path('genres/', GenresListView.as_view(), name='genres'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile_detail'),
    path('user_interface/<int:pk>/', UserInterface.as_view(), name='user_interface'),
    path('accounts/<int:pk>/update/', ChangeDataAccount.as_view(), name='user_edit'),
    path('users/', UsersListView.as_view(), name='users'),
    path('publishers/', PublishersListView.as_view(), name='publishers'),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail')

]
