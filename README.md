# 🌟 Hope Horizon API

Dự án **Hope Horizon API** cung cấp backend cho nền tảng hỗ trợ cộng đồng Hope Horizon. Dự án được xây dựng với Django và REST framework, phục vụ mục tiêu kết nối những người cần giúp đỡ với các tổ chức và cá nhân thiện nguyện.

---

## 📋 Yêu cầu hệ thống

- Python 3.8+
- pip
- Git (tuỳ chọn)
- Hệ điều hành: Windows / macOS / Linux

---

## ⚙️ Cài đặt & Chạy dự án

### 1. Clone hoặc tải mã nguồn
```bash
git clone [[https://github.com/your-username/Hope_Horizon_api.git](https://github.com/KaiO277/Hope_Horizon_api.git)](https://github.com/KaiO277/Hope_Horizon_api.git)
```

2. Tạo và kích hoạt môi trường ảo
```
python -m venv myenv
myenv\Scripts\activate        # Trên Windows
# hoặc
source myenv/bin/activate     # Trên macOS/Linux
```


3. Cài đặt các thư viện cần thiết
```
pip install -r requirements.txt
```

4. Di chuyển vào thư mục dự án
```
cd Hope_Horizon_api
```

5. Cập nhật cơ sở dữ liệu
```
python manage.py makemigrations
python manage.py migrate
```
7. Chạy dự án
   
🔸 Chạy trên một máy (localhost)
```
python manage.py runserver
```
🔸 Chạy cho nhiều thiết bị cùng mạng LAN
```
python manage.py runserver 0.0.0.0:8000
```
🧪 Kiểm tra hoạt động
Truy cập trình duyệt:
```
http://127.0.0.1:8000/
```
Nếu chạy bằng mạng LAN:
```
http://<IP-của-máy-chạy-server>:8000/
```

📝 Ghi chú
Nếu thay đổi các model, hãy chạy lại:

```
python manage.py makemigrations
python manage.py migrate
```

Dự án mặc định chạy trên cổng 8000, có thể thay đổi nếu cần.

Đảm bảo môi trường ảo đã được kích hoạt khi chạy dự án.
