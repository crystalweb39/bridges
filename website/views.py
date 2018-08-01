# Create your views here.
from bridges.website.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from bridges.common import *
from bridges.website.forms import *

def home(request):
    t = loader.get_template('index.html')
    people = People.objects.all()
    services = Service.objects.all()[:12]
    banners = ImageSlider.objects.all()
    msg = ''
    rp = request.POST
    if rp:
        form = EnquiryForm(rp)
        if form.is_valid():
            form.save()
            msg = 'success'
            form = EnquiryForm()
        else:
            msg = 'error'
        
    else:
        form = EnquiryForm()
    
    c = RequestContext(request, commondict({
            'people':people,
            'services':services,
            'form':form,
            'msg':msg,
            
            'banners':banners,
            
    },request))
    
    return HttpResponse(t.render(c))


def page(request,path):
    page = MiscPage.objects.get(slug=path)
    t = loader.get_template('page.html')
    c = RequestContext(request, commondict({
                                            
        'page':page,
    },request))
    
    return HttpResponse(t.render(c))