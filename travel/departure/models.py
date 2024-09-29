from django.db import models

class Departure(models.Model):
    DEPARTURE_CHOICES = [
        ('Upcoming Departures', 'Upcoming Departures'),
        ('Sep 2024', 'Sep 2024'),
        ('Oct 2024', 'Oct 2024'),
        ('Nov 2024', 'Nov 2024'),
        ('Dec 2024', 'Dec 2024'),
        ('Jan 2025', 'Jan 2025'),
        ('Feb 2025', 'Feb 2025'),
        ('Mar 2025', 'Mar 2025'),
        ('Apr 2025', 'Apr 2025'),
        ('May 2025', 'May 2025'),
        ('Jun 2025', 'Jun 2025'),
        ('Jul 2025', 'Jul 2025'),
        ('Aug 2025', 'Aug 2025'),
        ('Sep 2025', 'Sep 2025'),
        ('Oct 2025', 'Oct 2025'),
        ('Nov 2025', 'Nov 2025'),
        ('Dec 2025', 'Dec 2025'),
    ]

    LANGUAGES_CHOICES = [
        ('English', 'English'),
        ('Nepali', 'Nepali'),
    ]

    departure = models.CharField(
        max_length=20,
        choices=DEPARTURE_CHOICES,
        default='Upcoming Departures'
    )
    start_day = models.CharField(max_length=20)
    end_day = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    language = models.CharField(
        max_length=20,
        choices=LANGUAGES_CHOICES,
        default='English'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    parent_departure = models.ForeignKey(
        'self',  
        null=True,  
        blank=True,  
        related_name='children', 
        on_delete=models.CASCADE 
    )

    def __str__(self):
        return self.departure
