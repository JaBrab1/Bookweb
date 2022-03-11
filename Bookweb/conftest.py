import pytest
from django.contrib.auth.models import User
from django.test import Client

from Bookweb.models import Books, Author, Genres, Publisher


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def register():
    pass1 = 'elo'
    pass2 = 'elo'
    return pass1 == pass2

@pytest.fixture
def user():
    user = User(username='Brabek')
    user.set_password('ala')
    user.save()
    return user

# @pytest.fixture
# def book():
#     author = Author.objects.create(first_name='slawek', last_name='bo', description='fajny')
#     genre = Genres.objects.create(name='slawek', description='fajny')
#     books = Books.objects.create(
#        'title', Author.objects.get(id=1), 'johnpassword', Genres.objects.get(id=1), bool()
#    )
#     return books

@pytest.fixture
def author():
    author = Author.objects.create(first_name='slawek', last_name='bo', description='fajny')
    return author

@pytest.fixture
def genre():

    genre = Genres.objects.create(name='slawek', description='fajny')
    genre2 = Genres.objects.create(name='fajny', description='bardzo')

    return genre

@pytest.fixture
def authors():
    lst = []
    a = Author.objects.create(first_name='slawek', last_name='bo')
    lst.append(a)
    a = Author.objects.create(first_name='Gosia', last_name='bo')
    lst.append(a)
    a = Author.objects.create(first_name='Kasia', last_name='bo')
    lst.append(a)
    return lst

@pytest.fixture
def genres():
    lst = []
    a = Genres.objects.create(name='slawek', description='bo')
    lst.append(a)
    a = Genres.objects.create(name='Gosia', description='bo')
    lst.append(a)
    a = Genres.objects.create(name='Kasia', description='bo')
    lst.append(a)
    return lst

@pytest.fixture
def publishers():
    lst = []
    a = Publisher.objects.create(name='slawek', description='bo')
    lst.append(a)
    a = Publisher.objects.create(name='Gosia', description='bo')
    lst.append(a)
    a = Publisher.objects.create(name='Kasia', description='bo')
    lst.append(a)
    return lst