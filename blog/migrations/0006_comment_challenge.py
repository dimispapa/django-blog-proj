# Generated by Django 4.2.15 on 2024-08-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(null=True),
        ),
    ]
