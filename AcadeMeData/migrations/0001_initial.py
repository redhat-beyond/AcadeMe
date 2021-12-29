import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(default=0, primary_key=True, serialize=False,
                                                  validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100, unique=True)),
                ('mandatory', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('degree_id', models.IntegerField(default=0, primary_key=True, serialize=False,
                                                  validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100)),
                ('universities', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageBoards',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('courseName', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE,
                                                 to='AcadeMeData.course')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('msgID', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=300)),
                ('msgDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('board', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                            to='AcadeMeData.messageboards')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.IntegerField(primary_key=True, serialize=False,
                                                      validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='auth.user')),
                ('university', models.CharField(
                    choices=[('RU', 'Reichman University'), ('HU', 'Hebrew University'), ('TA', 'Tel Aviv University'),
                             ('BS', "Be'er Sheva University"), ('UN', 'Unknown')], default='UN', max_length=2)),
                ('degree', models.CharField(
                    choices=[('CS', 'Computer Science'), ('PS', 'Psychology'), ('GV', 'Government'),
                             ('BA', 'Business Administration'), ('UN', 'Unknown')], default='UN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('professor_id', models.IntegerField(primary_key=True, serialize=False,
                                                     validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True,
                                             validators=[django.core.validators.MinValueValidator(1),
                                                         django.core.validators.MaxValueValidator(5)])),
                ('university',
                 models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='AcadeMeData.university')),
            ],
        ),
        migrations.CreateModel(
            name='MessageTags',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('msg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcadeMeData.messages')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcadeMeData.user')),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='userID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='AcadeMeData.user'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.ManyToManyField(to='AcadeMeData.Degree'),
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='AcadeMeData.professor'),
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='AcadeMeData.university'),
        ),
    ]
