class ogrenci():
    "Bu sinif ogrenciyi tanimlar."
    def __init__(self):
        "Bu metot nesne tanimladiginda otomatik olarak calisir"
        self.name= "Mustafa"
        self.age= 14
        self.coding_lesson = "python"



class ogrenci2():
    counter = 0
    def __init__(self, name, age, coding_lesson):
        self.name= name
        self.age= age
        self.coding_lesson = coding_lesson

        ogrenci2.counter +=1
    
    def get_info(self):
        print("isim =", self.name , "yas =", self.age,  "ders =", self.coding_lesson)



    def update_info(self, lesson="java"):
        self.coding_lesson = lesson 
        self.get_info()

    def __str__(self):
        return self.name

        
ogr4 = ogrenci2("Mustafa",14,"python")
print(ogr4.age)

ogr4.get_info()

ogr4.update_info("ileri seviye")

print("sonrasi = ", ogr4.coding_lesson)

print(f"toplam ogrenci sayisi esittir = {ogrenci2.counter}")

print(ogr4) #<__main__.ogrenci2 object at 0x000001DEB796BFD0>
