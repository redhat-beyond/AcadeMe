from django.db import models


class Degree(models.Model):
    degree = models.CharField(max_length=100)
    universities = models.TextField(null=True, blank=True)  # Format should be "Uni1, Uni2, Uni3,..."
    description = models.TextField(null=True, blank=True)  # Describes the degree

    # methods
    def __str__(self):
        """
        Returns the name of all possible degrees in the database.
        """
        return self.degree

    def get_name(self):
        return self.degree

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
