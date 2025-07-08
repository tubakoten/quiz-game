# Quiz Game

questions = [
    {
        "soru": "Rick and Morty dizisinde Rick’in eski dostu olan kuş-adamın adı nedir?",
        "secenekler": ["A) Birdguy", "B) Featherlord", "C) Hawkman", "D) Birdperson"],
        "cevap": "D"
    },
    {
        "soru": "Yüzüklerin Efendisi’nde yüzüğü yok etmek için yola çıkan hobbit kimdir?",
        "secenekler": ["A) Bilbo", "B) Sam", "C) Frodo", "D) Merry"],
        "cevap": "C"
    },
    {
        "soru": "En uzun süre yayınlanan çizgi dizi hangisidir?",
        "secenekler": ["A) The Simpsons", "B) Family Guy", "C) South Park", "D) Rick and Morty"],
        "cevap": "A"
    },
    {
        "soru": "Toy Story’de Andy’nin komşusu olan kötü çocuğun adı nedir?",
        "secenekler": ["A) Carl", "B) Sid", "C) Alex", "D) Max"],
        "cevap": "B"
    },
    {
        "soru": "Marvel evreninde Thor’un çekicinin adı nedir?",
        "secenekler": ["A) Stormbreaker", "B) Mjölnir", "C) Excalibur", "D) Aegis"],
        "cevap": "B"
    },
    {
        "soru": "Aşağıdakilerden hangisi Pixar yapımı bir filmdir?",
        "secenekler": ["A) Frozen", "B) Tangled", "C) Encanto", "D) Inside Out"],
        "cevap": "D"
    },
    {
        "soru": "Oz Büyücüsü'nde Dorothy'nin meşhur repliği nedir?",
        "secenekler": [
            "A) There’s no place like home",
            "B) To infinity and beyond!",
            "C) I'll be back",
            "D) May the Force be with you"
        ],
        "cevap": "A"
    }
]

puan = 0

print("🎉 Eğlence Quizi'ne hoş geldin! 🎉\n")

for index, soru in enumerate(questions):
    print(f"Soru {index + 1}: {soru['soru']}")
    for secenek in soru['secenekler']:
        print(secenek)
    
    cevap = input("Cevabınız (A/B/C/D): ").strip().upper()
    if cevap == soru["cevap"]:
        print("✅ Doğru!\n")
        puan += 1
    else:
        print(f"❌ Yanlış! Doğru cevap: {soru['cevap']}\n")

print(f"🎯 Quiz bitti! Toplam puanınız: {puan}/{len(questions)}")

if puan == len(questions):
    print("🏆 Mükemmel! Hepsini bildiniz!")
elif puan >= 5:
    print("👏 Güzel iş çıkardınız, eğlence kültürünüz sağlam!")
else:
    print("🤔 Daha çok film, dizi izlemelisiniz!")


