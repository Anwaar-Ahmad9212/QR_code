import qrcode
from PIL import Image, ImageDraw,ImageFont



linkedin = qrcode.make("https://www.linkedin.com/in/muhammad-anwaar-ahmad/")
linkedin.save("linkedin.png")


url_whatsapp = "https://api.whatsapp.com/send/?phone=923478661176&text=Asslamoalaikum%2C%0A+My+name+is+%5B%5D+.%0A+We+met+at+%5B%5D.+%0A+I+just+wanted+to+say+you+that%3A&type=phone_number&app_absent=0"
whatsapp = qrcode.make(url_whatsapp)
whatsapp.save("whatsapp.png")


instagram = qrcode.make("https://www.instagram.com/me_anwaarahmad/profilecard/?igsh=OG43bW9yajF5MDY5" )
instagram.save("instagram.png")
