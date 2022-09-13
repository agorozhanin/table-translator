from django.db import models


class Declaration(models.Model):
    """
    Модель декларации. Содержит атрибуты:
    id - первичный ключ записи (int)
    order_num - номер заказа (int)
    price_in_dollars - цена в долларах (decimal)
    price_in_roubles - цена в рублях (decimal)
    delivery_time - срок поставки (date)
    """

    class Meta:
        verbose_name = "Декларация"
        verbose_name_plural = "Декларации"

    id = models.AutoField(verbose_name="ID", primary_key=True)
    order_num = models.IntegerField(verbose_name="Номер заказа", null=False, unique=True, blank=False)
    price_in_dollars = models.DecimalField(verbose_name="Стоимость в долларах", null=False, unique=False, blank=False,
                                           max_digits=9, decimal_places=3)
    price_in_roubles = models.DecimalField(verbose_name="Стоимость в рублях", null=False, unique=False, blank=False,
                                           max_digits=9, decimal_places=3)
    delivery_time = models.DateField(verbose_name="Срок поставки", null=True, blank=True)

    def __str__(self):
        return f"{self.id}. {self.order_num}"
