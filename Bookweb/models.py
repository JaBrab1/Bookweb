from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GRADES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10")
)


class Genres(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()

    @property
    def avg_grade(self):
        books = self.books_set.all()
        sum = 0
        grades = 0
        if len(list(books)) == 0:
            return 'brak dodanych książek'
        for book in books:
            for gread in book.bookgrades_set.all():
                sum += gread.grade
                grades += 1
            if grades == 0:
                return "brak ocen"
            else:
                return sum / grades
        return sum / grades

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Books(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    genre = models.ManyToManyField(Genres, through="Book_Genres")
    accepted = models.BooleanField(default=False)

    @property
    def avg_grade(self):
        sum = 0
        grades = 0
        for grade in self.bookgrades_set.all():
            sum += grade.grade
            grades += 1
        if grades == 0:
            return "brak ocen"
        else:
            return sum / grades

    def publications(self):
        return list(self.publication_set.all())

    def __str__(self):
        return self.title


class BookGrades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=GRADES)
    comment = models.TextField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='dzieciol')
        ]

    @property
    def name(self):
        return "{} | {} | {}".format(self.user, self.grade, self.book)



    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publication(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.name




    @property
    def name(self):
        return "{} | {} | {}".format(self.book, self.publication_year, self.publisher)

    def __str__(self):
        return self.name


class Book_Genres(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    @property
    def name(self):
        return "{} || {}".format(self.book, self.genre)

    def __str__(self):
        return self.name

class PublicationComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'publication'], name='dzieciol2')
        ]

    @property
    def name(self):
        return "{} | {} | {} | {}".format(self.user, self.publication.book.title, self.publication.publication_year, self.publication.publisher)

    def __str__(self):
        return self.name