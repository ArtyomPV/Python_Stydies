from datetime import datetime

from django.db import models


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(default=0)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    product = models.ManyToManyField('Product', through='ProductOrder')

    def __str__(self):
        return f'Order #{self.pk} - Total: {self.cost}'

    @property
    def total(self):
        sum = self.product.aggregate(sum=models.Sum('price'))['sum']
        self.cost = sum
        self.save()
        return sum

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()
