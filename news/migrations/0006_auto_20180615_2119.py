# Generated by Django 2.0.5 on 2018-06-15 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180615_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='img',
            options={'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='news.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='post',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.CharField(max_length=120, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
