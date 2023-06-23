from django.db import models

# Create your models here.
class Medicines(models.Model):
    name = models.CharField(max_length=30)
    manufac_date = models.DateField()
    expir_date = models.DateField()

    MTYPE = (
        ('fst', 'Таблетки'),
        ('scn', 'Капсулы'),
        ('thrd', 'Мазь'),
        ('frth' , 'Сироп'),
    )

    mtype = models.CharField(max_length=30, choices=MTYPE)
    price = models.PositiveIntegerField()
    decription = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return f"/{self.pk}"