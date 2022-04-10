from django.db import models


class Category(models.Model):
# verbose_name='Название'
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
# blank позволяет сохранять пустые поля, null разрешает Null
# editable=False - запрещает редактировать в админке
# help_text - описание для админки
# verbose_name='Описание'
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Good(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    # img_good = models.ImageField(upload_to='static/images', height_field=None, width_field=None. max_length=100)
    # on_delete=protect запрещает удаление
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-price']


class Course(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=16)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
