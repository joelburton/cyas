from django.db import models
from django.core.exceptions import ValidationError

# survey
# name
# #1 proj
# #2 proj

class Project(models.Model):
    title = models.CharField(
        max_length=50,
    )

    inventor = models.CharField(
        max_length=20,
    )
    
    def __str__(self):
        return self.title

    # TODOS
    

class Survey(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter your name",
    )

    project1 = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        related_name="fav1",
        null=True,
        blank=False,
    )

    project2 = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        related_name="fav2",
        null=True,
        blank=False,
    )

    def __str__(self):
        return self.name

    def clean(self):
        if self.project1 == self.project2:
            raise ValidationError("Cannot pick same project")
