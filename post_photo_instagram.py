from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("lupadocidadao", "esaniagro12")
InstagramAPI.login()  # login


photo_path = 'images/books_read.jpg'
caption = "Sample photo teste"
InstagramAPI.uploadPhoto(photo_path, caption=caption)