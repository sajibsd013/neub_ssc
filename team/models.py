from django.db import models

# Create your models here.

class Committee_list(models.Model):
    session = models.CharField(max_length=122)
    active = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.session}"


class Team(models.Model):
    session = models.ForeignKey(Committee_list, on_delete= models.CASCADE)
    name = models.CharField(max_length=122)
    position = models.CharField(max_length=122)
    image = models.ImageField(upload_to ="Images")

    # def __str__(self):
    #     return f"{self.name} ({self.position}) - ({self.session})"
