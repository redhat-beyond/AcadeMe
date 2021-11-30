from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('professor', '0001_initial'),
    ]

    def generate_professor_data(apps, schema_editor):
        from professor.models import Professor, University
        university = University(university_id=5, name="Reichman University", location='Herzliya',
                                description='Very nice university')
        university.save()
        professor_test_data = [
            (1, 'alison', university, 'Very nice guy', '4'),
            (2, 'ronald', university, 'terrible person', '1'),
        ]
        with transaction.atomic():
            for professor_id, name, uni, description, rate in professor_test_data:
                Professor.create_professor(professor_id, name, uni, description, rate)

    operations = [
        migrations.RunPython(generate_professor_data),
    ]
