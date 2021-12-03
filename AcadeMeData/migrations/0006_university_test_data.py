from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('AcadeMeData', '0002_User_test_data'),
    ]

    def generate_university_data(apps, schema_editor):
        from AcadeMeData.models import University

        university_test_data = [
            ('Reichman University', 'Herzliya', 'Very nice university'),
            ('Hebrew University', 'Jerusalem', 'Very good university')
        ]
        with transaction.atomic():
            for name, location, description in university_test_data:
                University(name=name, location=location,
                           description=description).save()

    operations = [
        migrations.RunPython(generate_university_data),
    ]
