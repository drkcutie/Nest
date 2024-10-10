import os, uuid


def upload_local_image(image, folder: str):
    if image:
        upload_uid = str(uuid.uuid4()) #ID FOR THE PCTURES


        # find path for the static folder
        STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')

      
        
        extension = image.content_type
        extension = extension.split("/")[1]
        STATIC_PATH = f"images/{folder}/{upload_uid}.{extension}"
        image_path = f"{STATIC_ROOT}/{STATIC_PATH}"

        print(image_path)

        with open(image_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        return STATIC_PATH
    
