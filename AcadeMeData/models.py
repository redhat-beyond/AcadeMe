from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import UserManager



class DEGREECHOICES(models.TextChoices):
    Computer_Science = 'CS', 'Computer Science'
    Psychology = 'PS', 'Psychology'
    GOVERNMENT = 'GV', 'Government'
    Business_Administration = 'BA', 'Business Administration'
    Unknown = 'UN', 'Unknown'


class TYPECHOICES(models.TextChoices):
    Student = 'S', 'Student'
    Expert = 'E', 'Expert'


class UNIVERSITYCHOICES(models.TextChoices):
    Reichman_University = 'RU', 'Reichman University'
    Hebrew_University = 'HU', 'Hebrew University'
    Tel_Aviv_University = 'TA', 'Tel Aviv University'
    Beer_Sheva_University = 'BS', "Be'er Sheva University"
    Unknown = 'UN', 'Unknown'


class User(models.Model):
    # The AUTH_USER_MODEL is the built in user model from django
    # Goto: https://docs.djangoproject.com/en/3.2/ref/contrib/auth/ for API
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # name = models.CharField(max_length=30, default="")  # we got the name\username from the built in user model django
    type = models.CharField(max_length=1, choices=TYPECHOICES.choices, default=TYPECHOICES.Student)
    university = models.CharField(max_length=2, choices=UNIVERSITYCHOICES.choices, default=UNIVERSITYCHOICES.Unknown)
    degree = models.CharField(max_length=2, choices=DEGREECHOICES.choices, default=DEGREECHOICES.Unknown)

    objects = UserManager()
    
    @staticmethod
    def create_user(username, email, password, type, university, degree):
        django_user = DjangoUser.objects.create_user(username=username,
                                                     email=email,
                                                     password=password)
        user = User(user=django_user,
                    type=type,
                    university=university,
                    degree=degree)
        user.save()
        return user

    @staticmethod
    def del_user(self):
        try:
            self.user.delete()
        except User.DoesNotExist:
            return False
        return True

    @staticmethod
    def get_user(username):
        try:
            user = DjangoUser.objects.get(username=username)
        except User.DoesNotExist:
            return False
        return user


class MessageBoards(models.Model):
    id = models.IntegerField(primary_key=True)
    courseName = models.TextField(max_length=30)

    def __str__(self):
        return self.id

class Messages(models.Model):
    msgID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    msgDate = models.DateTimeField(default=timezone.now)

    def get_msg(self):
        return self.msgID
    

