from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Job
# Create your views here.
def index(request):
    job_list = Job.objects.order_by('job_number')
    template = loader.get_template('form/index.html')
    context = RequestContext(request, {
        'job_list': job_list,
    })
    return HttpResponse(template.render(context))

def form(request):
    return render(request, 'form/form.html')

def equation(quantity):
	return 2*quantity+3

def submitted(request):
    if 'name' in request.GET and request.GET['name'] and 'company' in request.GET and request.GET['company'] and 'job_number' in request.GET and request.GET['job_number'] and 'quantity' in request.GET and request.GET['quantity']:
        name = request.GET['name']
        company = request.GET['company']
        job_number = request.GET['job_number']
        quantity = int(request.GET['quantity'])
        newJob = Job(name=name,company=company,job_number=job_number,quantity=quantity,data=equation(quantity))
        newJob.save()
        return HttpResponseRedirect('/')
    else: return HttpResponse('Bad Submission')

def report(request, job_number):
    job = get_object_or_404(Job, job_number=job_number)
    template = loader.get_template('form/report.html')
    context = RequestContext(request, {
        'job_number': job.job_number,
        'name': job.name,
        'company': job.company,
        'data': job.data,
    })
    return HttpResponse(template.render(context))