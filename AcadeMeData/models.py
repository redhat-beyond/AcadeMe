from django.db import models, transaction
from django.conf import settings
from django.contrib.auth.models import User as DjangoUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class DEGREECHOICES(models.TextChoices):
    Computer_Science = 'CS', 'Computer Science'
    Psychology = 'PS', 'Psychology'
    GOVERNMENT = 'GV', 'Government'
    Business_Administration = 'BA', 'Business Administration'
    Unknown = 'UN', 'Unknown'


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
    university = models.CharField(max_length=2, choices=UNIVERSITYCHOICES.choices, default=UNIVERSITYCHOICES.Unknown)
    degree = models.CharField(max_length=2, choices=DEGREECHOICES.choices, default=DEGREECHOICES.Unknown)

    @staticmethod
    def create_user(username, email, password, university, degree):
        django_user = DjangoUser.objects.create_user(username=username,
                                                     email=email,
                                                     password=password)
        user = User(user=django_user,
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

    @staticmethod
    def get_degree_by_name(name):
        """
        Gets us the Degree object with input 'name' as its name.
        """
        try:
            degree = Degree.objects.get(name=name)
        except Degree.DoesNotExist:
            return None
        return degree


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
    def get_professor(name):
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
    name = models.CharField(max_length=100, unique=True)
    degree = models.ManyToManyField(Degree)
    mandatory = models.BooleanField(default=False)  # False for elective, True for mandatory
    description = models.TextField(null=True, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.RESTRICT)
    university = models.ForeignKey(University, on_delete=models.RESTRICT)

    @staticmethod
    def create_course(course_id, name, degree, mandatory, description, professor, university):
        """
        Creates a Course object.
        """
        course = Course(course_id=course_id,
                        name=name,
                        mandatory=mandatory,
                        description=description,
                        professor=professor,
                        university=university)
        course.degree.add(degree)
        course.save()
        return course

    def __str__(self):
        return self.name

    @staticmethod
    def get_course_by_name(name):
        """
        Gets us the Degree object with input 'name' as its name.
        """
        try:
            course = Course.objects.get(name=name)
            return course
        except Course.DoesNotExist:
            return None

    def course_belongs(self, university, degree):
        """
        returns if course belongs to this degree in this university
        """
        return degree in self.degree.all() and university == self.university

    @staticmethod
    def get_course_by_id(id):
        """
        Gets us the Course object with input 'id' as its id.
        """
        try:
            course = Course.objects.get(course_id=id)
            return course
        except Course.DoesNotExist:
            return None


class MessageBoards(models.Model):
    id = models.IntegerField(primary_key=True)
    courseName = models.ForeignKey(Course, null=False, blank=True, on_delete=models.CASCADE, default=0)

    @staticmethod
    def create_msgboard(id, courseName):
        msgboard = MessageBoards(id=id, courseName=courseName)
        msgboard.save()
        return msgboard

    @staticmethod
    def get_msgboard_by_id(id):
        return MessageBoards.objects.get(id=id)

    @staticmethod
    def get_msgboard_by_course(course):
        return MessageBoards.objects.get(courseName=course)


class Messages(models.Model):
    msgID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    text = models.TextField(max_length=300)
    msgDate = models.DateTimeField(default=timezone.now)
    board = models.ForeignKey(MessageBoards, on_delete=models.CASCADE, default=1)

    def get_msg(self):
        return self.msgID

    def create_message(id, user, text, board):
        with transaction.atomic():
            msg = Messages(msgID=id, userID=user, text=text, board=board)
            msg.save()
            return msg

    @staticmethod
    def get_msg_by_id(msgID):
        return Messages.objects.get(msgID=msgID)


class MessageTags(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    msg = models.ForeignKey(Messages, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_msgtag(id, msg, userID):
        with transaction.atomic():
            tag = MessageTags(id=id, msg=msg, userID=userID)
            tag.save()
            return tag

    def __str__(self):
        return self.id

    def get_msg_tag(id):
        return MessageTags.objects.get(id=id)
