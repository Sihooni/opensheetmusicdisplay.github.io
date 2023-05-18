# 파일 경로
file_path = r"C:\Users\sh010\OneDrive - 고려대학교\바탕 화면\JAS\이름.txt"

# 파일을 읽기 모드로 열기
with open(file_path, "r", encoding="cp949") as file:
    content = file.read()

# 줄바꿈 문자를 제거
content_without_linebreaks = content.replace("\n", "")

# 파일을 쓰기 모드로 열고 줄바꿈 없는 내용을 다시 쓰기
with open(file_path, "w", encoding="utf-8") as file:
    file.write(content_without_linebreaks)
