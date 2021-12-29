from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from AcadeMeData.models import Course, Degree, Professor, University

        university = University(university_id=1, name="Reichman University", location='Herzliya',
                                description='Very nice university')
        university.save()

        degree = Degree(degree_id=2, name="Computer Science", universities="Ben Gurion University",
                        description="Learn about how to write awesome code!")
        degree.save()

        professor = Professor(professor_id=3, name="Shimon Shocken", university=university,
                              description="Nice guy", rate=1)
        professor.save()

        test_data = [
            (1, 'Open Source Code Workshop', degree, False, 'Build a Django project from the grounds up!',
             professor, university),
            (2, '16th Century Poetry', degree, True,
             'Learn about the revolution in poetry in 16th century England', professor, university),
        ]
        with transaction.atomic():
            for id, name, degree, mandatory, description, professor, university in test_data:
                course = Course(course_id=id, name=name, mandatory=mandatory,
                                description=description, professor=professor, university=university)
                course.degree.add(degree)
                course.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
