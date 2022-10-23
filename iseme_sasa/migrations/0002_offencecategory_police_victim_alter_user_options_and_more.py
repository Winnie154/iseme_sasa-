# Generated by Django 4.1.1 on 2022-10-19 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iseme_sasa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffenceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Select a category (EG: Domestic violence)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='police', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('police_id', models.FloatField(blank=True, max_length=50, null=True)),
                ('station_number', models.FloatField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='victim', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.CharField(max_length=100)),
                ('social_status', models.CharField(max_length=5000)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AddField(
            model_name='report',
            name='perpetrator_first_name',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='perpetrator_gender',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='perpetrator_last_name',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='perpetrator_name',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('victim', 'victim'), ('police', 'police')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='VictimImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vendor_img_uploads')),
                ('caption', models.CharField(max_length=500)),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='victim_image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='police_img_uploads')),
                ('caption', models.CharField(max_length=500)),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='police_image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offence_title', models.CharField(max_length=100)),
                ('datetime', models.DateField(max_length=5000)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('category', models.ForeignKey(help_text='Select the type of offence.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='iseme_sasa.offencecategory')),
            ],
        ),
    ]
