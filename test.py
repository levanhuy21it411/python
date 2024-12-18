import pandas as pd
from ics import Calendar, Event
from datetime import datetime

# Đọc file CSV
file_path = "E:/lich_fullstack.csv"  # Đổi tên file nếu cần
df = pd.read_csv(file_path)

# Tạo đối tượng Calendar
calendar = Calendar()

# Đảm bảo các cột cần thiết trong CSV (tuỳ thuộc vào file của bạn)
# Giả sử file có cột 'summary', 'description', 'start', 'end'
for index, row in df.iterrows():
    event = Event()
    event.name = row['fullstack']  # Tên sự kiện
    event.description = row.get('description', '')  # Mô tả sự kiện
    event.begin = datetime.strptime(row['start'], '%Y-%m-%d %H:%M:%S')  # Thời gian bắt đầu
    event.end = datetime.strptime(row['end'], '%Y-%m-%d %H:%M:%S')  # Thời gian kết thúc
    calendar.events.add(event)

# Lưu Calendar vào file .ics
output_file = "lich_fullstack.ics"
with open(output_file, "w") as f:
    f.writelines(calendar)

print(f"File .ics đã được tạo: {output_file}")
