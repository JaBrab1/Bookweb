import pytest
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from Bookweb.models import Books, Author, Genres, Publisher, Publication


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_detail(client, django_user_model):
   user = django_user_model.objects.create(
       username='someone', password='password'
   )
   url = reverse('register')
   response = client.get(url)
   assert response.status_code == 200
   assert User.objects.get(username='someone',password='password')

@pytest.mark.django_db
def test_login(client, django_user_model):
    user = django_user_model.objects.create(
        username='someone', password='password'
    )
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'username': 'someone',
        'password': 'password',
    }
    assert client.post(url, dct)

@pytest.mark.django_db
def test_logout(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'username': 'Brabek',
        'password': 'ala',
    }
    assert client.post(url, dct)
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_book(client, user):
    author = Author.objects.create(first_name='slawek', last_name='bo', description='fajny')
    genre = Genres.objects.create(name='slawek', description='fajny')
    # books = Books.objects.create(title='title', author=Author.objects.get(id=1), description='johnpassword', accepted=bool())
    client.force_login(user)
    dct = {
        'title': 'HobsaaHobsaa',
        'author': author.id,
        'description': 'extra',
        'genre': [genre.id]
    }
    url = reverse('add_book')
    response = client.post(url, dct)

    assert Books.objects.count() == 1

@pytest.mark.django_db
def test_authors(client, authors):
    url = reverse('authors')
    response = client.get(url)
    assert response.status_code == 200
    assert len(Author.objects.all())==3

@pytest.mark.django_db
def test_genres(client, genres):
    url = reverse('genres')
    response = client.get(url)
    assert response.status_code == 200
    assert len(Genres.objects.all())==3

@pytest.mark.django_db
def test_publishers(client, publishers):
    url = reverse('publishers')
    response = client.get(url)
    assert response.status_code == 200
    assert len(Publisher.objects.all())==3

@pytest.mark.django_db
def test_users(client, user):
    url = reverse('users')
    response = client.get(url)
    assert response.status_code == 200
    assert len(User.objects.all()) == 1

@pytest.mark.django_db
def test_add_author(client, user):
    client.force_login(user)
    dct = {
        'first_name': 'Misio',
        'last_name': 'Patysio',
        'description': 'extra typ'
    }
    url = reverse('add_author')
    response = client.post(url, dct)

    assert len(Author.objects.all()) == 1

@pytest.mark.django_db
def test_genre_get_view(client):
    genre = Genres.objects.create(name='siemanko', description='fajny')
    url = reverse('genre_detail', args=[genre.id])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_author_get_view(client):
    author = Author.objects.create(first_name='siemanko',last_name='siemanko', description='fajny')
    url = reverse('author_detail', args=[author.id])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_book_get_view(client):
    author = Author.objects.create(first_name='siemanko', last_name='siemanko', description='fajny')
    book = Books.objects.create(title='siemanko',author=author, description='fajny')
    url = reverse('book_detail', args=[book.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_get_view(client, user):
    url = reverse('profile_detail', args=[user.id])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_interface_get_view(client, user):
    client.force_login(user)
    url = reverse('user_interface', args=[user.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_edit_get_view(client, user):
    client.force_login(user)
    url = reverse('user_edit', args=[user.id])
    response = client.get(url)
    assert response.status_code == 200




@pytest.mark.django_db
def test_publisher_detail_get_view(client, user):
    publisher = Publisher.objects.create(name='siemanko', description='fajny')
    client.force_login(user)
    url = reverse('publisher_detail', args=[publisher.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_publication_detail_get_view(client, author):
    publisher = Publisher.objects.create(name='siemanko', description='fajny')
    book = Books.objects.create(title='siemanko', author=author, description='fajny')
    publication = Publication.objects.create(book=book, publisher=publisher , publication_year='1212')
    url = reverse('publication_detail', args=[publication.id])
    response = client.get(url)
    assert response.status_code == 200
