from django.db import models

# Create your models here.


class item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        if self.status:
            return "\u2705" + "  " + self.title + "  " + self.description + "\n"
        else:
            return "\u2750" + "  " + self.title + "  " + self.description + "\n"
