def cetak_nama(nama=''):
  # Tulis kode fungsi cetak_nama di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  nama=input("Masukkan nama: ")
  i = 0
  while(i < len(nama)):
    i = i+1
    print(nama[0:i])
    if (i == len(nama)):
        print(nama+"!")
  print("Tidak ada nama yang dicetak")

def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  x = 0
  for i in range(len(kata2)):
    if(kata1[i] == kata2[i]):
      x = x + 1
  return x

def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  #Jika operator bernilai '+', maka fungsi akan mengembalikan bil1 + bil2
  if operator =="+":
    hitung = bil1 + bil2
    return  hitung
  #Jika operator bernilai '-', maka fungsi akan mengembalikan bil1 - bil2  
  elif operator == "-":
    hitung = bil1 - bil2
    return hitung
  #Jika operator bernilai '*', maka fungsi akan mengembalikan bil1 * bil2
  elif operator == "*":
    hitung = bil1 * bil2 
    return hitung
  pass



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':test()