# Lưu ý
<p>Script cần hai máy tính, nếu dùng chung mạng thì có thể dùng phần mềm VPN để nhận được quà (VD: Proton VPN).
Flow farm 200: Máy 1 sẽ thực hiện tạo room đầu tiên, room 2 người và máy 1 sẽ thực hiện các đòn đánh để kiếm điểm. Máy 2 chỉ cần vào sau đó và bật auto ready. Như vậy chỉ có máy 1 là nhận được quà từ các mốc của sự kiện 200.
</p>

Cấu hình game: 
+ Đặt ở chế độ 800x600 - Windowed
+ Mang nhân vật võ sí + Trang bị bốn cánh tay, cần có skill Hanh cáp (để đánh không bị té, người thực hiện đánh không cần có skill này)

> auto_ready: Tự động nhấn nút Ready
> auto_get_5000_points: Tự động vào trận đánh gần đủ điểm, sau đó đợi đến giây thứ 399 thì kết thúc trận đấu
> auto_fast_match: Tự động kết thúc nhanh trận đấu. Dùng để farm Gold


# Package
pip install PyGetWindow PyAutoGUI numpy keyboard opencv-python pyinstaller

pip install --upgrade Pillow


# Pyinstaller cmd
> pyinstaller --clean --onedir --noconfirm D:\projects\ga2-farm200\auto_ready.py

> pyinstaller --clean --onedir --noconfirm D:\projects\ga2-farm200\auto_get_5000_points.py

> pyinstaller --clean --onedir --noconfirm D:\projects\ga2-farm200\auto_fast_match.py












