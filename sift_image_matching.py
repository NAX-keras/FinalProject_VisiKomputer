import cv2
import matplotlib.pyplot as plt

def sift_matching(imgA_path, imgB_path, title):
    imgA = cv2.imread(imgA_path, cv2.IMREAD_GRAYSCALE)
    imgB = cv2.imread(imgB_path, cv2.IMREAD_GRAYSCALE)

    sift = cv2.SIFT_create()

    kpA, desA = sift.detectAndCompute(imgA, None)
    kpB, desB = sift.detectAndCompute(imgB, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(desA, desB, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Sort biar lebih rapi
    good_matches = sorted(good_matches, key=lambda x: x.distance)

    result = cv2.drawMatches(imgA, kpA, imgB, kpB,
                             good_matches[:50], None,
                             flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    print("===================================")
    print(title)
    print("Keypoints Image A:", len(kpA))
    print("Keypoints Image B:", len(kpB))
    print("Good Matches:", len(good_matches))
    print("===================================")

    plt.figure(figsize=(15,8))
    plt.imshow(result, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()


# =====================
# EKSPERIMEN
# =====================

sift_matching('image1.jpeg', 'image2.jpeg', 'Normal vs Rotasi')
sift_matching('image1.jpeg', 'image3.jpeg', 'Normal vs Zoom')
sift_matching('image1.jpeg', 'image4.jpeg', 'Normal vs Blur')
