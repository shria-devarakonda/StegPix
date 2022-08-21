import imghdr

from stegano.lsbset import generators
import inspect
import random

from StegPix.scripts.utils.constants import sample_message


def hacky_string():
    sample_string = 'errorERROR-_=+[{}]1234567890failFAILdeathDEATHspookyCURSE////'
    result = ''.join((random.choice(sample_string)) for x in range(random.randint(10, 100)))
    print(f"Hacking: {result}")


def generator_selector():
    # todo: will create use for this func later
    all_generators = inspect.getmembers(generators, inspect.isfunction)
    generator_names = []
    for generator in all_generators:
        print(f"GENERATOR NAME: {generator[0]}\nGENERATOR DESCRIPTION: {generator[0].__doc__}\n")
        generator_names.append(generator[0])
    gen = input("Which of the above generators would you like to use to encrypt your message in the image?\n>>")
    gen = gen.lower().strip()
    if gen in generator_names:
        return gen
    else:
        raise Exception("Generator not present in the given list")


def read_message(path):
    with open(path, "r") as f:
        secret = f.readlines()
    if not secret:
        print("File is empty. Using sample message.")
        secret = sample_message
    return secret


def image_file_handler(filepath):
    img_type = imghdr.what(filepath)
    if img_type == "jpeg" or img_type == "tiff":
        decrypter, img_type = "exifHeader", img_type
    elif img_type == "png":
        generator = "eratosthenes"
        decrypter, img_type = generator, img_type
    else:
        raise Exception("Image format not supported.")
    return decrypter, img_type


def write_message(message, path):
    with open(path, 'w', encoding='utf-8') as my_file:
        my_file.write(message.decode('utf-8'))
    if not message:
        raise Exception("Message is empty!")


def write_png_message(message, path):
    with open(path, 'w') as my_file:
        my_file.write(message)
    if not message:
        raise Exception("Message is empty!")