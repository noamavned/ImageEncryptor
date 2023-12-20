import random
import os
import shutil
from error import raise_error

def enc(s):
    s = [''.join(format(ord(n), 'b')) for n in s]
    n = []
    for v, i in enumerate(s):
        n.append(f'|{v*360}|'+str(int(''.join([str(random.choice([1, 2, 3, 4]))
                 if x == '1' else str(random.choice([5, 6, 7, 8])) for x in i]))+180))
    random.shuffle(n)
    n = ''.join(n)
    return n


def dec(s):
    chunks = s.split('|')[1::]
    l = [[int(int(chunks[i])/360), str(''.join(['1' if int(x) in [1, 2, 3, 4]
                                                else '0' for x in str(int(chunks[i+1])-180)]))] for i in range(0, len(chunks), 2)]
    l = [x[1] for x in sorted(l, key=lambda x: x[0])]
    l = ''.join([chr(int(binary, 2)) for binary in l])
    return l


def extract_text_from_image(image_path):
    image_copy_path = image_path[0:-4] + '_copy.txt'

    try:
        shutil.copy(image_path, image_copy_path)
    except FileNotFoundError:
        print(f"File '{image_path}' not found.")
        return
    except FileExistsError:
        print(f"File '{image_copy_path}' already exists.")
        return
    successful_decode = False
    encodings_to_try = ['utf-8', 'latin-1', 'ascii']
    for encoding in encodings_to_try:
        try:
            with open(image_copy_path, 'r', encoding=encoding) as f:
                t = f.read().strip()
                t = t.split("/scb325/")[-2]
                successful_decode = True
                break
        except UnicodeDecodeError:
            continue
        except:
            raise_error("Check if the path you chose is correct.")
            t = None
            break
    if not successful_decode:
        raise_error(
            f"Unable to decode the content of '{image_copy_path}' with any of the specified encodings.")
        t = None
    os.remove(image_copy_path)
    return t


def hide_text_in_jpeg(image_path, text_to_hide, output_path):
    try:
        with open(image_path, 'rb') as file:
            jpeg_data = bytearray(file.read())
        eoi_marker_index = jpeg_data.rfind(b'\xFF\xD9')

        if eoi_marker_index == -1:
            raise_error(
                "End of Image (EOI) marker not found in the JPEG data.")

        encoded_text = text_to_hide.encode('utf-8')
        jpeg_data = jpeg_data[:eoi_marker_index] + \
            encoded_text + jpeg_data[eoi_marker_index:]

        with open(output_path, 'wb') as output_file:
            output_file.write(jpeg_data)
    except Exception as e:
        raise_error(
            f"Error: {e}")