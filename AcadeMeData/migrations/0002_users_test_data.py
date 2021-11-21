from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_user_data(apps, schema_editor):
        from AcadeMeData.models import Users
        from django.contrib.auth.models import User

        user_test_data = [
            ('user1', 'user1@gmail.com', 'password1'),
            ('User2', 'user2@gmail.com', 'Password2'),
            ('User3', 'user3@gmail.com', 'Password3'),
            ('user4', 'user4@gmail.com', 'Password4')
        ]
        with transaction.atomic():
            for username, email, password in user_test_data:
                user = User.objects.create_user(username=username, email=email, password=password)
                Users(user=user).save()

    operations = [
        migrations.RunPython(generate_user_data),
    ]
