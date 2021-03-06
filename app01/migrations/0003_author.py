# Generated by Django 2.2.12 on 2021-05-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20210507_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='邮箱')),
                ('book', models.ManyToManyField(to='app01.Book', verbose_name='书名')),
            ],
            options={
                'db_table': '作者',
            },
        ),
    ]
