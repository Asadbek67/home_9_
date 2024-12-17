from django.db import models

class Types(models.Model):
    name = models.CharField(max_length=100, verbose_name='Gul nomi')
    color = models.CharField(max_length=100, verbose_name='Gul rangi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Turi"
        verbose_name_plural = "Gullar turi"

class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name='Gul nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Gulning narxi')
    descriptions = models.TextField(verbose_name='Gul haqida tushuncha')
    image = models.ImageField(upload_to='flowers/', verbose_name='Gulning rasmi')
    views = models.IntegerField(default=0, verbose_name='Ko\'rishlar soni', help_text='Ko\'rishlar soniga tegmang 😑')
    types = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='flowers')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gullar"
        verbose_name_plural = "Gullar ma'lumoti"
