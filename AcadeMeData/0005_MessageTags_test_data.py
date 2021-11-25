from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '__latest__'),
        ('AcadeMeData', '0001_initial'),
    ]


    def generate_msgtagsdata(apps, schema_editor):
        from AcadeMeData.models import MessageTags, User, Messages
        userrnd1=User.objects.get(user=5)
        userrnd2=User.objects.get(user=6)
        test_data = [
            (1, userrnd1 ),
            (2, userrnd2),
        ]
        with transaction.atomic():
            for id, userID in test_data:
                MessageTags(id=id, userID=userID).save()

    operations = [
        migrations.RunPython(generate_msgtagsdata),
    ]
