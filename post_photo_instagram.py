from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("lupadocidadao", "esaniagro12")
InstagramAPI.login()  # login


photo_path = 'books_read.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)