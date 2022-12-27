from django.db import models

# Create your models here.
class Todo(models.Model):
  PRIORITY = (
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low')
  )
  # ineger db'de daha az yer tutar, onun için 1,2,3 olarak tanımladık
  task = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  priority = models.SmallIntegerField(choices=PRIORITY, default=3)
  is_done = models.BooleanField(default=False)
  updated_date = models.DateTimeField(auto_now=True)
  created_date = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.task