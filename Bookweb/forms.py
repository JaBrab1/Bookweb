import django.forms as forms
from .models import Books, Genres, Author, Publisher, Publication, Book_Genres, BookGrades, GRADES
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_username_is_not_taken(value):
    if User.objects.filter(username=value):
        raise ValidationError('Ten login jest już zajęty')

class RegisterForm(forms.Form):

    login = forms.CharField(validators=[validate_username_is_not_taken], label='Nazwa użytkownika')
    pass1 = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    pass2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz Hasło')
    first_name = forms.CharField(label='imie')
    last_name = forms.CharField(label='nazwisko')
    email = forms.EmailField(label='email')

    def clean(self):
        cleaned_data= super().clean()
        if cleaned_data['pass1'] != cleaned_data['pass2']:
            raise ValidationError('hasła nie sa takie same')
        return cleaned_data

class LoginForm(forms.Form):
    login = forms.CharField(max_length=64, label='Twój Login')
    password = forms.CharField(widget=forms.PasswordInput)



# class AddBookForm(forms.Form):
#     title = forms.CharField(label='Tytuł', max_length=250)
#     author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Author')
#     description = forms.CharField(widget=forms.Textarea())
#     genre = forms.ModelMultipleChoiceField(
#                        widget = forms.CheckboxSelectMultiple,
#                        queryset = Genres.objects.all(),
#                         label='Gatunek (może być kilka)'
#                )
    #formularz dodania ksiazki, pod adresem /add_book/

# class AddAuthorForm(forms.Form):
#     first_name = forms.CharField(label='Imię', max_length=50)
#     last_name = forms.CharField(label='Nazwisko', max_length=50)
#     description = forms.CharField(widget=forms.Textarea())
    #formularz dodania ksiazki, pod adresem /add_author/

class UserProfileForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=100)
    last_name = forms.CharField(label='Nazwisko', max_length=100)
    email = forms.EmailField(label='email')
    #formularz edycji danych uzytkownika w jego interface

class AuthorSearchForm(forms.Form):
    last_name = forms.CharField(label='Nazwisko Autora', max_length=50)

class BookSearchForm(forms.Form):
    title = forms.CharField(label='Tytuł Książki', max_length=100)

class AllSearchForm(forms.Form):
    search = forms.CharField(label='Wyszukaj', max_length=100)

class AddCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(), label='Skomentuj')
    grade = forms.ChoiceField(choices=GRADES, label='Ocena')
