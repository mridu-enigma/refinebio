# Generated by Django 2.1.8 on 2019-09-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_refinery_common', '0035_auto_20190919_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='computedfile',
            name='svd_algorithm',
            field=models.CharField(choices=[('NONE', 'None'), ('RANDOMIZED', 'randomized'), ('ARPACK', 'arpack')], default='NONE', help_text='The SVD algorithm that was used to generate the file.', max_length=255),
        ),
        migrations.AddField(
            model_name='dataset',
            name='svd_algorithm',
            field=models.CharField(choices=[('NONE', 'None'), ('RANDOMIZED', 'randomized'), ('ARPACK', 'arpack')], default='NONE', help_text='Specifies choice of SVD algorithm', max_length=255),
        ),
    ]
