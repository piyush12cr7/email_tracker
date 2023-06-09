# Generated by Django 4.2.1 on 2023-06-02 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('opened', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_app.email')),
            ],
        ),
    ]
