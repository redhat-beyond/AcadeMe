from django.db import models
from django.conf import settings
from django.contrib.auth.models import User as DjangoUser
from django.core.validators import MinValueValidator, MaxValueValidator


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
        except DjangoUser.DoesNotExist:
            return None
        return user

    """    def get_user(username):
        try:
            user = DjangoUser.objects.get(username=username)
        except User.DoesNotExist:
            return False
        return user
    """


class Degree(models.Model):
    degree_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)], default=0)
    name = models.CharField(max_length=100)
    universities = models.TextField(null=True, blank=True)  # Format should be "Uni1, Uni2, Uni3,..."
    description = models.TextField(null=True, blank=True)  # Describes the degree

    # methods
    def __str__(self):
        """
        Returns the name of all possible degrees in the database.
        """
        
        return self.name

    @staticmethod
    def create_degree(degree_id, name, universities, description):
        """
        Creates a degree object.
        """
        
        degree = Degree(degree_id=degree_id, name=name, universities=universities, description=description)
        degree.save()
        return degree
       
    def get_name(self):
        """
        Returns the name of a specific degree.
        """
        
        return self.name

    def get_description(self):
        """
        Returns the description of a specific degree.
        """
        
        return self.description

    def get_universities(self):
        """
        Returns a string of all universities that offers this degree.
        * will be used later to determine if a university offers the specific degree.
        """
        
        return self.universities

