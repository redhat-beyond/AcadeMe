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
        Creates a Degree object.
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


class University(models.Model):
    university_id = models.IntegerField(
        primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # maybe change here to: description = models.TextField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_university_by_name(name):
        # gets the relevant university that match the given name
        return University.objects.get(name=name)

    @staticmethod
    def get_university_by_location(location):
        # gets the relevant university that match the given location
        return University.objects.get(location=location)


class Professor(models.Model):
    professor_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.RESTRICT)  # , related_name='%(class)s_something')
    description = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)],
                               blank=True, null=True)  # average professor rating, starts as null

    def __str__(self):
        return self.name

    @staticmethod
    def create_professor(professor_id, name, university, description, rate):
        professor = Professor(professor_id=professor_id,
                              name=name,
                              university=university,
                              description=description,
                              rate=rate)
        professor.save()
        return professor

    @staticmethod
    def get_proffesor(name):
        try:
            professor = Professor.objects.get(name=name)
        except professor.DoesNotExist:
            return None
        return professor

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)], default=0)
    name = models.CharField(max_length=100)  # Name of the course
    degree = models.ForeignKey(Degree, on_delete=models.RESTRICT)
    elective = models.BooleanField(default=False) # False for mandatory, True for elective
    description = models.TextField(null=True, blank=True) #Decribes the course
    professor = models.ForeignKey(Professor, on_delete=models.RESTRICT)

    # Fields for a rating system we will implement later:
    # The rating of this course.
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=
        [MinValueValidator(1), MaxValueValidator(5)],
        blank=True, null=True)
    # Counter for the number of rates, will be used later to calculate the rating.
    sum_rates = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)


    #methods
    def __str__(self):
        """
        Returns the name of all possible courses in the database.
        """
        return self.course

    @staticmethod
    def create_course(course_id, name, degree, elective, description, professor):
        """
        Creates a Course object.
        """
        course = Course(course_id=course_id,
                              name=name,
                              degree=degree,
                              elective=elective,
                              description=description,
                              professor=professor)
        course.save()
        return course

    def get_name(self):
        """
        Returns the name of this specific course.
        """
        return self.course

    def get_description(self):
        """
        Returns the description of a specific course.
        """
        return self.description

    def is_elective(self):
        """
        Returns 'True' if this course is an elective
        and 'False' if this course is mandatory.
        """
        return self.elective
