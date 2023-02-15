from django.db import models

# Create your models here.
class Todo(models.Model):
    
    priority_choices = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    )
    # integer db'de daha az yer tutar, onun için 1,2,3 olarak tanımladık
    
    
    status_choices = (
        ('c', 'Complated'),
        ('w', 'Waiting'),
        ('p', 'On Progress')
    )
    # integer yerine string olark da tanımlanabilir.
    
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=priority_choices, default=3)
    
    #? default değer number olmadığı için CharField kullanılabilir. 
    status = models.CharField(choices=status_choices , default='w', max_length=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title