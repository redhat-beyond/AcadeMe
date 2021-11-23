from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from AcadeMeData.models import Degree

        test_data = [
            ('Computer Science', 'Recihman University',
                'A degree in Computer Science offers the tools to succeed in todays technology driven world'),
            ('History', 'Hebrew University, Afeka College',
                'A degree in History offers students a broad understanding of historical events'),
        ]
        with transaction.atomic():
            for degree, universities, description in test_data:
                Degree(degree=degree, universities=universities, description=description).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
