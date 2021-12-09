from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_user_data(apps, schema_editor):
        from AcadeMeData.models import User
        # from django.contrib.auth.models import User as djangoUser

        user_test_data = [
            ('user5', 'user1@gmail.com', 'password1', 'BS', 'CS'),
            ('user6', 'user2@gmail.com', 'Password2', 'RU', 'PS'),
            ('user7', 'user3@gmail.com', 'Password3', 'TA', 'BA'),
            ('user8', 'user4@gmail.com', 'Password4', 'BS', 'CD')
        ]
        with transaction.atomic():
            for username, email, password, university, degree in user_test_data:
                User.create_user(username, email, password, university, degree)

    operations = [
        migrations.RunPython(generate_user_data),
    ]
