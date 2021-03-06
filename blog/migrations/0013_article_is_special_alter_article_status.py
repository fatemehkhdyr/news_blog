# Generated by Django 4.0 on 2022-01-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_special',
            field=models.BooleanField(default=True, verbose_name='آیا مقاله ویژه است ؟'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], default='d', max_length=1, verbose_name='وضعیت'),
        ),
    ]
