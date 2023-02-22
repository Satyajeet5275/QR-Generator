from io import BytesIO
import qrcode


def Generate_QR_Image(Text, Fill_Color="#000000", Background_Color="#ffffff", File_Format="JPEG"):

    QR_Manager = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10, border=2) 

    QR_Manager.add_data(Text)   # Adding The Text.
    QR_Manager.make(fit=True)   # Detecting The Best Version To Use.

    QR_Image = QR_Manager.make_image(fill_color=Fill_Color, back_color=Background_Color)  # Generating The Image.

    Buffered = BytesIO()  # Creating The Buffer.
    QR_Image.save(Buffered, format=File_Format)  # Saving The Image To The Buffer.

    return Buffered.getvalue()  # Returning The Bytes Of The Image.

Generate_QR_Image("https://www.youtube.com/watch?v=8KVrdL0VcAk")