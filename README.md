# FinalProject_VisiKomputer
# Implementation of Scale-Invariant Feature Transform for Digital Image Matching

## Deskripsi
Proyek ini mengimplementasikan algoritma **SIFT** untuk mencocokkan fitur antara dua citra digital.  
Eksperimen dilakukan untuk menguji ketahanan terhadap:
- Rotasi
- Zoom (perubahan skala)
- Blur

## Requirement
- Python 3.x  
- OpenCV  
- Matplotlib  
## Install Python
Pastikan kamu sudah menginstall Python di komputer.  
Download Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  

Install dependency dengan:
pip install opencv-python matplotlib


Cara Menjalankan :

1. Clone repository:
git clone https://github.com/username/FinalProject_VisiKomputer.git

2. Masuk ke folder project:
cd FinalProject_VisiKomputer

3. jalankan program
python sift_image_matching.py

Program akan menampilkan:
  1.Jumlah keypoints pada setiap citra
  2.Jumlah good matches

Dataset :
image1.jpeg → Normal
image2.jpeg → Rotasi
image3.jpeg → Zoom
image4.jpeg → Blur
