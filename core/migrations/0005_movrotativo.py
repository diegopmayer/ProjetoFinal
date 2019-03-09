# Generated by Django 2.1.7 on 2019-03-04 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190304_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovRotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField()),
                ('pago', models.BooleanField(default=False)),
                ('valor_hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parametros')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo')),
            ],
        ),
    ]