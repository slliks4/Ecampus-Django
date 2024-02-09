# Generated by Django 4.1.3 on 2022-12-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_portal', '0005_rename_give_name_personal_info_given_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographics_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=50)),
                ('Birthday', models.DateField()),
                ('First_language', models.CharField(max_length=200)),
                ('Country_of_residence', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Demographics_info',
            },
        ),
        migrations.AlterModelOptions(
            name='personal_info',
            options={'verbose_name_plural': 'Personal_info'},
        ),
    ]