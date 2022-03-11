from django.contrib import admin
from .models import Books, BookGrades, Publisher, Publication, Author, Genres, Book_Genres, PublicationComments

# Register your models here.


admin.site.register(Books)

admin.site.register(BookGrades)

admin.site.register(Publisher)
admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Genres)
admin.site.register(Book_Genres)
admin.site.register(PublicationComments)

