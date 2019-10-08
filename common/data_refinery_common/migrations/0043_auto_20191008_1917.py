# Generated by Django 2.1.8 on 2019-10-08 19:17

from django.db import migrations

def update_computed_file_relationship(apps, schema_editor):
    """  """
    ComputedFile = apps.get_model('data_refinery_common', 'ComputedFile')
    OrganismComputedFileAssociation = apps.get_model('data_refinery_common',
                                                     'OrganismComputedFileAssociation')
    computed_files = ComputedFile.objects.filter(compendia_organism__isnull=False).all()
    for computed_file in computed_files:
        OrganismComputedFileAssociation.objects.get_or_create(
            organism=computed_file.compendia_organism,
            computed_file=computed_file
        )

class Migration(migrations.Migration):

    dependencies = [
        ('data_refinery_common', '0042_auto_20191008_1906'),
    ]

    operations = [
        migrations.RunPython(update_computed_file_relationship),
    ]