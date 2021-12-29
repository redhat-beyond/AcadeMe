from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
        ('AcadeMeData', '0002_User_test_data'),
        ('AcadeMeData', '0003_messageBoards_test_data'),
    ]

    def generate_msgdata(apps, schema_editor):
        from AcadeMeData.models import Messages, User, MessageBoards
        userrnd1 = User.create_user('name', 'email', 'pass', 'kaki', 'cs')
        board = MessageBoards.get_msgboard_by_id(1)
        test_data = [
            (1, userrnd1, 'random message', board),
        ]
        with transaction.atomic():
            for msgID, userID, text, board in test_data:
                msg = Messages(msgID=msgID, userID=userID, text=text, board=board)
                msg.save()

    operations = [
        migrations.RunPython(generate_msgdata),
    ]
