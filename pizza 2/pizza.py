import csv
import datetime
import pandas
# Pizza üst sınıfı

class Pizza:
    def __init__(self):
        self.description = "Bilinmeyen Pizza"
        self.cost = 0
        
    def get_description(self):
        return self.description
        
    def get_cost(self):
        return 0.0

# Pizza alt sınıfları
class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        
    def get_cost(self):
        return 20.0
        
class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margarita Pizza"
        
    def get_cost(self):
        return 25.0
        
class TurkishPizza(Pizza):
    def __init__(self):
        self.description = "Türk Pizza"
        
    def get_cost(self):
        return 30.0

# Sos üst sınıfı (Decorator)
class Sos(Pizza):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Bilinmeyen Sos"
        
    def get_description(self):
        return self.component.get_description() + ", " + self.description
        
    def get_cost(self):
        return self.component.get_cost()

# Sos alt sınıfları (Decorator)
class ZeytinSos(Sos):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Zeytin Sos"
        
    def get_cost(self):
        return self.component.get_cost() + 2.0
        
class MantarSos(Sos):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Mantar Sos"
        
    def get_cost(self):
        return self.component.get_cost() + 3.0
        
class KeciPeyniriSos(Sos):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Keçi Peyniri Sos"
        
    def get_cost(self):
        return self.component.get_cost() + 4.0
        
class EtSos(Sos):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Et Sos"
        
    def get_cost(self):
        return self.component.get_cost() + 5.0
        
class SoganSos(Sos):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Soğan Sos"
        
    def get_cost(self):
        return self.component.get_cost() + 1.0
        
class MisirSos(Sos):
    def __init__(self, pizza):
        self.component = pizza
        self.description = "Mısır Sos"
        
    def get_cost(self):
        return self.component.get_cost() + 2.5

# Menüyü ekrana yazdıran fonksiyon
def print_menu():
    with open("Menu.txt") as f:
        print(f.read())


def get_order():
    total_cost = 0
    print("Lütfen pizza seçin (1-4): ")
    pizza_choice = input()
    if pizza_choice == "1":
        pizza = ClassicPizza()
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
    elif pizza_choice == "3":
        pizza = TurkishPizza()
    elif pizza_choice == "4":
        pizza = Pizza()
    else:
        print("Hatalı seçim.")
        return None
    is_on = True
    while  is_on:
        print("Lütfen sos seçin (1-6) (Çıkmak için q ya basın): ")
        sos_choice = input()
        if sos_choice == "1":
            pizza = ZeytinSos(pizza)
        elif sos_choice == "2":
            pizza = MantarSos(pizza)
        elif sos_choice == "3":
            pizza = KeciPeyniriSos(pizza)
        elif sos_choice == "4":
            pizza = EtSos(pizza)
        elif sos_choice == "5":
            pizza = SoganSos(pizza)
        elif sos_choice == "6":
            pizza = MisirSos(pizza)
        elif sos_choice == 'q':
            break
        else:
            print("Hatalı seçim.")
            return None
        total_cost = pizza.get_cost()
        pizza.cost = total_cost
    return pizza

class CreditCard:
    def __init__(self):
        self.card_number = input("Kart numaranizi girin: ")
        self.expiration_date = input("Son kullanma tarihi giriniz (aa/yy):").split("/")
        self.cvv = input("Cvv giriniz: ")
        self.name = input("Kart üzerinde yazan isim: ")
        self.password = input("Kart şifresi: ")

    def process_payment(self, amount):
        print(f"Kredi kartı ile {amount} TL tutarında ödeme yapıldı.")


def save_order(orderr, credit_card: CreditCard):
    with open("Orders.csv", mode="a", newline="") as f:
        writer = csv.writer(f)
        description = orderr.get_description()
        cost = orderr.get_cost()
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = credit_card.name
        writer.writerow([f"Pizza: {description}",
                         f" Tutar: {cost}", f" Sipariş_tarihi: {date}", "\n", f" Isim: {name}",
                         f" Kart_numarasi: {credit_card.card_number}",
                         f" Son_kullanma_tarihi: {credit_card.expiration_date}", f" Cvv: {credit_card.cvv}",
                         f" Password: {credit_card.password}", "\n"])
        credit_card.process_payment(cost)


while True:
    print_menu()
    order = get_order()
    if order:
        new_card = CreditCard()
        save_order(order, new_card)
        print("Siparişiniz alındı. Teşekkür ederiz!")
    else:
        print("Hatalı seçim.")
    choice = input("bir tane daha siparis vercenmi? (E/H): ")
    if choice.lower() != "e":
        print("Güle güle!")
        break
