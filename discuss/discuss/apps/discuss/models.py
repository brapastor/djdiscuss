from django.db import models
from psycopg2._psycopg import DATETIME

from discuss.apps.users.models import User
from django.template.defaultfilters import slugify
import datetime
class TimeStampModel(models.Model):
    user = models.ForeignKey(User, db_index=True, null=True, blank=True)
    description =  models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True


class Tag (models.Model):

    nombre = models.CharField(max_length=10)

    # para poder ver en el administrador
    def __str__(self):
        return self.nombre

class Question(TimeStampModel):
    tag =  models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    # El editable False hara que no salga en el navegador
    slug = models.SlugField(editable=False, unique=True)

    # para ver el el administrador
    def __str__(self):
        return '%s %s' % (self.user, self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Question, self).save(*args,**kwargs)


class Answer(TimeStampModel):
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.user
