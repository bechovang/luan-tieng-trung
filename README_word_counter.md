# Tool Đếm Từ Luận Án (Thesis Word Counter)

## 📋 Mô tả
Tool Python để đếm số từ trong luận án đa ngôn ngữ (Trung-Việt-Anh), hỗ trợ xử lý file LaTeX và tạo báo cáo chi tiết.

## 🚀 Tính năng chính

### ✅ Đã hoàn thành
- ✅ Đếm từ theo 3 ngôn ngữ: Chữ Hán, Tiếng Việt, Tiếng Anh
- ✅ Xử lý file LaTeX (.tex) tự động
- ✅ Loại bỏ các lệnh LaTeX và comments
- ✅ Phân tích theo từng chương
- ✅ Tạo báo cáo JSON và Excel
- ✅ Thống kê chi tiết và tổng quan

### 📊 Kết quả mẫu
```
📊 THỐNG KÊ TỔNG QUAN:
   Tổng số từ: 3,898
   Số chương: 10
   - Chữ Hán: 3,510
   - Tiếng Việt: 388
   - Tiếng Anh: 388

🌐 PHÂN BỐ NGÔN NGỮ:
   - Chữ Hán: 90.05%
   - Tiếng Việt: 9.95%
   - Tiếng Anh: 9.95%
```

## 🛠️ Cài đặt

### Yêu cầu hệ thống
- Python 3.7+
- Các thư viện: `pandas`, `openpyxl`

### Cài đặt thư viện
```bash
pip install pandas openpyxl
```

## 📖 Cách sử dụng

### 1. Chạy tool cơ bản
```bash
python word_counter.py
```

### 2. Kết quả
Tool sẽ tạo ra:
- `word_count_report.json`: Báo cáo chi tiết dạng JSON
- `word_count_report.xlsx`: Báo cáo Excel với nhiều sheet

## 📁 Cấu trúc file

### Input
- `main.tex`: File chính của luận án
- `data/chap*.tex`: Các chương của luận án
- `data/cover.tex`, `data/ack.tex`: File phụ

### Output
- `word_count_report.json`: Dữ liệu chi tiết
- `word_count_report.xlsx`: Báo cáo Excel

## 🔧 Tùy chỉnh

### Thêm ngôn ngữ mới
Chỉnh sửa class `LanguageDetector`:
```python
def detect_new_language(self, text: str) -> List[str]:
    # Thêm pattern cho ngôn ngữ mới
    pattern = re.compile(r'your_pattern_here')
    return pattern.findall(text)
```

### Thay đổi cách đếm từ
Chỉnh sửa method `count_by_language()` trong class `LanguageDetector`.

## 📊 Giải thích kết quả

### Thống kê tổng quan
- **Tổng số từ**: Tổng số từ unique trong toàn bộ luận án
- **Số chương**: Số lượng file .tex được xử lý
- **Phân bố ngôn ngữ**: Số từ theo từng ngôn ngữ

### Thống kê theo chương
- Tên chương và số từ tương ứng
- Chương dài nhất và ngắn nhất
- Trung bình từ/chương

### Phân bố ngôn ngữ
- Tỷ lệ phần trăm theo ngôn ngữ
- Giúp đánh giá tính đa ngôn ngữ của luận án

## ⚠️ Lưu ý quan trọng

### Xử lý LaTeX
- Tool tự động loại bỏ các lệnh LaTeX
- Loại bỏ comments và environments
- Giữ lại nội dung text thuần túy

### Detection ngôn ngữ
- **Chữ Hán**: Sử dụng Unicode range `\u4e00-\u9fff`
- **Tiếng Việt**: Pattern với dấu tiếng Việt
- **Tiếng Anh**: Pattern Latin alphabet

### Giới hạn
- Tool đếm từ unique (không trùng lặp)
- Có thể có overlap giữa các ngôn ngữ
- Không đếm các từ quá ngắn (< 1 ký tự)

## 🐛 Xử lý lỗi

### Lỗi thường gặp
1. **PermissionError khi tạo Excel**: Đóng file Excel nếu đang mở
2. **File không tìm thấy**: Kiểm tra cấu trúc thư mục
3. **Encoding error**: Đảm bảo file .tex có encoding UTF-8

### Debug
Thêm print statements trong code để debug:
```python
print(f"Processing file: {file_name}")
print(f"Found words: {language_counts}")
```

## 📈 Mở rộng tương lai

### Tính năng có thể thêm
- [ ] Đếm số trang ước tính
- [ ] Phân tích độ phức tạp câu
- [ ] So sánh với yêu cầu của trường
- [ ] Tích hợp với LaTeX compiler
- [ ] Phân tích cấu trúc luận án

### Cải thiện detection
- [ ] Machine learning cho language detection
- [ ] Hỗ trợ thêm ngôn ngữ
- [ ] Cải thiện accuracy

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Python version (>= 3.7)
2. Các thư viện đã cài đặt
3. Cấu trúc file .tex
4. Encoding của file

## 📄 License
Tool này được tạo cho mục đích học tập và nghiên cứu. 