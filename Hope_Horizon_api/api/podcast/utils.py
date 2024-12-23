# my_app/utils.py
from datetime import datetime
from django.utils.text import slugify
import random

def generate_unique_filename(title, file_name):   
    # Lấy ngày giờ hiện tại theo định dạng "YYYYMMDD_HHMMSS"
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    number_random = random.uniform(0, 100000)
    
    # Tạo tên file duy nhất
    unique_filename = f"{title}_{current_time}_{number_random}"
    
    return unique_filename
