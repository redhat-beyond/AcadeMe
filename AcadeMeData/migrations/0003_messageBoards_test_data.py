from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from AcadeMeData.models import MessageBoards, Course, Professor, University
        university = University(name='Reichman University', location='Herzliya', description='Very nice university')
        university.save()
        proffesor = Professor(professor_id=3, name='Shimon Shocken', university=university, description='Nice guy',
                              rate=1)
        course1 = Course(1, 'Open Source Code Workshop', False, 'Build a Django project from the grounds up', proffesor)
        test_data = [
            (1, course1),
        ]
        with transaction.atomic():
            for id, course1 in test_data:
                msgboard = MessageBoards(id=id, courseName=course1)
                msgboard.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
