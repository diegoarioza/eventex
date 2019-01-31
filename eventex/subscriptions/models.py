from django.db import models


class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    created_at = models.DateTimeField('Criado Em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'inscricoes'
        verbose_name = 'inscricao'
        ordering = ('-created_at',)