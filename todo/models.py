from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)
        verbose_name = ('TodoList')
        verbose_name_plural = ('TodoLists')

    def __str__(self):
        return self.title