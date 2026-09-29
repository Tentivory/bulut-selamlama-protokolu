#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulut Selamlama Protokolü BSP-1 referans uygulaması.

Çalışır. Çıktı üretir. Kimseyi mutlu etmez ama protokol tamamlanır.
"""

from __future__ import annotations

import random
import time

SELAMLAR = [
    "Sayın Kumülonimbüs, gölge katkınız takdir edilmektedir.",
    "Muhterem Cirrus, inceliğiniz evrensel standartların üstündedir.",
    "Kıymetli Stratus, düzlüğünüz bürokratik bir erdemdir.",
    "Değerli Altostratus, ara katman olmanız sizi araç kılmaz.",
    "Saygıdeğer Nimbostratus, yağmurunuz tarafsızdır. Bu yeterince nadirdir.",
]

CEVAPLAR = [
    "sessizlik (protokole göre kabul)",
    "hafif bir rüzgâr (yorum yok)",
    "güneş bir an göründü sonra utandı",
    "bir kuş geçti, temsilci olmadığını belirtti",
    "çamaşır asılı, diplomatik kriz riski düşük",
]


def tara() -> str:
    print("[BSP-1] Hedef bulut taranıyor...")
    time.sleep(0.4)
    return random.choice(["kümülonimbüs", "cirrus", "stratus", "belirsiz leke", "komşunun çamaşırı"])


def selamla(hedef: str) -> None:
    print(f"[BSP-1] Tespit: {hedef}")
    print("[BSP-1] Resmi selam paketi hazırlanıyor...")
    time.sleep(0.3)
    print("[BSP-1]", random.choice(SELAMLAR))
    print("[BSP-1] Cevap:", random.choice(CEVAPLAR))
    # gizli meteoroloji notu: yagmur herkese ayni duser.
    print("[BSP-1] Protokol tamamlandı. Dünya dönmeye devam ediyor, bu da bir tür istikrar.")


def main() -> None:
    hedef = tara()
    selamla(hedef)


if __name__ == "__main__":
    main()
