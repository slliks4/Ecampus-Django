# Generated by Django 4.1.3 on 2022-12-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_portal', '0007_delete_demographics_info_personal_info_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='Kin_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='Kin_city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='Kin_family_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='Kin_given_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='Kin_information_authorization',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='Kin_middle_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='City',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Family_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Given_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Middle_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Preffered_family_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Preffered_first_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]