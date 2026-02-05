import pandas as pd
import re

filename = "各级研究生信息.xlsx"
df = pd.read_excel(filename, header=None)

html_output = []
current_year = ""

html_output.append('<div class="students-container">')

for index, row in df.iterrows():
    col0 = str(row[0]).strip()
    col1 = str(row[1]).strip()
    
    if "级" in col0:
        current_year = col0
        html_output.append(f'<h2 class="student-year">{current_year}</h2>')
        html_output.append('<div class="student-grid">')
        continue
        
    # Check if it's a student row (usually col0 is "图片" or empty, and col1 has content)
    if col1 and col1 != "nan":
        # Parse info
        # Content format example: "李秋霖\n研究方向 ：未见目标位姿估计\n邮箱：1413630487@qq.com"
        lines = re.split(r'[ \n]+', col1)
        
        name = lines[0]
        direction = ""
        email = ""
        
        # Try to find direction and email
        full_text = col1
        
        # Extract email
        email_match = re.search(r'邮箱[：:]\s*([\w\.\-]+@[\w\.\-]+)', full_text)
        if email_match:
            email = email_match.group(1)
        
        # Extract direction
        dir_match = re.search(r'研究方向[：:]\s*(.*?)(?=\n|邮箱|$)', full_text)
        if dir_match:
            direction = dir_match.group(1).strip()
            
        # Generate HTML
        # Assuming images are stored as name.png or name.jpg in assets/img/students/
        # Using a placeholder if image doesn't exist (handled by alt text or css)
        
        card_html = f"""
  <div class="student-card">
    <div class="student-img">
      <img src="/assets/img/students/{name}.png" alt="{name}" onerror="this.src='/assets/img/default_avatar.png'">
    </div>
    <div class="student-info">
      <h3>{name}</h3>
      {f'<p class="direction"><strong>研究方向：</strong>{direction}</p>' if direction else ''}
      {f'<p class="email"><strong>邮箱：</strong>{email}</p>' if email else ''}
    </div>
  </div>
"""
        html_output.append(card_html)
    
    # Check if next row is a new year or end of file to close the grid
    if index + 1 < len(df):
        next_col0 = str(df.iloc[index+1][0]).strip()
        if "级" in next_col0:
            html_output.append('</div>') # Close previous grid
    else:
        html_output.append('</div>') # Close last grid

html_output.append('</div>')

with open("students_section.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_output))

print("HTML generated in students_section.html")
