from django.db import migrations, transaction

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
        
    ]

    def generate_data(apps, schema_editor):
        from AcadeMeData.models import Degree

        test_data = [
        (1, 'Computer Science', 'Recihman University, Ben Gurion University, Tel Aviv University',
         'A degree in Computer Science offers the tools to succeed in todays technology driven world'),
        (0, 'History', 'Hebrew University, Afeka College',
         'A degree in History offers students a broad understanding of historical events'),
        ]
        with transaction.atomic():
            for id, name, universities, description in test_data:
                Degree(degree_id=id, name=name, universities=universities, description=description).save()

    operations = [
        migrations.RunPython(generate_data),
    ]