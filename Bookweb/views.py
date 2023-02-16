from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, AuthorSearchForm, UserProfileForm, BookSearchForm, AllSearchForm, \
    AddCommentForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
from .models import Genres, Author, Books, Publication, Publisher, BookGrades


class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['pass1']
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name,
                last_name=surname
            )
            return redirect('/')
        else:
            return render(request, 'register.html', {'form':form})

class LoginView(View):
    def get(self,request    ):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    def post(self,request   ):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['login']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_login, password=user_password)
            if user is None:
                return render(request, 'login.html', {'form':form})
            else:
                login(request, user)
                return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self,request):
        form_search = AllSearchForm()
        logout(request)
        return render(request, 'base.html', {'form_search': form_search})


class MainView(View):
    def get(self, request):
        form_search = AllSearchForm()
        return render(request, 'base.html', {'form_search': form_search})

    def post(self, request):
        form_search = AllSearchForm(request.POST)
        if form_search.is_valid():
            search_author = Author.objects.filter(last_name__icontains=form_search.cleaned_data['search'])
            search_book = Books.objects.filter(title__contains=form_search.cleaned_data['search'])
            search_publisher = Publisher.objects.filter(name__contains=form_search.cleaned_data['search'])
            return render(request, 'base.html',
                          {'form_search': form_search, 'search_author': search_author, 'search_book': search_book,
                           'search_publisher':search_publisher})
        else:
            return render(request, 'base.html', {'form_search': form_search})

class AddBookView(LoginRequiredMixin, CreateView):
    model = Books
    fields = ['title', 'author', 'description', 'genre']
    success_url = ('/')

class AddAuthorView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'description']
    success_url = ('/')

class GenresListView(View):
    def get(self, request):
        genres = Genres.objects.all()
        return render(request, 'genres_list.html', {'genres': genres})

class GenreDetailView(View):
    def get(self, request, pk):
        genre = Genres.objects.get(id=pk)
        return render(request, 'genre_details.html', {
            'genre':genre
        })

class AuthorListView(View):
    def get(self, request):
        author = Author.objects.all()
        return render(request, 'author_list.html', {'author': author})

class UsersListView(View):
    def get(self, request):
        user = User.objects.all()

        return render(request, 'users_list.html', {'user': user})


class AuthorDetailView(View):
    def get(self, request, pk):
        author = Author.objects.get(id=pk)
        return render(request, 'author_details.html', {
            'author':author
        })

class BookDetailView(View):
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        add_comment = AddCommentForm()
        return render(request, 'book_details.html', {
            'book':book, 'add_comment':add_comment
        })
    def post(self, request, pk):
        user = request.user
        book = Books.objects.get(id=pk)
        add_comment = AddCommentForm()
        try:
            bookgrades = book.bookgrades_set.get(id=book.id)
            grade = request.POST.get('grade')
            comment = request.POST.get("comment")
            bookgrades.grade = int(grade[0])
            bookgrades.comment = comment
            bookgrades.save()
            return render(request, 'book_details.html', {
                'book': book, 'add_comment': add_comment
            })
        except:
            grade = request.POST.get('grade')
            comment = request.POST.get('comment')
            BookGrades.objects.update(
                user=user,
                book=book,
                comment=comment,
                grade=grade
            )
            return render(request, 'book_details.html', {
                'book': book, 'add_comment': add_comment
            })




class UserProfile(View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return render(request, 'user_profile.html', {
            'user':user
        })


class UserInterface(LoginRequiredMixin, View):

    def get(self, request, pk):
        u = User.objects.get(id=pk)
        if u == request.user:
            return render(request, 'user_interface.html', {'user': u})
        else:
            raise PermissionDenied

class ChangeDataAccount(LoginRequiredMixin, View):
    def get(self, request, pk):
        u = User.objects.get(id=pk)
        if u == request.user:
            form = UserProfileForm(initial={
                'first_name': u.first_name,
                'last_name': u.last_name,
                'email': u.email})
            return render(request, 'user_edit.html', {'form':form})
        else:
            raise PermissionDenied
    def post(self, request, pk):
        u = User.objects.get(id=pk)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        u.first_name = first_name
        u.last_name = last_name
        u.email = email
        u.save()
        return redirect(f'/')

class PublishersListView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'publisher_list.html', {'publishers': publishers})

class PublisherDetailView(View):
    def get(self, request, pk):
        publisher = Publisher.objects.get(id=pk)
        return render(request, 'publisher_details.html', {
            'publisher':publisher
        })

class PublicationDetailView(View):
    def get(self, request, pk):
        publication = Publication.objects.get(id=pk)
        return render(request, 'publication_details.html', {
            'publication':publication
        })

