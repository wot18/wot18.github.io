from docx import Document
import re

def check_docx_for_links():
    try:
        doc = Document("论文+专利+软著+纵向+横向+教研+获奖20260106.docx")
        print("Reading docx file...")
        
        found_videos = False
        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue
                
            # Check for keywords
            if "视频" in text or "bilibili" in text.lower() or "http" in text.lower():
                print(f"Found relevant text: {text}")
                found_videos = True
                
        if not found_videos:
            print("No video links or keywords found in the document.")
            
    except Exception as e:
        print(f"Error reading docx: {e}")

if __name__ == "__main__":
    check_docx_for_links()
