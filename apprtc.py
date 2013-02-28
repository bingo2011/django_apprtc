import json
import random

def generate_random(len):
    word = ''
    for i in range(len):
        word += random.choice('0123456789')
    return word

def make_pc_config(stun_server, turn_server, ts_pwd):
    servers = []
    if turn_server:
        turn_config = 'turn:{}'.format(turn_server)
        servers.append({'url':turn_config, 'credential':ts_pwd})
    if stun_server:
        stun_config = 'stun:{}'.format(stun_server)
    else:
        stun_config = 'stun:' + 'stun.l.google.com:19302'
    servers.append({'url':stun_config})
    return {'iceServers':servers}

def make_pc_constraints(compat):
    constraints = { 'optional': [] }
    # For interop with FireFox. Enable DTLS in peerConnection ctor.
    if compat.lower() == 'true':
        constraints['optional'].append({'DtlsSrtpKeyAgreement': True})
    return constraints

def make_offer_constraints(compat):
    constraints = { 'mandatory': {}, 'optional': [] }
    # For interop with FireFox. Disable Data Channel in createOffer.
    if compat.lower() == 'true':
        constraints['mandatory']['MozDontOfferDataChannel'] = True
    return constraints

def make_media_constraints(hd_video):
    constraints = { 'optional': [], 'mandatory': {} }
    # Demo 16:9 video with media constraints.
    if hd_video.lower() == 'true':
        # Demo with WHD by setting size with 1280x720.
        constraints['mandatory']['minHeight'] = 720
        constraints['mandatory']['minWidth'] = 1280
        # Disabled for now due to weird stretching behavior on Mac.
    #else:
        # Demo with WVGA by setting Aspect Ration;
        #constraints['mandatory']['maxAspectRatio'] = 1.778
        #constraints['mandatory']['minAspectRatio'] = 1.777
    return constraints
