#KAMERA + GÖRÜNTÜ İŞLEME
"""
KAMERA GÖRÜNTÜ İŞLEME
- Kameradan görüntü alır
- Gürültü temizleme
- Kenar tespiti yapar
"""

import cv2


class KameraIsleme:
    def __init__(self):
        self.kamera = cv2.VideoCapture(0)

        if not self.kamera.isOpened():
            raise RuntimeError("Kamera açılamadı!")

    def goruntu_isle(self):
        """
        Görüntüyü alır ve işler
        """
        ret, kare = self.kamera.read()
        if not ret:
            return None

        # Gri tonlamaya çevir
        gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

        # Gürültüyü azalt
        bulanık = cv2.GaussianBlur(gri, (5, 5), 0)

        # Kenar tespiti
        kenarlar = cv2.Canny(bulanık, 50, 150)

        return kenarlar

    def baslat(self):
        """
        Sonsuz döngüde görüntü işleme
        """
        while True:
            sonuc = self.goruntu_isle()

            if sonuc is not None:
                cv2.imshow("Kenar Tespiti", sonuc)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.kapat()

    def kapat(self):
        self.kamera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    kamera = KameraIsleme()
    kamera.baslat()
