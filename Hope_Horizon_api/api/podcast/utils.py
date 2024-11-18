# my_app/utils.py
from datetime import datetime
from django.utils.text import slugify
import random

def generate_unique_filename(title, file):   
    # Lấy ngày giờ hiện tại theo định dạng "YYYYMMDD_HHMMSS"
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    number_ramdom = random.uniform(0,100000)
    
    # Tạo tên mới cho file bằng cách ghép tên gốc với thời gian hiện tại
    unique_filename = f"{title}_{current_time}_{number_ramdom}"
    
    return unique_filename
