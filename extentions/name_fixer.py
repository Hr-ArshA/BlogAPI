import os
import random
import time
from hashlib import sha256
from uuid import uuid4


def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_img_path(instance, filename):
    file_time = time.time()
    name, ext = get_file_name_ext(filename)
    class_name = str(instance.__class__).split('\'')[-2].split('.')[-1]

    '''
    makeing name of files with sha256
    
    random_num = random.randint(0,99999999999999999)
    hash_this = str(str(file_time) + str(random_num)).encode('utf-8')
    hash_it = sha256(hash_this).hexdigest()
    final_name = f"{hash_it}{ext}"
    '''

    '''
    makeing name of files with uuid
    '''
    name = str(uuid4())
    final_name = f"{name}{ext}"


    return f"image/{class_name}/{final_name}"
