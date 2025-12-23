#ENGELDEN KAÇINMA
"""
ENGELDEN KAÇINMA MODÜLÜ
- Sonar mesafesine göre karar üretir
"""

class EngeldenKacinma:

    def __init__(self, guvenli_mesafe=1.0):
        self.guvenli_mesafe = guvenli_mesafe

    def karar_ver(self, sonar_mesafesi):
        """
        Sonar mesafesine göre hareket kararı verir
        """

        if sonar_mesafesi <= 0:
            return "HATALI VERİ"

        if sonar_mesafesi < self.guvenli_mesafe:
            return "DUR_VE_YON_DEGISTIR"
        else:
            return "ILERLE"
