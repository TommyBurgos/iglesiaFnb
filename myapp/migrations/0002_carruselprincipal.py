# Generated by Django 4.2.16 on 2024-11-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarruselPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='carrusel/default.jpg', upload_to='carrusel/')),
                ('titulo1', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]
