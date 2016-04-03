#from django.shortcuts import render

# Create your views here.

from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import BasicEnquiryForm

def index(request):
	print('execute index..')
	return render(request, 'enquiryforms/index.html')	
	
#def detail(request, form_id):
 #   return HttpResponse("You're looking at Details of Form # %s." % form_id)

def confirm(request):
	print('execute confirm..')
	return render(request, 'enquiryforms/confirm.html')	
	
def info(request, contact_no):
    response = "You're looking at the results of contact # %s."
    return HttpResponse(response % contact_no)

def save_data(request):
	print('Student Fname:', request.POST['student_fname'])	
	f1 = BasicEnquiryForm(enq_date = timezone.now(),
	career_choice = request.POST['career_choice'],
	student_fname = request.POST['student_fname'],
	student_mname = request.POST['student_mname'],
	student_lname = request.POST['student_lname'],
	contact_no_primary = request.POST['contact_no_primary'],
	contact_no_home = request.POST['contact_no_home'],
	contact_email = request.POST['contact_email'],
	address_home = request.POST['address_home'],
	father_name = request.POST['father_name'],
	father_contact_primary = request.POST['father_contact_primary'],
	father_contact_home = request.POST['father_contact_home'],
	ssc_school = request.POST['ssc_school'],
	ssc_classes = request.POST['ssc_classes'],
	ssc_science = request.POST['ssc_science'],
	ssc_maths = request.POST['ssc_maths'],
	ssc_aggregate = request.POST['ssc_aggregate'],	
	birth_date = request.POST['birth_date'],
	ssc_rollno = request.POST['ssc_rollno']
	)
	f1.save()		
	return render(request, 'enquiryforms/confirm.html')	
	
"""    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
"""		