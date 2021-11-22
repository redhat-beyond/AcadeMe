from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_university_data(apps, schema_editor):
        from AcadeMeData.models import University

        university_test_data = [
            ('Reichman University', 'Herzliya', 'Very nice university'),
            ('Hebrew University', 'user2@gmail.com', 'Very good university')
        ]
        with transaction.atomic():
            for name, location, description in university_test_data:
                University(name=name, location=location,
                           description=description).save()

    operations = [
        migrations.RunPython(generate_university_data),
    ]
