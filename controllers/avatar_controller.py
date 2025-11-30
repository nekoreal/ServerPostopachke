from PIL import Image
from io import BytesIO
from miniIO_S3.S3photos import upload_photo_bytes, get_photo_bytes

def get_avatar_bytes(user_id):
    avatar_bytes = get_photo_bytes(user_id, 'avatars')
    if avatar_bytes is None:
        avatar_bytes = get_photo_bytes("defoultAvatar", 'avatars')
    return avatar_bytes

def save_avatar(img: Image.Image, user_id, size:int=100):
    processed_img=process_image_to_square(img)

    output = BytesIO()
    processed_img.save(output, format='JPEG')
    output.seek(0)
    #output_for_return=BytesIO()
    #processed_img.save(output_for_return, format='JPEG')
    #output_for_return.seek(0)

    upload_photo_bytes(user_id, output, 'avatars')
    return {"message": "Avatar saved"}
    #return output_for_return

def process_image_to_square(img: Image.Image, size:int=100) -> Image.Image:
    width, height = img.size
    min_side = min(width, height)
    left = (width - min_side) // 2
    top = (height - min_side) // 2
    right = left + min_side
    bottom = top + min_side
    img = img.crop((left, top, right, bottom))
    img = img.resize((size, size), Image.LANCZOS)
    return img