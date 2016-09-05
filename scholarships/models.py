# Please note that this model is also used by the API

from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# TODO: Figure out how to store these choices
STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    ('DC', 'Washington DC'),
)

SCHOOL_YEAR_CHOICES = (
    ('HS', 'High School'),
    ('HS1', 'High School Freshman'),
    ('HS2', 'High School Sophomore'),
    ('HS3', 'High School Junior'),
    ('HS4', 'High School Senior'),
    ('UG', 'College Freshman'),
    ('UG1', 'College Freshman'),
    ('UG2', 'College Sophomore'),
    ('UG3', 'College Junior'),
    ('UG4', 'College Senior'),
)

@python_2_unicode_compatible  # only if you need to support Python 2
class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    amount = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    count = models.PositiveIntegerField(null=True, verbose_name="Number of Awards (blank if unknown)")
    archived = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    # TODO: Connect each scholarship to a particular user who owns/verifies it
    # verifier = models.ForeignKey('auth.User', related_name='scholarships')
    
    # Eligibility fields. Should this be another table of its own? YES
    # min_gpa = models.DecimalField(decimal_places=2, max_digits=3)
    # education = models.CharField() # SplitArrayField()
    # state = models.CharField(choices=STATE_CHOICES) 
    # major = models.CharField(blank=True)
    # degree_level = models.CharField(blank=True)
    # daca_only = models.BooleanField()
    # school = models.CharField(blank=True)
    # race = models.CharField()
    # nationality = models.CharField()

    def __repr__(self):
        return '%s - <Name %r, Deadline %r, Amount %r>' % (self.id, self.name, self.deadline, self.amount)
    
    def __str__(self):
        return '%s' % (self.name)
        
    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
        
    was_updated_recently.admin_order_field = 'date_updated'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'
