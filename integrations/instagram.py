from InstagramAPI import InstagramAPI
import time

InstagramAPI = InstagramAPI("lupadocidadao", "esaniagro12")

def login():    
    InstagramAPI.login()  

def post(images):
    login()

    for img in images:
        photo_path = img['imagem']
        caption = img['caption']
        InstagramAPI.uploadPhoto(photo_path, caption=caption)
        time.sleep(2)