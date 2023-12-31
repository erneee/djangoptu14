from django.db import models
import uuid

class Author(models.Model):
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavarde', max_length=100)
    description = models.TextField('Aprasymas', max_length=2000, default='Labai geras autorius')

    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def display_books(self):
        return ', '.join(book.title for book in self.books.all()[:2])

    display_books.short_description = "Knygos"


class Book(models.Model):
    title = models.CharField('Pavadinimas', max_length=200)
    summary = models.TextField('Aprasymas', max_length=1000)
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Simbolių '
                                                             '<a href="https://www.isbn-international.org/content/what-isbn"> ISBN kodas</a>')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='books')
    genre = models.ManyToManyField('Genre', help_text='Isrinkite zanra(-us)')

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:2])


    display_genre.short_description = "Zanras"
    author.short_description = "Autorius"



class Genre(models.Model):
    name = models.CharField('Pavadinimas', max_length=25, help_text='Sukurkite zanra')

    class Meta:
        verbose_name = "Zanras"
        verbose_name_plural = "Zanrai"


    def __str__(self):
        return self.name

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='bookinstance_set')
    due_back = models.DateField('Bus prieinama', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Kopijos statusas'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        # return f"{self.id} {self.book.title} {self.book.author.first_name}"
        return f"{self.id}"
