from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_api', '0006_alter_output_input'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(default='84062', max_length=255)),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
