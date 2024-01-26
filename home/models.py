from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_content = models.TextField(null=False, blank=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
