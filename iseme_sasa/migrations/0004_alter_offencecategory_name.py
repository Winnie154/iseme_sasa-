# Generated by Django 4.1.1 on 2022-10-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iseme_sasa', '0003_policeprofileimageupload_trackstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offencecategory',
            name='name',
            field=models.CharField(help_text='Select a category (EG: Sexual Assault)', max_length=200),
        ),
    ]
