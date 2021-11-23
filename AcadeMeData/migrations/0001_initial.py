# Generated by Django 3.2.8 on 2021-11-23 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('universities', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              primary_key=True, serialize=False, to='auth.user')),
                ('type', models.CharField(
                    choices=[('S', 'Student'), ('E', 'Expert')], default='S', max_length=1)),
                ('university', models.CharField(choices=[
                    ('RU', 'Reichman University'), ('HU', 'Hebrew University'), ('TA', 'Tel Aviv University'),
                    ('BS', "Be'er Sheva University"), ('UN', 'Unknown')], default='UN', max_length=2)),
                ('degree', models.CharField(choices=[
                    ('CS', 'Computer Science'), ('PS', 'Psychology'), ('GV', 'Government'),
                    ('BA', 'Business Administration'), ('UN', 'Unknown')], default='UN', max_length=2)),
            ],
        ),
    ]
