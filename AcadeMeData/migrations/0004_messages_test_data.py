from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]

    def generate_msgdata(apps, schema_editor):
        from AcadeMeData.models import Messages, User
        userrnd1= User.create_user('name','email','pass', 's','kaki','cs')
        test_data = [
            (1, userrnd1, 'random message'),
        ]
        with transaction.atomic():
            for msgID, userID, text in test_data:
                msg=Messages(msgID=msgID, userID=userID, text=text)
                msg.save()

    operations = [
        migrations.RunPython(generate_msgdata),
    ]
