from InstagramAPI import InstagramAPI
import time

InstagramAPI = InstagramAPI("lupadocidadao", "esaniagro12")

def login():    
    InstagramAPI.login()  

def post(image):
    login()
    
    photo_path = image['imagem']
    caption = image['caption']
    InstagramAPI.uploadPhoto(photo_path, caption=caption)
