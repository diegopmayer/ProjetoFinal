# Generated by Django 2.1.7 on 2019-03-05 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_mensalista'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pgto', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mensalista')),
            ],
        ),
    ]
