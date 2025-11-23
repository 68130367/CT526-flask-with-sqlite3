# สร้างโฟลเดอร์ venv สำหรับเก็บสภาพแวดล้อมจำลอง โดยใช้ extension Python Environments ในการสร้าง

# ติดตั้ง Flask โดยใช้คำสั่ง pip install Flask

# การวางโครงสร้างโฟลเดอร์ (Project Structure)

- `templates`: Flask จะเข้ามาหาไฟล์ HTML ในนี้โดยอัตโนมัติเมื่อเราใช้คำสั่ง `render_template()`
- `static`: Flask จะใช้โฟลเดอร์นี้สำหรับเก็บไฟล์ที่ไม่ต้องประมวลผล เช่น CSS, JavaScript, รูปภาพ
- สร้างไฟล์ `app.py` เพื่อกำหนด route
- สร้าง Layout กลาง (layout.html) เพื่อใช้ร่วมกัน
- สร้างหน้าเว็บโดยสืบทอดจาก Layout
- เพิ่มสีสันล์ด้วย CSS

# run project by using this command `python app.py`
