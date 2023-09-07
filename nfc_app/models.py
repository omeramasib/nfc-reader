from django.db import models

# Create your models here.
class NFCData(models.Model):
    card_id = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_id