from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader

# todo: add sample filepaths where not provided
from StegPix.scripts.utils.utils import image_file_handler, write_png_message, write_message


def message_decrypter(decrypter, img_type, path):
    if img_type == "png":
        png_image_decrypter(decrypter, path)
    else:
        jpg_image_decrypter(path)


def png_image_decrypter(decrypter, filepath):
    decrypter = f"generators.{decrypter}()"
    decrypter_generator = eval(decrypter)
    message = lsbset.reveal(filepath, decrypter_generator)
    save_message_path = input("Please provide the path with the filename (with extension: .txt) of where you would "
                              "like to save the decrypted message.\n>>")
    # todo : add validation for filepath directory or isempty
    write_png_message(message, save_message_path)
    return f"File is present at {save_message_path}"


def jpg_image_decrypter(filepath):
    message = exifHeader.reveal(filepath)
    save_message_path = input("Please provide the path with the filename (with extension: .txt) of where you would "
                              "like to save the decrypted message.\n>>")
    # todo : add validation for filepath directory or isempty
    write_message(message, save_message_path)
    return f"File is present at {save_message_path}"


# todo: add a func for saving the message


def run_decryption():
    path = input("Please provide the path of the image to be decrypted.\n>>")
    # todo: add filepath validation
    decrypter, img_type = image_file_handler(path)
    message_decrypter(decrypter, img_type, path)

