# Generated by Django 5.0.6 on 2024-09-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(choices=[('Upcoming Departures', 'Upcoming Departures'), ('Sep 2024', 'Sep 2024'), ('Oct 2024', 'Oct 2024'), ('Nov 2024', 'Nov 2024'), ('Dec 2024', 'Dec 2024'), ('Jan 2025', 'Jan 2025'), ('Feb 2025', 'Feb 2025'), ('Mar 2025', 'Mar 2025'), ('Apr 2025', 'Apr 2025'), ('May 2025', 'May 2025'), ('Jun 2025', 'Jun 2025'), ('Jul 2025', 'Jul 2025'), ('Aug 2025', 'Aug 2025'), ('Sep 2025', 'Sep 2025'), ('Oct 2025', 'Oct 2025'), ('Nov 2025', 'Nov 2025'), ('Dec 2025', 'Dec 2025')], default='Upcoming Departures', max_length=20)),
                ('start_day', models.CharField(max_length=20)),
                ('end_day', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('language', models.CharField(choices=[('English', 'English'), ('Nepali', 'Nepali')], default='English', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
