from django.db import models

# Create your models here.


# Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Book : =>
class Book(models.Model):
    BOOK_TYPES = [
        ("novel", "Novel"),
        ("history", "History"),
        ("science_fiction", "Science Fiction"),
        ("biography", "Biography"),
        ("other", "Other"),
    ]
    BOOK_STATUS = [
        ("available", "available"),
        ("rental", "rental"),
        ("sold", "sold"),
    ]

    title = models.CharField(max_length=250, verbose_name="Title")
    author = models.CharField(
        max_length=250, verbose_name="Author", null=True, blank=True
    )
    book_photo = models.ImageField(
        upload_to="photos", null=True, blank=True, verbose_name="Book Cover Image"
    )
    author_photo = models.ImageField(
        upload_to="photos", null=True, blank=True, verbose_name="Author Cover Image"
    )
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ratal_price_day = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    ratal_period = models.IntegerField(null=True, blank=True)
    activate = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=BOOK_STATUS, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True
    )
    # book_type = models.CharField(max_length=20, choices=BOOK_TYPES, default='other', verbose_name='Book Type')

    # publication_date = models.DateField(verbose_name='Publication Date')
    # isbn = models.CharField(max_length=13, verbose_name='ISBN', unique=True)
    # summary = models.TextField(verbose_name='Summary', null=True, blank=True)
    # page_count = models.PositiveIntegerField(verbose_name='Page Count')

    def __str__(self):
        return self.title
