- Cài máy ảo: python -m venv myenv
- Bật máy ảo: myenv\Scripts\activate
- Cài những phiên bản đã được liệt kê trong file requirements.txt bằng lệnh: pip install -r requirements.txt
- cd đến cd Hope_Horizon_api để chạy project: cd .\Hope_Horizon_api\
- Cập nhật lại database cho dự án với hai lệnh:
     python manage.py makemigrations
     python manage.py migrate
- Run dự án
  + Nếu bạn chạy một máy thì chạy lệnh sau:
    python manage.py runserver
  + Nếu bạn chạy hai máy cùng mạng thì chạy lệnh sau:
    python manage.py runserver 0.0.0.0:8000
