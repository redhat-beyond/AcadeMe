from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
        ('AcadeMeData', '0002_User_test_data'),
        ('AcadeMeData', '0003_messageBoards_test_data'),
        ('AcadeMeData', '0004_messages_test_data'),
    ]

    def generate_msgtagsdata(apps, schema_editor):
        from AcadeMeData.models import User, Messages, MessageTags
        userrnd1 = User.create_user('u', 'u@gmail.com', 'pas', 'BS', 'CS')
        msgID = Messages.create_message(1, userrnd1, 'Hello this is test message')
        test_data = [
            (1, msgID, userrnd1),
        ]
        with transaction.atomic():
            for id, msgID, userID in test_data:
                msgTag = MessageTags(id=id, msg=msgID, userID=userID)
                msgTag.save()

    operations = [
        migrations.RunPython(generate_msgtagsdata),
    ]
