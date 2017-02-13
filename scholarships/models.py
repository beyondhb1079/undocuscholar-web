# Please note that this model is also used by the API

from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from enum import Enum

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

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.value, x.name) for x in cls]

class ScholarshipStatus(ChoiceEnum):
    ARCHIVED = 0
    UNVERIFIED = 1
    VERIFIED = 2

class ScholarshipAmount(int):
    UNKNOWN = 0
    FULL_TUITION = 1

    def __init__(self, val):
        super(ScholarshipAmount, self).__init__()

    @staticmethod
    def unknown():
        if ScholarshipAmount.UNKNOWN is None:
            ScholarshipAmount.UNKNOWN = ScholarshipAmount(0)
        return ScholarshipAmount.UNKNOWN

    @staticmethod
    def full_tuition():
        if ScholarshipAmount.FULL_TUITION is None:
            ScholarshipAmount.FULL_TUITION = ScholarshipAmount((1 << 31) - 1)
        return ScholarshipAmount.FULL_TUITION

    def __str__(self):
        if self == ScholarshipAmount.UNKNOWN:
            return "(Unknown)"
        elif self == ScholarshipAmount.FULL_TUITION:
            return "(Full Tuition)"
        else:
            return "%s" % super(ScholarshipAmount, self).__str__()
    
    def __lt__(self, other):
        if self == ScholarshipAmount.FULL_TUITION:
            return other == ScholarshipAmount.FULL_TUITION
        elif other == ScholarshipAmount.FULL_TUITION:
            return self != ScholarshipAmount.FULL_TUITION
        else:
            return super(ScholarshipAmount, self).__lt__(other)

    def __gt__(self, other): return self != other and not self < other

    def __ge__(self, other): return not self < other

    def __le__(self, other): return self == other or self < other

class ScholarshipAmountField(models.PositiveIntegerField):
    description = "Represents a scholarship amount"

    def __init__(self, *args, **kwargs):
        super(ScholarshipAmountField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return ScholarshipAmount(value)

    def to_python(self, value):
        if isinstance(value, ScholarshipAmount):
            return value

        if value is None:
            return value

        return ScholarshipAmount(value)

@python_2_unicode_compatible
class EligibilityRequirement(models.Model):
    """
    Database model for scholarship eligibility requirements.
    TODO: Better model eligibility requirements

    Future work:
    - Current Education Level: High School, HS Senior, Grad student
    - State: WA, OR, etc.
    - Major: Computer Science, Informatics, Law School, Medical School, etc. (this is tricky)
    - Target Degree Level: Associates, Bachelor's, etc.
    - DACA required?
    - School: University of Washington, etc.
    - Ethnicity: Hispanic/Latino, Asian/Pacific Islander, African American, etc.
    - Nationality: Mexico, Guatemala, etc.
    """
    min_gpa = models.DecimalField(decimal_places=2, max_digits=3)
    daca_required = models.BooleanField(default=False, verbose_name='DACA Required?')
    state = models.CharField(choices=STATE_CHOICES, null=True, max_length=2)

@python_2_unicode_compatible  # only if you need to support Python 2
class Scholarship(models.Model):
    """
    Database model for scholarships.

    Future work:
    - some scholarships have unspecified deadline, what to do about these?
    - other potential scholarship attributes:
      - Award Count: Number of scholarship awards handed out
      - Acceptance Rate: What percent of applicants get the scholarship
      - Scholarship Type: Academic/Community/Organization/Athletic
      - Verifier ID: User ID of the person who verifies a scholarship
      - Date Verified: Date the scholarship was verified

    """
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    amount = ScholarshipAmountField(verbose_name="Award Amount ($)", default=ScholarshipAmount.UNKNOWN,
                                    help_text='Enter the max award amount or 0 for UNKNOWN or 1 for FULL TUITION')
    description = models.TextField(blank=True, help_text='Short description about the scholarship and any additional requirements')
    website = models.URLField(blank=True, help_text='Website URL for full scholarship details')
    status = models.IntegerField(default=1, choices=ScholarshipStatus.choices(), verbose_name='Scholarship Status',
                                 help_text='VERIFIED - Active and verified. '
                                           'UNVERIFIED - Active but not verified. '
                                           'ARCHIVED - Not active.')
    date_created = models.DateTimeField(auto_now_add=True, help_text='The date a scholarship was added to the database')
    date_updated = models.DateTimeField(auto_now=True, help_text='The date a scholarship was last updated')

    def __repr__(self):
        return '%s - <Name %r, Deadline %r, Amount %r>' % (self.id, self.name, self.deadline, self.amount)
    
    def __str__(self):
        return '%s' % (self.name)

    def has_old_deadline(self):
        # Has old deadline if deadline is > 180 days ago and self.active (TODO)
        # TODO: Should we use deadline or date_updated?
        now = timezone.now()
        return now - datetime.timedelta(days=180) <= self.deadline <= now
        
    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
        
    was_updated_recently.admin_order_field = 'date_updated'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'
    
    has_old_deadline.admin_order_field = 'deadline'
    has_old_deadline.boolean = True
    has_old_deadline.short_description = 'Old Deadline? (>180 days)'
