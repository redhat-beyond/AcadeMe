from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_professor_data(apps, schema_editor):
        from AcadeMeData.models import Professor, University
        uni = University(university_id=5, name="Reichman University", location='Herzliya',
                         description='Very nice university').save()
        professor_test_data = [
            (1, 'alison', uni, 'Very nice guy', '4'),
            (2, 'ronald', uni, 'terrible person', '1'),
        ]
        with transaction.atomic():
            for professor_id, name, uni, description, rate in professor_test_data:
                Professor.create_professor(professor_id, name, uni, description, rate)

    operations = [
        migrations.RunPython(generate_professor_data),
    ]
