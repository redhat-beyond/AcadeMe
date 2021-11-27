from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from AcadeMeData.models import Course, Degree, Professor

        degree = Degree(degree_id=1, name="Computer Science", universities="Ben Gurion University",
                        description="Learn about how to write awesome code!").save()
        professor = Professor(professor_id=1, name="Shimon Shocken", university='RU',
                              description="Nice guy", rate=1).save()

        test_data = [
            (1, 'Open Source Code Workshop', degree, False, 'Build a Django project from the grounds up!',
             professor),
            (2, '16th Century Poetry', degree, True,
             'Learn about the revolution in poetry in 16th century England', professor),
        ]
        with transaction.atomic():
            for id, name, degree, elective, description, professor in test_data:
                Course(course_id=id, name=name, elective=elective,
                       description=description, professor=professor).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
