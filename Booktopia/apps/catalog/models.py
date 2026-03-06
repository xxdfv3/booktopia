from django.db import models

class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=100)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    description = models.TextField("Описание", blank=True, null=True)
    published_year = models.IntegerField("Год издания", null=True, blank=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.author}"