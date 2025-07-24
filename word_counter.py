#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thesis Word Counter Tool
Đếm số từ trong luận án đa ngôn ngữ (Trung-Việt-Anh)
"""

import re
import os
import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import unicodedata
from collections import Counter
from datetime import datetime

class LatexParser:
    """Xử lý và làm sạch nội dung LaTeX"""
    
    def __init__(self):
        # Các environment cần loại bỏ
        self.ignore_environments = [
            'figure', 'table', 'equation', 'align', 'itemize', 'enumerate',
            'thebibliography', 'bibliography', 'abstract', 'quote', 'verse'
        ]
        
        # Các lệnh LaTeX cần loại bỏ
        self.ignore_commands = [
            'chapter', 'section', 'subsection', 'subsubsection', 'paragraph',
            'footnote', 'footcite', 'cite', 'ref', 'label', 'caption',
            'includegraphics', 'url', 'href', 'textbf', 'textit', 'emph',
            'underline', 'textsuperscript', 'textsubscript', 'newline',
            'vspace', 'hspace', 'centering', 'raggedright', 'raggedleft',
            'makeatletter', 'makeatother', 'newcommand', 'renewcommand',
            'usepackage', 'documentclass', 'begin', 'end', 'input', 'include',
            'bibliographystyle', 'bibliography', 'graphicspath', 'frontmatter',
            'mainmatter', 'backmatter', 'tableofcontents', 'listoffigures',
            'listoftables', 'makecover', 'addcontentsline'
        ]
    
    def remove_comments(self, content: str) -> str:
        """Loại bỏ comments LaTeX"""
        # Loại bỏ comment một dòng
        content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
        return content
    
    def remove_latex_commands(self, content: str) -> str:
        """Loại bỏ các lệnh LaTeX"""
        # Loại bỏ các lệnh có tham số
        for cmd in self.ignore_commands:
            # Pattern cho lệnh có tham số trong {}
            pattern1 = rf'\\{cmd}\s*{{[^}}]*}}'
            content = re.sub(pattern1, '', content)
            
            # Pattern cho lệnh có tham số trong []
            pattern2 = rf'\\{cmd}\s*\[[^\]]*\]'
            content = re.sub(pattern2, '', content)
            
            # Pattern cho lệnh không có tham số
            pattern3 = rf'\\{cmd}\b'
            content = re.sub(pattern3, '', content)
        
        # Loại bỏ các lệnh khác có tham số
        content = re.sub(r'\\[a-zA-Z]+\s*{[^}]*}', '', content)
        content = re.sub(r'\\[a-zA-Z]+\s*\[[^\]]*\]', '', content)
        content = re.sub(r'\\[a-zA-Z]+\b', '', content)
        
        return content
    
    def remove_environments(self, content: str) -> str:
        """Loại bỏ các environment LaTeX"""
        for env in self.ignore_environments:
            # Pattern cho environment với nội dung
            pattern = rf'\\begin\s*{{{env}}}.*?\\end\s*{{{env}}}'
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Loại bỏ các environment khác
        content = re.sub(r'\\begin\s*{[^}]*}.*?\\end\s*{[^}]*}', '', content, flags=re.DOTALL)
        
        return content
    
    def clean_content(self, content: str) -> str:
        """Làm sạch toàn bộ nội dung LaTeX"""
        # Loại bỏ comments trước
        content = self.remove_comments(content)
        
        # Loại bỏ environments
        content = self.remove_environments(content)
        
        # Loại bỏ commands
        content = self.remove_latex_commands(content)
        
        # Loại bỏ các ký tự đặc biệt LaTeX
        content = re.sub(r'\\[{}]', '', content)  # Loại bỏ \{ và \}
        content = re.sub(r'\\[~^"]', ' ', content)  # Loại bỏ \~, \^, \"
        
        # Loại bỏ khoảng trắng thừa
        content = re.sub(r'\s+', ' ', content)
        content = content.strip()
        
        return content

class LanguageDetector:
    """Phân loại và đếm từ theo ngôn ngữ"""
    
    def __init__(self):
        # Pattern cho chữ Hán
        self.chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
        
        # Pattern cho tiếng Việt (có dấu) - cải thiện
        self.vietnamese_pattern = re.compile(r'\b[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđa-zA-Z]+\b')
        
        # Pattern cho tiếng Anh và Latin
        self.english_pattern = re.compile(r'\b[a-zA-Z]+\b')
    
    def detect_chinese(self, text: str) -> List[str]:
        """Tìm tất cả chữ Hán"""
        return self.chinese_pattern.findall(text)
    
    def detect_vietnamese(self, text: str) -> List[str]:
        """Tìm tất cả từ tiếng Việt có dấu"""
        return self.vietnamese_pattern.findall(text)
    
    def detect_english(self, text: str) -> List[str]:
        """Tìm tất cả từ tiếng Anh"""
        return self.english_pattern.findall(text)
    
    def count_by_language(self, text: str) -> Dict[str, int]:
        """Đếm từ theo ngôn ngữ"""
        chinese_words = self.detect_chinese(text)
        vietnamese_words = self.detect_vietnamese(text)
        english_words = self.detect_english(text)
        
        # Loại bỏ trùng lặp và từ rỗng
        chinese_count = len([w for w in set(chinese_words) if len(w.strip()) > 0])
        vietnamese_count = len([w for w in set(vietnamese_words) if len(w.strip()) > 0])
        english_count = len([w for w in set(english_words) if len(w.strip()) > 0])
        
        # Tính tổng thực tế (có thể có overlap)
        total_unique = len(set(chinese_words + vietnamese_words + english_words))
        
        return {
            'chinese': chinese_count,
            'vietnamese': vietnamese_count,
            'english': english_count,
            'total': total_unique
        }

class ChapterStats:
    """Thống kê cho một chương"""
    
    def __init__(self, chapter_name: str, file_path: str):
        self.chapter_name = chapter_name
        self.file_path = file_path
        self.total_words = 0
        self.chinese_words = 0
        self.vietnamese_words = 0
        self.english_words = 0
        self.raw_content = ""
        self.clean_content = ""
        self.language_breakdown = {}
    
    def to_dict(self) -> Dict:
        """Chuyển thành dictionary"""
        return {
            'chapter_name': self.chapter_name,
            'file_path': self.file_path,
            'total_words': self.total_words,
            'chinese_words': self.chinese_words,
            'vietnamese_words': self.vietnamese_words,
            'english_words': self.english_words,
            'language_breakdown': self.language_breakdown
        }

class ThesisWordCounter:
    """Tool chính để đếm từ trong luận án"""
    
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.latex_parser = LatexParser()
        self.language_detector = LanguageDetector()
        self.chapters = []
        self.total_stats = {}
    
    def load_tex_files(self) -> List[Tuple[str, str]]:
        """Đọc tất cả file .tex trong project"""
        tex_files = []
        processed_files = set()  # Để tránh trùng lặp
        
        # Đọc main.tex trước
        main_tex = self.project_path / "main.tex"
        if main_tex.exists():
            with open(main_tex, 'r', encoding='utf-8') as f:
                tex_files.append(("main.tex", f.read()))
                processed_files.add("main.tex")
        
        # Đọc các file trong thư mục data
        data_dir = self.project_path / "data"
        if data_dir.exists():
            for file_path in data_dir.glob("*.tex"):
                if file_path.name not in processed_files:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        tex_files.append((file_path.name, f.read()))
                        processed_files.add(file_path.name)
        
        return tex_files
    
    def process_chapter(self, chapter_name: str, content: str, file_path: str) -> ChapterStats:
        """Xử lý một chương"""
        stats = ChapterStats(chapter_name, file_path)
        
        # Làm sạch nội dung LaTeX
        clean_content = self.latex_parser.clean_content(content)
        stats.clean_content = clean_content
        
        # Đếm từ theo ngôn ngữ
        language_counts = self.language_detector.count_by_language(clean_content)
        
        stats.total_words = language_counts['total']
        stats.chinese_words = language_counts['chinese']
        stats.vietnamese_words = language_counts['vietnamese']
        stats.english_words = language_counts['english']
        stats.language_breakdown = language_counts
        
        return stats
    
    def analyze_thesis(self) -> Dict:
        """Phân tích toàn bộ luận án"""
        print("Đang đọc các file .tex...")
        tex_files = self.load_tex_files()
        
        print(f"Tìm thấy {len(tex_files)} file .tex")
        
        # Xử lý từng file
        for file_name, content in tex_files:
            print(f"Đang xử lý: {file_name}")
            
            # Xác định tên chương từ nội dung
            chapter_match = re.search(r'\\chapter\s*{([^}]+)}', content)
            if chapter_match:
                chapter_name = chapter_match.group(1)
            else:
                chapter_name = file_name.replace('.tex', '')
            
            stats = self.process_chapter(chapter_name, content, file_name)
            self.chapters.append(stats)
        
        # Tính tổng thống kê
        self.calculate_total_stats()
        
        return self.generate_report()
    
    def calculate_total_stats(self):
        """Tính tổng thống kê"""
        total_chinese = sum(chap.chinese_words for chap in self.chapters)
        total_vietnamese = sum(chap.vietnamese_words for chap in self.chapters)
        total_english = sum(chap.english_words for chap in self.chapters)
        total_words = sum(chap.total_words for chap in self.chapters)
        
        self.total_stats = {
            'total_words': total_words,
            'chinese_words': total_chinese,
            'vietnamese_words': total_vietnamese,
            'english_words': total_english,
            'num_chapters': len(self.chapters)
        }
    
    def generate_report(self) -> Dict:
        """Tạo báo cáo tổng hợp"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_stats': self.total_stats,
            'chapters': [chap.to_dict() for chap in self.chapters],
            'summary': self.generate_summary()
        }
        
        return report
    
    def generate_summary(self) -> Dict:
        """Tạo tóm tắt"""
        if not self.chapters:
            return {}
        
        # Tìm chương dài nhất và ngắn nhất
        longest_chapter = max(self.chapters, key=lambda x: x.total_words)
        shortest_chapter = min(self.chapters, key=lambda x: x.total_words)
        
        # Tính trung bình
        avg_words = self.total_stats['total_words'] / len(self.chapters)
        
        return {
            'longest_chapter': {
                'name': longest_chapter.chapter_name,
                'words': longest_chapter.total_words
            },
            'shortest_chapter': {
                'name': shortest_chapter.chapter_name,
                'words': shortest_chapter.total_words
            },
            'average_words_per_chapter': round(avg_words, 2),
            'language_distribution': {
                'chinese_percentage': round(self.total_stats['chinese_words'] / self.total_stats['total_words'] * 100, 2),
                'vietnamese_percentage': round(self.total_stats['vietnamese_words'] / self.total_stats['total_words'] * 100, 2),
                'english_percentage': round(self.total_stats['english_words'] / self.total_stats['total_words'] * 100, 2)
            }
        }
    
    def print_report(self, report: Dict):
        """In báo cáo ra console"""
        print("\n" + "="*60)
        print("BÁO CÁO ĐẾM TỪ LUẬN ÁN")
        print("="*60)
        
        # Thống kê tổng quan
        total = report['total_stats']
        print(f"\n📊 THỐNG KÊ TỔNG QUAN:")
        print(f"   Tổng số từ: {total['total_words']:,}")
        print(f"   Số chương: {total['num_chapters']}")
        print(f"   - Chữ Hán: {total['chinese_words']:,}")
        print(f"   - Tiếng Việt: {total['vietnamese_words']:,}")
        print(f"   - Tiếng Anh: {total['english_words']:,}")
        
        # Phân bố ngôn ngữ
        summary = report['summary']
        lang_dist = summary['language_distribution']
        print(f"\n🌐 PHÂN BỐ NGÔN NGỮ:")
        print(f"   - Chữ Hán: {lang_dist['chinese_percentage']}%")
        print(f"   - Tiếng Việt: {lang_dist['vietnamese_percentage']}%")
        print(f"   - Tiếng Anh: {lang_dist['english_percentage']}%")
        
        # Thống kê theo chương
        print(f"\n📖 THỐNG KÊ THEO CHƯƠNG:")
        for chap in report['chapters']:
            print(f"   {chap['chapter_name']}: {chap['total_words']:,} từ")
        
        # Chương dài nhất và ngắn nhất
        longest = summary['longest_chapter']
        shortest = summary['shortest_chapter']
        print(f"\n📈 CHI TIẾT:")
        print(f"   Chương dài nhất: {longest['name']} ({longest['words']:,} từ)")
        print(f"   Chương ngắn nhất: {shortest['name']} ({shortest['words']:,} từ)")
        print(f"   Trung bình/chương: {summary['average_words_per_chapter']:,} từ")
        
        print("\n" + "="*60)
    
    def export_to_json(self, report: Dict, filename: str = "word_count_report.json"):
        """Export báo cáo ra file JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã export báo cáo ra file: {filename}")
    
    def export_to_excel(self, report: Dict, filename: str = "word_count_report.xlsx"):
        """Export báo cáo ra file Excel"""
        try:
            # Tạo DataFrame cho các chương
            chapters_df = pd.DataFrame(report['chapters'])
            
            # Tạo DataFrame cho tổng thống kê
            total_df = pd.DataFrame([report['total_stats']])
            
            # Tạo DataFrame cho summary
            summary_df = pd.DataFrame([report['summary']])
            
            # Export ra Excel với nhiều sheet
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                chapters_df.to_excel(writer, sheet_name='Chapters', index=False)
                total_df.to_excel(writer, sheet_name='Total_Stats', index=False)
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            print(f"✅ Đã export báo cáo ra file Excel: {filename}")
        except PermissionError:
            print(f"⚠️ Không thể tạo file Excel {filename} (file có thể đang được mở)")
            print("   Hãy đóng file Excel nếu đang mở và chạy lại")
        except Exception as e:
            print(f"❌ Lỗi khi tạo file Excel: {e}")

def main():
    """Hàm chính"""
    print("🔍 Bắt đầu đếm từ luận án...")
    
    # Khởi tạo counter
    counter = ThesisWordCounter()
    
    # Phân tích luận án
    report = counter.analyze_thesis()
    
    # In báo cáo
    counter.print_report(report)
    
    # Export kết quả
    counter.export_to_json(report)
    counter.export_to_excel(report)
    
    print("\n🎉 Hoàn thành!")

if __name__ == "__main__":
    main() 