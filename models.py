from django.db import models

class Robot(models.Model):
    name = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "робот-пылесос"
        verbose_name_plural = "роботы-пылесосы"
        ordering = ["name"] #сортировка по имени

    @property
    def __str__(self):
        return self.name
