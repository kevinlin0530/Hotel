# Generated by Django 4.2.2 on 2023-08-01 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
        ('owner', '0002_alter_owner_owner_name'),
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='Agent_name',
            new_name='agent_name',
        ),
        migrations.AlterField(
            model_name='agent',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='hotel.hotel', to_field='hotel_name'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='owner.owner', to_field='owner_name'),
        ),
    ]
