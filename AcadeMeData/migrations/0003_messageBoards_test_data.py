from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from AcadeMeData.models import MessageBoards
        test_data = [
            (1, 'Linear Algebra'),
            (2, 'Algorithms'),
        ]
        with transaction.atomic():
            for id, text in test_data:
                MessageBoards(id=id, courseName=text).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
