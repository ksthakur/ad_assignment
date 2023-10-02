# Generated by Django 4.2.5 on 2023-10-02 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_user', '0002_remove_appusers_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_data', models.CharField(max_length=200)),
                ('search_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_user.appusers')),
            ],
        ),
    ]