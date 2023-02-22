from tkinter import *
from PIL import Image
import validators
import qrcode

#main frame
root=Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#C52233")
root.resizable(False,False)

def generate():
    name=title.get()
    text=content.get()
    # generating qr code using qrcode 
    
    
    
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    # adding URL or text to QRcode
    qr.add_data(text)
    # generating QR code
    qr.make(fit=True)

    if(validators.url(text)):               #Valid Url
        if(text.find("youtube.com")!=-1):   #Youtube
            logo = Image.open('yt.png')
            # taking base width
            basewidth = 80
            # adding color to QR code
            img = qr.make_image(fill_color="#d4101d", back_color="white").convert('RGB')
        
        elif(text.find("instagram.com")!=-1):   #instagram
            logo = Image.open('insta.png')
            basewidth = 80
            img = qr.make_image(fill_color="#FD2266", back_color="white").convert('RGB')
        
        elif(text.find("facebook.com")!=-1):   #Facebook
            logo = Image.open('fb.png')
            basewidth = 80
            img = qr.make_image(fill_color="#1878F3", back_color="white").convert('RGB')

        elif(text.find("twitter.com")!=-1):   #Twitter
            logo = Image.open('twitter.png')
            basewidth = 80
            img = qr.make_image(fill_color="#2DAAE1", back_color="white").convert('RGB')

        else:   #Other Websites
            logo = Image.open('web.png')
            basewidth = 80
            img = qr.make_image(fill_color="#167ABC", back_color="white").convert('RGB')

    elif(validators.email(text)):   #Email Address
        logo = Image.open('email.png')
        basewidth = 80
        img = qr.make_image(fill_color="#B42119", back_color="white").convert('RGB')
    
    else:
        logo = Image.open('info.png')
        basewidth = 80
        img = qr.make_image(fill_color="#008375", back_color="white").convert('RGB')
        
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    #set size of QR code
    pos = ((img.size[0] - logo.size[0]) // 2,(img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    # save the QR code generated
    img.save("generated/"+str(name)+".png")


#label
Label(root,text="Title",fg="white",bg="#C52233",font=20).place(x=50,y=170)

#Entry
title=Entry(root,width=15,font="arial 15")
title.place(x=50,y=200)

#label
Label(root,text="Content",fg="white",bg="#C52223",font=20).place(x=50,y=240)

#Entry
content=Entry(root,width="15",text="Content",font="arial 15")
content.place(x=50,y=270)

#Button
Button(root, text = " Generate " ,width=20,height=2,fg="white",bg="black", command=generate ).place(x=50,y=320)

root.mainloop()