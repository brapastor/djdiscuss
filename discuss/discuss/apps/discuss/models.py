from django.db import models
from discuss.apps.users.models import User

class TimeStampModel(models.Model):
    user = models.ForeignKey(User)
    description =  models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True


class Tag (models.Model):

    nombre = models.CharField(max_length=10)

    # para poder ver en el administrador
    def __unicode__(self):
        return self.nombre

class Question(TimeStampModel):
    tag =  models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)

    # para ver el el administrador
    def __unicode__(self):
        return '%s %s' % (self.user, self.title)

class Answer(TimeStampModel):
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.user
