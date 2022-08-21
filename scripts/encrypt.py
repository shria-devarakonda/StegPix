from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader

# todo: add sample filepaths where not provided
from StegPix.scripts.utils.utils import read_message, image_file_handler


def message_encrypter(encrypter, img_type, path, message_path):
    if img_type == "png":
        png_image_encrypter(encrypter, path, message_path)
    else:
        jpg_image_encrypter(path, message_path)


def png_image_encrypter(encrypter, filepath, message_path):
    secret_message = read_message(message_path)
    secret_message = '\n'.join(secret_message)
    encrypter = f"generators.{encrypter}()"
    encrypter_generator = eval(encrypter)
    secret_image = lsbset.hide(filepath,
                               secret_message,
                               encrypter_generator)
    save_image_path = input("Please provide the path with the filename (with extension: .png) of where you "
                            "would like to save the encrypted image.\n>>")
    # todo : add validation for filepath directory or isempty
    secret_image.save(save_image_path)
    return f"File is present at {save_image_path}"


def jpg_image_encrypter(filepath, message_path):
    secret_message = read_message(message_path)
    secret_message = '\n'.join(secret_message)
    save_image_path = input("Please provide the path with the filename (with extension: .jpg or .tiff) of where you "
                            "would like to save the encrypted image.\n>>")
    # todo : add validation for filepath directory or isempty
    secret = exifHeader.hide(filepath,
                             save_image_path, secret_message=secret_message)
    return f"File is present at {save_image_path}"


def run_encryption():
    path = input("Please provide the path of the image to be encrypted.\n>>")
    # todo: add filepath validation
    encrypter, img_type = image_file_handler(path)
    secret_message_path = input("Please provide the path of the text file with the secret message.\n>>")
    message_encrypter(encrypter, img_type, path, secret_message_path)

