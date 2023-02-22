from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import validators
import qrcode

#main frame
root=Tk()
root.title("QR Generator")
root.geometry("1000x600+250+100")
root.config(bg="#C52233")
root.resizable(False,False)
card=Image.open('temp/tempqr.png').resize((200,200),Image.ANTIALIAS)
def generate():
    name=title.get()
    text=content.get()
    global card
    if(name.strip()!="" and text.strip()!=""):
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
                card=Image.open('yt_card.png')
                logo = Image.open('yt.png')
                # taking base width
                basewidth = 80
                # adding color to QR code
                img = qr.make_image(fill_color="#d4101d", back_color="white").convert('RGB')

            
            elif(text.find("instagram.com")!=-1):   #instagram
                card=Image.open('insta_card.png')
                logo = Image.open('insta.png')
                basewidth = 80
                img = qr.make_image(fill_color="#FD2266", back_color="white").convert('RGB')
            
            elif(text.find("facebook.com")!=-1):   #Facebook
                card=Image.open('fb_card.png')
                logo = Image.open('fb.png')
                basewidth = 80
                img = qr.make_image(fill_color="#1878F3", back_color="white").convert('RGB')

            elif(text.find("twitter.com")!=-1):   #Twitter
                card=Image.open('twitter_card.png')
                logo = Image.open('twitter.png')
                basewidth = 80
                img = qr.make_image(fill_color="#2DAAE1", back_color="white").convert('RGB')

            else:   #Other Websites
                card=Image.open('web_card.png')
                logo = Image.open('web.png')
                basewidth = 80
                img = qr.make_image(fill_color="#167ABC", back_color="white").convert('RGB')

        elif(validators.email(text)):   #Email Address
            card=Image.open('email_card.png')
            logo = Image.open('email.png')
            basewidth = 80
            img = qr.make_image(fill_color="#B42119", back_color="white").convert('RGB')
        
        else:
            card=Image.open('info_card.png')
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
        img.save("temp/tempqr.png")

        #Creating Card by merging generated qr and card templet
        code=Image.open('temp/tempqr.png').resize((200,200),Image.ANTIALIAS)
        card.paste(code,(75,200))
        card=card.resize((230,400),Image.ANTIALIAS)
        card.save("temp/tempcard.png")

        tempqr=PhotoImage(file="temp/tempcard.png")
        img_view.config(image=tempqr)

        btn1.config(stat=NORMAL)
        
    else:
        messagebox.showerror("Invalid Input","Please Fill all fields correctly")
#Function to save image
def saveas():    
    card.save("generated/"+title.get()+".png")

    # file=filedialog.asksaveasfile(defaultextension='.png',
    # filetypes=[
    #     ("JPEG file",".jpeg"),
    #     ("JPG file",".jpg"),
    #     ("PNG file",".png"),
    #     ])
    # # card.save(file)
    # # file.close()
    # file = filedialog.asksaveasfile(mode='w', defaultextension=".png")
    # if file:
    #     card.save(file)
    # files = [('All Files', '*.*'), 
    #          ('Python Files', '*.py'),
    #          ('Text Document', '*.txt')]
    # file = asksaveasfile(filetypes = files, defaultextension = files)

#label
l1=Label(root,text="QR Code Generator",fg="white",bg="#C52233",font=30)
l1.place(x=45,y=60)
l1.config(font=('Arial bold',40))
#label
Label(root,text="Title",fg="white",bg="#C52233",font=20).place(x=50,y=170)

#Entry
title=Entry(root,width=15,font="arial 15")
title.place(x=50,y=200)

#label
Label(root,text="Content",fg="white",bg="#C52233",font=20).place(x=50,y=240)

#Entry
content=Entry(root,width="30",text="Content",font="arial 15")
content.place(x=50,y=270)

#Button
Button(root, text = " Generate " ,width=20,height=2,fg="white",bg="black", command=generate ).place(x=50,y=340)

#ImageView
img_view=Label(root,bg="#C52233")
img_view.pack(padx=130,pady=0,side=RIGHT)

#Button
btn1=Button(root,text="Download",width=20,height=2,fg="white",bg="black", command=saveas , state=DISABLED)
btn1.place(x=250,y=340)

root.mainloop()