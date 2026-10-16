# Çalışma Kuralları

## Git akışı
- `main` her zaman çalışır durumda olmalı. Doğrudan `main`'e push yok.
- Her kişi kendi branch'inde çalışır: `kisi1/env`, `kisi2/a2c`, `kisi3/ppo`, `kisi4/sac` gibi.
- İş bitince Pull Request açılır, **en az bir kişi** kodu okuyup onaylar (çapraz review: K1→K2→K3→K4→K1).
- Commit mesajı kısa ve açık olsun: `env: lidar sensörü eklendi`.

## Ortak dosyalara dokunma kuralı
`agents/base.py`, `scripts/train.py`, `scripts/evaluate.py`, `common/` ve `configs/default.yaml` ortak dosyalardır.
Bunlarda değişiklik gerekiyorsa önce grupta söyleyin, küçük bir PR ile ayrı yapın.

## Adil karşılaştırma
Ortam, gözlem, ödül, eğitim bütçesi (ortam adımı), seed'ler ve test haritaları tüm algoritmalar için aynıdır.
Kendi ajanınızın içini istediğiniz gibi tasarlayın, ama dışarıdan ortak `Agent` arayüzüne uyun.
