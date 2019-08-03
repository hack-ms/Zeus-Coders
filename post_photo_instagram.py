from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("lupadocidadao", "esaniagro12")
InstagramAPI.login()  # login


photo_path = 'images/colors.jpg'
caption = "Sample photo teste"
InstagramAPI.uploadPhoto(photo_path, caption=caption)