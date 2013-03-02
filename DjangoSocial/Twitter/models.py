from django.db import models

class TwitterQuery(models.Model) :
    query = models.CharField(max_length = 100)
    max_keywords = models.IntegerField()

    def __unicode__(self):
        return self.query