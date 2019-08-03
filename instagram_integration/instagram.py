from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("lupadocidadao", "esaniagro12")

def login():    
    InstagramAPI.login()  

def post(path_imagem, caption):
    login()
       
    photo_path = path_imagem
    caption = caption
    InstagramAPI.uploadPhoto(photo_path, caption=caption)