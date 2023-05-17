from django.contrib.auth.models import User
from django.db.models import CASCADE, DateTimeField, ForeignKey, CharField, Model


# Create your models here.

class Poll(Model):
    question = CharField(max_length=100)
    created_by = ForeignKey(User, CASCADE)
    pub_date = DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(Model):
    poll = ForeignKey('apps.Poll', CASCADE, 'choices')
    choice_text = CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(Model):
    choice = ForeignKey('apps.Choice', CASCADE, 'votes')
    poll = ForeignKey('apps.Poll', CASCADE)
    voted_by = ForeignKey(User, CASCADE)

    class Meta:
        unique_together = ("poll", "voted_by")
