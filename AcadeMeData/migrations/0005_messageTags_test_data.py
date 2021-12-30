from django.db import migrations, transaction

from AcadeMeData.models import MessageBoards


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
        ('AcadeMeData', '0002_User_test_data'),
        ('AcadeMeData', '0003_messageBoards_test_data'),
        ('AcadeMeData', '0004_messages_test_data'),
    ]

    def generate_msgtagsdata(apps, schema_editor):
        from AcadeMeData.models import User, Messages, MessageTags, University, Professor, Course
        userrnd1 = User.create_user('u', 'u@gmail.com', 'pas', 'BS', 'CS')
        university = University(university_id=1, name='Reichman University', location='Herzliya',
                                description='Very nice university')
        professor = Professor(professor_id=3, name="Shimon Shocken", university=university, description="Nice guy",
                              rate=1)
        course = Course(1, 'Open Source Code Workshop', False, 'Build a Django project from the grounds up!', professor)
        board = MessageBoards(id=1, courseName=course)
        msgID = Messages.create_message(1, userrnd1, 'Hello this is test message', board)
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
