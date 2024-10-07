# Generated by Django 5.1 on 2024-10-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_linck_name_headertext_link_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=55, null=True)),
                ('link_name', models.CharField(blank=True, max_length=55, null=True)),
            ],
            options={
                'verbose_name': 'Main Block',
                'verbose_name_plural': 'Main Block',
            },
        ),
        migrations.AddField(
            model_name='headertext',
            name='class_image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='headertext',
            name='class_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='headertext',
            name='class_item',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
