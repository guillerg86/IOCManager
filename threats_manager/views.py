# Activate only on debug
import logging
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .forms import AllowedIPCreateForm, BlockedIPCreateForm
from .models import BlockedIP, AllowedIP
from core.generic_functions import qs_to_array_dict

def threats_manager_home(request):
    # Obtenemos los datos
    # Últimas añadidas a whitelist
    last_excluded_ips = AllowedIP.objects.all().order_by('-created')[:5]
    # Últimas añadidas a blocked
    last_blocked_ips = BlockedIP.objects.all()
    last_blocked_ips = last_blocked_ips.exclude(ip__in=AllowedIP.objects.all().values_list('ip',flat=True))
    last_blocked_ips = last_blocked_ips.order_by('-modified')[:10]

    new_whitelisted_ip_form = AllowedIPCreateForm
    new_blocked_ip_form = BlockedIPCreateForm


    data = {
        'last_whitelisted_ips': last_excluded_ips,
        'last_blocked_ips': last_blocked_ips,
        'new_whitelisted_ip_form': new_whitelisted_ip_form,
        'new_blocked_ip_form':new_blocked_ip_form
    }
    return render(request,'threats_manager/thmg_home.html',data)



def ajax_get_last_allowedips(request):
    try:
        allowed_ips_qs = qs_to_array_dict(get_last_allowedips())
        data = {'result': 'OK', 'last_whitelisted_ips':allowed_ips_qs }
        return JsonResponse(data)
    except Exception as e :
        logging.exception(e)
        data = {'result': 'KO', 'message':'Error while retrieving data'}
        return JsonResponse(data)

def ajax_create_allowedip(request):
    data = {'result': 'KO'}
    if request.method != "POST":
        data['message'] = 'Not a POST request'
        return JsonResponse(data)

    form = AllowedIPCreateForm(request.POST)
    if form.is_valid() == False:
        data['message'] = 'Form is not valid. Check fields.'
        return JsonResponse(data)

    try:
        new_ip = AllowedIP()
        new_ip.ip = form.cleaned_data['ip']
        new_ip.short_description = form.cleaned_data['short_description']
        new_ip.description = form.cleaned_data['description']
        new_ip.save()
        data['result'] = 'OK'
        data['message'] = 'Object saved'
    except:
        data['message'] = 'Unknown error while saving new ip.'
    return JsonResponse(data)

class BlockedIPListView(ListView):
    template_name = 'basetpl.html'
    model = BlockedIP
    paginate_by = 50
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_blockedip_form"] = BlockedIPCreateForm()
        return context


def get_last_allowedips():
    return AllowedIP.objects.all().order_by('-created')[:5]


