meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL":"tanggapan terhadap lelucon",
            "SHEESH":"sedikit ketidaksetujuan",
            "CREEPY":"menakutkan, tidak menyenangkan",
            "AGGRO":"untuk menjadi agresif/marah",
            "SKIBIDI":"jelek/buruk",
            "CMIWW":"Benarkan aku jika salah",
            "ASAP":"Secepat mungkin"

            }


word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan j
    print("Mohon maaf,katanya yang anda cari tidak ada")
