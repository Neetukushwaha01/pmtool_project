# Generated by Django 4.1.7 on 2023-04-11 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_projectattachment_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ViedoProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_title', models.TextField()),
                ('project_description', models.TextField()),
                ('Loom_Videolink', models.URLField()),
                ('Attachment_viedo', models.FileField(upload_to='files/upload')),
                ('type_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.requesttypes')),
            ],
        ),
    ]
