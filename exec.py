from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_png_to_pdf(input_folder, output_file):
    # PDF 생성을 위한 Canvas 객체 생성
    c = canvas.Canvas(output_file, pagesize=(letter[1], letter[0]))  # A4 용지 가로로 설정

    # 페이지 크기 설정
    page_width, page_height = letter[::-1]  # 가로와 세로를 바꿈

    # 입력 폴더 내의 모든 PNG 파일 가져오기
    png_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.png')])

    # PNG 파일을 이어붙여서 PDF로 추가
    for png_file in png_files:
        # PNG 파일 열기
        image_path = os.path.join(input_folder, png_file)
        image = Image.open(image_path)

        # 이미지 비율 계산
        image_width, image_height = image.size
        aspect_ratio = image_width / image_height

        # 이미지를 페이지에 맞게 추가할 때 사용할 크기 계산
        if aspect_ratio > 1:
            # 이미지의 가로가 더 긴 경우
            image_height = page_height
            image_width = page_height * aspect_ratio
        else:
            # 이미지의 세로가 더 긴 경우
            image_width = page_width
            image_height = page_width / aspect_ratio

        # 이미지를 페이지에 추가
        c.drawImage(image_path, 0, 0, width=image_width, height=image_height)
        c.showPage()  # 페이지 추가

    # PDF 파일 저장
    c.save()
    print("PDF 파일 생성이 완료되었습니다.")

# 입력 폴더와 출력 파일 지정
input_folder = "png"  # 입력 폴더 경로 설정
output_file = "output.pdf"  # 출력 PDF 파일 경로 설정

# PNG 파일을 PDF로 변환
convert_png_to_pdf(input_folder, output_file)
