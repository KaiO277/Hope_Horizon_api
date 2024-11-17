# my_app/utils.py
from datetime import datetime
from django.utils.text import slugify

def generate_unique_podcast_title(title):
    # Lấy ngày giờ hiện tại theo định dạng "YYYYMMDD_HHMMSS"
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Slugify title để tạo tên hợp lệ cho URL
    unique_title = f"{slugify(title)}_{current_time}"
    
    return unique_title
