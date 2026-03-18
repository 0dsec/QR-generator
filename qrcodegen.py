import os
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer as gappedsquare
from qrcode.image.styles.colormasks import VerticalGradiantColorMask as verticalgrad

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
print(
"  /$$$$$$  /$$$$$$$\n" \
" /$$__  $$| $$__  $$\n" \
"| $$  \ $$| $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$$ \n" \
"| $$  | $$| $$$$$$$/ /$$__  $$ /$$__  $$| $$__  $$ \n" \
"| $$  | $$| $$__  $$| $$  \ $$| $$$$$$$$| $$  \ $$ \n" \
"| $$/$$ $$| $$  \ $$| $$  | $$| $$_____/| $$  | $$ \n" \
"|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$  | $$ \n" \
" \____ $$$|__/  |__/ \____  $$ \_______/|__/  |__/ \n" \
"      \__/           /$$  \ $$                     \n" \
"                    |  $$$$$$/                     \n" \
"                     \______/                      \n" \
)
my_data = input("Enter your url-> ")
save_as_name = input("Save As -> ")

qr_color_top = [
    int(input("Top Color R -> ")),
    int(input("Top Color G -> ")),
    int(input("Top Color B -> "))
]

qr_color_bottom = [
    int(input("Bottom Color R -> ")),
    int(input("Bottom Color G -> ")),
    int(input("Bottom Color B -> "))
]

bg_color = [
    int(input("Background Color R -> ")),
    int(input("Background Color G -> ")),
    int(input("Background Color B -> "))
]

qr.add_data(my_data)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=gappedsquare(),
    color_mask=verticalgrad(
        back_color=(bg_color[0], 
                    bg_color[1], 
                    bg_color[2]),
        top_color=(qr_color_top[0], 
                   qr_color_top[1], 
                   qr_color_top[2]),
        bottom_color=(
            max(0, qr_color_bottom[0]),
            max(0, qr_color_bottom[1]),
            max(0, qr_color_bottom[2])
        )
    )
)

img.save(save_as_name + ".png")

print("Thank you! Your QR has been saved!")