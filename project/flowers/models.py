from django.db import models


class Types(models.Model):
    name = models.CharField(max_length=100,verbose_name='gul nomi')
    color = models.CharField(max_length=100, verbose_name='gul rangi')



    def __string__(self):
        return self.name

    class Meta:
        verbose_name="Turi"
        verbose_name_plural='Gullar turi'

class Flower (models.Model):
    name=models.CharField(max_length=100,verbose_name='gul nomi')
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='gulning narxi')
    descriptions=models.TextField(verbose_name='gul haqida tushuncha')
    image=models.ImageField(upload_to='flowers/',verbose_name='gulning rasmi')
    views=models.IntegerField(default=0, verbose_name='korishlar soni' , help_text='erkak boling korishlar soniga tegmang😑')
    types=models.ForeignKey(Types, on_delete=models.CASCADE)

    def __String__(self):
        return self.name

    class Meta:
        verbose_name = 'Gullar'
        verbose_name_plural = 'Gullar malumoti'