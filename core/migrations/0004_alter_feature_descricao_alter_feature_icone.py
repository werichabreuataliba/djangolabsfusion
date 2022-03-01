# Generated by Django 4.0.2 on 2022-02-28 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Laptop')], max_length=18, verbose_name='Icone'),
        ),
    ]
