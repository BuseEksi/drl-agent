# Ortam Tasarım Dokümanı (Hafta 1: ekipçe doldurulacak)

Bu doküman 8 Kasım'da dondurulur. Sonrasında değişiklik ancak 4 kişinin ortak kararıyla yapılır.

## 1. Harita
- Boyut (ör. 20x20):
- Engel yoğunluğu aralığı:
- Üretim yöntemi (rastgele engel / oda-koridor):
- Bağlantılılık garantisi (ulaşılamayan boş hücre kalmasın):
- Eğitim harita seed'leri: rastgele. Test seti: 1000–1099. Zor/büyük set (generalization): 2000–2099.

## 2. Sensör (kısmi gözlemlenebilirlik)
- Lidar ışın sayısı ve menzili:
- Yerel pencere boyutu (5x5 / 7x7):
- Sensör gürültüsü (şimdilik yok, robustness testinde eklenecek):

## 3. Gözlem uzayı
-

## 4. Aksiyon uzayı
- Öneri: Discrete(4) = ileri, sol, sağ, bekle

## 5. Ödül fonksiyonu (v1)
- Yeni keşfedilen hücre başına: +
- Adım başına: -
- Çarpışma: -
- Tamamlanma bonusu: +
- Bilinen tuzaklar (reward hacking): yerinde dönme, duvar dibinde dolaşma, çarpmamak için hareketsiz kalma

## 6. Bölüm bitişi
- Keşif oranı >= %X:
- Adım limiti:
- Çarpışmada bitsin mi?:

## 7. Hafıza kararı (hafta 6)
- Frame stacking / GRU: hepsine aynı şekilde uygulanacak

## Hocaya sorulacak sorular
1. "Tek ajan" ifadesi, aynı ortamda her kişinin ayrı algoritma eğitmesine izin veriyor mu?
2. Aksiyon uzayı ayrık mı olmalı, en az bir algoritma sürekli aksiyonla mı denenmeli?
3. Baseline (frontier-based) hâlâ zorunlu mu?
4. Rapor bireysel mi, grup halinde mi?
