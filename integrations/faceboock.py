#urllib_parse_urlparse.py
# 
import matplotlib.pyplot as plt
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import parse_qs
import datetime
import facebook
import subprocess
import warnings
import numpy as np
import time

# codigo da pagina no facebook
page_id = "101829217838141"
# token de acesso
token_access = "EAAF2nd2XYr0BACRZBPo3G0ZBqBCtZBxb0P6p1S8ZB7CZBA4Jip8oksbrSyngPB4MFdFZBgRwEtBkYFGOpLTxZAU9EFZCHNmKsCiP5gJc9ZCXHQelK5TFgk5uvff18F73y35fqOuxplfVZA9l5YWmfG4WDqRuX0dKYO2WAMm6gAPbybJgZDZD"

def post(image):    
    now = datetime.datetime.now()
    msg = image['caption']
    graph = facebook.GraphAPI(token_access)

    try:
        result_photo = graph.put_photo(image=open(image['imagem'], 'rb'),album_path=page_id + "/photos")
        result = graph.put_object(page_id, "feed", message= msg, object_attachment = result_photo['id'])
        id_publicacao = result['id']   
        print('Publicação efetuada com sucesso.')
    except KeyError:
        print('erro ao realizar o post!')
        exit()

    feed = graph.get_connections("me", "feed")
    post = feed["data"]

       
