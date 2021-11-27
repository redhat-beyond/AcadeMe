from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]



    def generate_msgdata(apps, schema_editor):
        from AcadeMeData.models import Messages, User
        user_test_data = [
            ('user51', 'user1@gmail.com', 'password1', 'S', 'BS', 'CS'),
            ('user61', 'user2@gmail.com', 'Password2', 'E', 'RU', 'PS'),
            ('user71', 'user3@gmail.com', 'Password3', 'S', 'TA', 'BA'),
            ('user81', 'user4@gmail.com', 'Password4', 'E', 'BS', 'CD')
        ]
        with transaction.atomic():
            for username, email, password, type, university, degree in user_test_data:
                User.create_user(username, email, password, type, university, degree)
        userrnd1=User.objects.get(user=5)
        userrnd2=User.objects.get(user=6)
        test_data = [
            (1, userrnd1, 'random message'),
            (2, userrnd2, 'random message2'),
        ]
        with transaction.atomic():
            for msgID, userID, text in test_data:
                Messages(msgID=msgID, userID=userID, text=text).save()

    operations = [
        migrations.RunPython(generate_msgdata),
    ]
