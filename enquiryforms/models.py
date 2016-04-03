from django.db import models

# Create your models here.
class BasicEnquiryForm(models.Model):
	 enq_date = models.DateField('Enquiry Date')
	 birth_date = models.DateField('Birth Date', null=True)
	 career_choice = models.CharField(max_length=20, null=True)
	 student_fname = models.CharField(max_length=50, null=True)
	 student_mname = models.CharField(max_length=50, null=True)
	 student_lname = models.CharField(max_length=50, null=True)
	 contact_no_primary = models.CharField(max_length=10, null=True)
	 contact_no_home = models.CharField(max_length=10, null=True)
	 contact_email = models.CharField(max_length=100, null=True)
	 address_home = models.CharField(max_length=1000, null=True)
	 father_name = models.CharField(max_length=200, null=True)
	 father_contact_primary = models.CharField(max_length=10, null=True)
	 father_contact_home = models.CharField(max_length=10, null=True)
	 ssc_school = models.CharField(max_length=100, null=True)
	 ssc_classes = models.CharField(max_length=100, null=True)
	 ssc_science = models.CharField(max_length=6, null=True)
	 ssc_maths = models.CharField(max_length=6, null=True)
	 ssc_aggregate = models.CharField(max_length=6, null=True)
	 ssc_percent = models.CharField(max_length=6, null=True)
	 ssc_rollno = models.CharField(max_length=7, null=True)
	 def __str__(self):
		 return (self.student_fname + " - " + self.student_lname + " - " + self.contact_no_primary)
	