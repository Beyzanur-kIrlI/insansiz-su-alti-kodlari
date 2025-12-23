# ===============================
# YOLOv8 ile Nesne Algılama
# VS Code + Linux Uyumlu
# ===============================

# Gerekli kütüphaneler
import cv2
import torch
from ultralytics import YOLO

# ===============================
# 1. MODELİ YÜKLEME
# ===============================

# Eğitilmiş YOLOv8 modelinin yolu
model_yolu = "/home/beyzanur/auv_yolo/model/best.pt"

# Modeli yükle
model = YOLO(model_yolu)

print("YOLOv8 modeli yüklendi")

# ===============================
# 2. VİDEO / KAMERA KAYNAĞI
# ===============================

# Video dosyası yolu
# Webcam kullanmak için 0 yazabilirsin
video_yolu = "/home/beyzanur/auv_yolo/video/gate.mp4"
cap = cv2.VideoCapture(video_yolu)

if not cap.isOpened():
    print("Video açılamadı")
    exit()

print("Video kaynağı açıldı")

# ===============================
# 3. VİDEO OKUMA VE ALGILAMA
# ===============================

while True:
    ret, frame = cap.read()

    # Video bittiyse çık
    if not ret:
        print("Video sona erdi")
        break

    # ===============================
    # 4. YOLOv8 İLE NESNE TESPİTİ
    # ===============================

    results = model(frame)

    # ===============================
    # 5. TESPİT SONUÇLARINI İŞLEME
    # ===============================

    for result in results:
        kutular = result.boxes.xyxy.cpu().numpy()
        guvenler = result.boxes.conf.cpu().numpy()
        siniflar = result.boxes.cls.cpu().numpy()

        for i in range(len(kutular)):
            x1, y1, x2, y2 = kutular[i]
            guven = guvenler[i]
            sinif_id = int(siniflar[i])

            sinif_adi = model.names[sinif_id]
            etiket = f"{sinif_adi} %{guven*100:.1f}"

            # Kutuyu çiz
            cv2.rectangle(
                frame,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (255, 0, 0),
                2
            )

            # Etiketi yaz
            cv2.putText(
                frame,
                etiket,
                (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

    # ===============================
    # 6. SONUCU EKRANDA GÖSTERME
    # ===============================

    cv2.imshow("YOLOv8 - AUV Nesne Algilama", frame)

    # q tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Program kapatıldı")
        break

# ===============================
# 7. KAYNAKLARI SERBEST BIRAK
# ===============================

cap.release()
cv2.destroyAllWindows()
