# Lưu ý
```
<p>Script cần hai máy tính. 
Cần dùng VPN nếu xài chung mạng. (VD: Proton VPN - Free Unlimited)

```

<b>FLow farm 200:</b>
1) Máy 1 thực hiện đầu tiên: Tạo room 2 người, sẽ là máy đánh kiếm điểm và kết thúc trận đấu.  
2) Máy 2 thực hiện sau: Vào room mà máy 1 đã tạo, sau đó bật auto sẵn sàng và treo máy. Máy này sẽ không nhận được quà của event 200 vì không đủ điểm.
</p>

<b>Cấu hình ban đầu:</b>
- Setting trong game: Đặt ở chế độ 800x600 - Windowed
- Nhân vật: Võ Sĩ
- Trang bị: Bốn cánh tay (Mua bằng Gold trong Shop)
- Skill trang bị: Hanh cáp (Máy 2 cần skill này để không bị té)

<b>Scripts:</b>
> auto_ready: Tự động nhấn nút Ready  

> auto_get_5000_points: Tự động vào trận đánh gần đủ điểm, sau đó đợi đến giây thứ 399 thì kết thúc trận đấu  

> auto_fast_match: Tự động kết thúc nhanh trận đấu. Dùng để farm Gold  


# Package
```
pip install PyGetWindow PyAutoGUI numpy keyboard opencv-python pyinstaller  
```
```
pip install --upgrade Pillow
```

# Pyinstaller CMD
```
pyinstaller --clean --onedir --noconfirm D:\projects\ga2-farm200\auto_ready.py  
```
```
pyinstaller --clean --onedir --noconfirm D:\projects\ga2-farm200\auto_get_5000_points.py  
```
```
pyinstaller --clean --onedir --noconfirm D:\projects\ga2-farm200\auto_fast_match.py  
```







