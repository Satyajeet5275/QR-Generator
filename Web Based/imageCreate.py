from PIL import Image
card=Image.open('yt_card.png')
code=Image.open('generated/Youtube.png').resize((200,200),Image.ANTIALIAS)
card.paste(code,(75,200))
print(type(card))
print(type(code))
card.show()