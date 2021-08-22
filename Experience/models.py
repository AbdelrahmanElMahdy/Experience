from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


# Create your models here.

class Experience(models.Model):
    id = models.BigAutoField(primary_key=True)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name="Auther", 
        on_delete=models.CASCADE
    )
    story=models.TextField(
        verbose_name="Story",
        blank=False
    )
    foundation=models.CharField(
        verbose_name="foundation", 
        max_length=50,blank=False
    )  
    data_added=models.DateField(
        verbose_name="Date Field", 
        auto_now=True, 
        auto_now_add=False
    )

    def __str__(self):
        return self.story 

class Rate(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_choices = (
        ("suggest", _("SUGGEST")),
        ("compliment", _("COMPLIMENT")),
        ("complaint", _("COMPLAINT")),
    )
    rate_choices = (
        ("verybad", _("Very Bad")),
        ("notbad", _("Not Bad")),
        (("good"), _("Good")),
        ("verygood", _("very good")),
        ("excellent", _("Excellent")),
    )
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name="Auther", 
        on_delete=models.CASCADE)
    
    rate = models.CharField(
        verbose_name="Rate", 
        max_length=50, 
        choices=rate_choices)

    rate_category = models.CharField(
        verbose_name="Rate Category", 
        choices=category_choices, 
        max_length=50, 
        blank=True
    )

    message = models.TextField(
        verbose_name="Message", 
        max_length=250, 
        blank=True
    )
    
    experience=models.ForeignKey(
        Experience, 
        verbose_name=_("Experience"), 
        on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rate_category


