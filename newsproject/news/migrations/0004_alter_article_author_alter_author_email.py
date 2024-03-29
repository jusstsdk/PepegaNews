# Generated by Django 4.0.4 on 2022-05-30 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_author_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
