from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.contrib.auth.decorators import login_required

from ncpp.forms import ClimateIndexesForm1, ClimateIndexesForm2, ClimateIndexesForm3
from ncpp.views import ClimateIndexesWizard


urlpatterns = patterns('',
    
    # top-level url
    url(r'^$', 'django.views.generic.simple.redirect_to', { 'url': '/ncpp/climate_indexes/'}, name='home' ),
    
    # climate indexes use case
    # note use of 'login_required' decorator directly in URL configuration
    url(r'^climate_indexes/$', login_required(ClimateIndexesWizard.as_view([ClimateIndexesForm1, ClimateIndexesForm2, ClimateIndexesForm3])), name='climate_indexes' ),
        
    # user jobs listing
    url(r'^jobs/(?P<username>.+)/$', 'ncpp.views.jobs_list', name='jobs_list' ),
    
    # job display pages
    url(r'^job/request/(?P<job_id>.+)/$', 'ncpp.views.job_request', name='job_request' ),
    url(r'^job/response/(?P<job_id>.+)/$', 'ncpp.views.job_response', name='job_response' ),
    url(r'^job/check/(?P<job_id>.+)/$', 'ncpp.views.job_check', name='job_check' ),
    url(r'^job/(?P<job_id>.+)/$', 'ncpp.views.job_detail', name='job_detail' ),
    
    # login/logout using django default authentication views and templates
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/ncpp/login/'}, name='logout'),

)