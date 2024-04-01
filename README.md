# png-to-pdf

png 사진 묶어 pdf 파일로 변환하자!

## png-to-pdf 사용 방법

이 코드는 여러 개의 png 파일들을 묶어 하나의 pdf 파일로 만드는 프로그램입니다.
clone 받으신 후에 아래의 순서에 맞게 사용하시면 됩니다. 

1. 이 레포지토리 코드를 `git clone` 명령어를 사용해 로컬에 다운로드합니다.
   
2. 필요한 라이브러리들을 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다.

```bash
pip3 install Pillow reportlab
```

3. 변환하고자 하는 png 파일을 `png`라는 이름의 폴더에 모은 후, `png-to-pdf` 파일에 폴더를 놓아 주세요.

<img width="641" alt="image" src="https://github.com/gitchannn/png-to-pdf/assets/107979804/b85004d6-c610-46b4-a10c-43fdb286e65f">

여기서 `png` 폴더 안에 들어있는 png 사진들을 이제 변환하게 됩니다.

4. python 코드를 실행해 주세요.

```bash
python3 exec.py
```

<img width="696" alt="image" src="https://github.com/gitchannn/png-to-pdf/assets/107979804/a6fdfed7-a9ae-4574-b500-92d65c76f0ec">

png 파일이 많을 경우에 시간이 오래 걸릴 수 있습니다. 보통 600장 정도의 사진은 4분 정도 소요됩니다.

5. `output.pdf` 파일 확인

프로젝트 파일의 루트 위치에 pdf 파일이 생성됩니다. 

<img width="641" alt="image" src="https://github.com/gitchannn/png-to-pdf/assets/107979804/160e8cd1-b334-47b9-b7c0-3d08f80ee82f">

   
