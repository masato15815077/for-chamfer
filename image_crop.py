from PIL import Image

ORG_FILE_NAME = r'C:\Users\fukuzaki.masato\AppData\Local\Continuum\anaconda3\Projects\for_chamfer\images\lena.jpg'
CRP_FILE_NAME = r'C:\Users\fukuzaki.masato\AppData\Local\Continuum\anaconda3\Projects\for_chamfer\images\lena_part.jpg'

im = Image.open(ORG_FILE_NAME)

# 画像の切り出し（特徴画像作成のため）
im_crop = im.crop((200, 75, 225, 100))
im_crop.save(CRP_FILE_NAME, quality=95)

# im_crop.show()

