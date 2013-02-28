# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from apprtc import *

def mainpage(request):
    room_key = '1111'
    initiator = 1

    base_url = request.build_absolute_uri()
    room_link = base_url + '?r=' + room_key;
    token = 1
    user = generate_random(8)

    pc_config = make_pc_config('', '', '')
    pc_constraints = make_pc_constraints('')
    offer_constraints = make_offer_constraints('')
    media_constraints = make_media_constraints('')

    template_values = {'token': token,
        'me': user,
        'room_key': room_key,
        'room_link': room_link,
        'initiator': initiator,
        'pc_config': json.dumps(pc_config),
        'pc_constraints': json.dumps(pc_constraints),
        'offer_constraints': json.dumps(offer_constraints),
        'media_constraints': json.dumps(media_constraints),
    }

    return render_to_response('index.html', template_values, context_instance=RequestContext(request))

def handle_message(request):
    import pdb; pdb.set_trace()

    print request.POST
