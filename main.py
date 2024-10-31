import datetime

print("------------------1 uzd.---------------------")
student = {
    "vardas": "Petras",
    "pavarde": "Petrauskas",
    "amzius": 20,
    "studiju_programa": "Program1",
    "kreditai": 5,
    "pazymiai": [7, 8, 9, 5],
    "ugis": 156,
    "kursas": 5,
    "universitetas": "KTU"
}

print(student)
print(student['vardas'])
print(student['kursas'])
print(student['universitetas'])

print("------------------2 uzd.---------------------")
film = {
    "pavadinimas": "The Godfather",
    "režisierius": "Francis Ford Coppola",
    "biudžetas": 6000000,
    "uždarbis": 270000000,
    "žanras": "American crime fiction",
    "trukmė": 3,
    "išleidimo_metai": datetime.date(1972, 3, 24),
    "aktorių sąrašas": ["Al Pacino", "Marlon Brando", "James Caan"]
}

print(film)
print(f"pelnas: {film['uždarbis'] - film['biudžetas']}")
print(f"aktorių kiekis: {len(film['aktorių sąrašas'])}")
print(f"Filmui yra metų: {datetime.date.today().year - film['išleidimo_metai'].year}")

print("------------------3 uzd.---------------------")
book1 = {
    "pavadinimas": "Danukas Dunduliukas",
    "autorius": "Petras Petraukas",
    "žanras": "Detektyvas",
    "kaina": 18.5,
    "puslapių kiekis": 120,
    "skyrių sąrašas": ["pirmas sk", "antras sk", "trecias sk"],
    "išleidimo metai": 1970,
    "yra knygynuose": True
}

book2 = {
    "pavadinimas": "Bembis ir Bembio vaikai",
    "autorius": "Zita Zitkauskaitė",
    "žanras": "Nuotykių",
    "kaina": 10.42,
    "puslapių kiekis": 180,
    "skyrių sąrašas": ["pirmas", "antras", "trecias", "ketvirtas"],
    "išleidimo metai": 1960,
    "yra knygynuose": False
}
print(book1)
print(book2)
print(
    f"Plonesnė knyga: {book1["pavadinimas"] if book1["puslapių kiekis"] < book2["puslapių kiekis"] else book2["pavadinimas"]}")
print(
    f"Daugiau skyrių turi: {book1["pavadinimas"] if len(book1["skyrių sąrašas"]) > len(book2["skyrių sąrašas"]) else book2["pavadinimas"]}")

cheaper_book = ""
more_expensive_book = ""

if book1['kaina'] < book2['kaina']:
    cheaper_book = book1
    more_expensive_book = book2
else:
    cheaper_book = book2
    more_expensive_book = book1

print(f"Pigesnė knyga:{cheaper_book['pavadinimas']}")

if cheaper_book['kaina'] * 2 < more_expensive_book['kaina']:
    print(f"Pigesnė knyga po padvigubintos kainos: {cheaper_book['pavadinimas']}")
else:
    print(f"Pigesnė knyga padvigubintos kainos: {more_expensive_book['pavadinimas']}")

print("------------------4 uzd.---------------------")
item1 = {
    "pavadinimas": "stalas",
    "kaina": 80.2,
    "savikaina": 40,
    "kodas": 123456,
    "kiekis": 15,
    "matmenys": {"plotis": 80, "ilgis": 150, "aukštis": 80}
}
item2 = {
    "pavadinimas": "kėdė",
    "kaina": 30.2,
    "savikaina": 10.5,
    "kodas": 987654,
    "kiekis": 2,
    "matmenys": {"plotis": 50, "ilgis": 60, "aukštis": 25}
}
item3 = {
    "pavadinimas": "pufikas",
    "kaina": 10.2,
    "savikaina": 5.5,
    "kodas": 445566,
    "kiekis": 86,
    "matmenys": {"plotis": 20, "ilgis": 30, "aukštis": 20}
}

warehouse = [item1, item2, item3]

for i, item in enumerate(warehouse):
    print(f"{i + 1}-a prekė kainuoja: {item["kaina"]}. ", end="")

print()
max_price_item = warehouse[0]
for i, item in enumerate(warehouse):
    if item["kaina"] > max_price_item["kaina"]:
        max_price_item = item

    print(item)
    print(f"{i + 1}-os prekės pelningumas: {round((item["kaina"] - item["savikaina"]) * item["kiekis"])}")
    print(
        f"{i + 1}-os prekės tūris: {item["matmenys"]["plotis"] * item["matmenys"]["ilgis"] * item["matmenys"]["aukštis"]}")

print(f"Brangiausia prekė: {max_price_item["pavadinimas"]}. Jos kaina: {max_price_item["kaina"]}")

print("------------------5 uzd.---------------------")
auto = {}
auto["markė"] = "ford"
auto["modelis"] = "mustang"
auto["rida"] = 1000
auto["metai"] = 2020
auto["spalva"] = "red"
auto["darbinis tūris"] = 2.2
auto["daužta"] = False
auto["parduodama"] = True

print(auto)
print(f"Kiek automobiliui metų: {datetime.date.today().year - auto["metai"]}")
print(f"Vidutiniškai per metus automobilis nuvažiavo: {auto["rida"] / (datetime.date.today().year - auto['metai'])}")

print("------------------6 uzd.---------------------")
cat_breed1 = {
    "name": "Abyssinian",
    "min_weight": 5,
    "max_weight": 10,
    "colours": ["Ruddy", "bright red", "blue", "fawn"],
    "price": 2000,
    "sold": 15
}
cat_breed2 = {
    "name": "Bengal",
    "min_weight": 6,
    "max_weight": 18,
    "colours": ["Bright orange to light brown, with dark spots", "a distinctive marbling pattern"],
    "price": 1500,
    "sold": 55
}
cat_breed3 = {
    "name": "Sphynx",
    "min_weight": 6,
    "max_weight": 12,
    "colours": ["White", "black", "blue", "red", "cream", "chocolate", "lavender", "cinnamon", "fawn"],
    "price": 3000,
    "sold": 5
}

breeds = [cat_breed1, cat_breed2, cat_breed3]

max_sold = breeds[0]
for i, breed in enumerate(breeds):
    print(f"{i + 1}-a katė: {breed}")
    print(f"{i + 1}-a katė kainuoja: {breed["price"]}. ")
    if breed["sold"] > max_sold["sold"]:
        max_sold = breed

print(f"Labiausiai perkama katė: {max_sold["name"]}")

print("------------------7 uzd.---------------------")
bookstore = {
    "pavadinimas": "Knygų pasaulis",
    "adresas": "Nemuno g. 2",
    "plotas": 102,
    "knygu_kiekis": 10000,
    "darbo_valandos": "I-V: 8:00-17:00",
    "atidarytas": True
}
for b in bookstore:
    print(b)

print("------------------8 uzd.---------------------")
student1 = {
    "vardas": "Petras",
    "pavarde": "Petrauskas",
    "studiju_programa": "Program1",
    "pazymiai": [7, 8, 9, 5]
}
student2 = {
    "vardas": "Inga",
    "pavarde": "Ingauskaitė",
    "studiju_programa": "Program2",
    "pazymiai": [2, 9, 5, 6, 7]
}
students = [student1, student2]
averages = []
for i, s in enumerate(students):
    print(s)
    average = sum(s["pazymiai"]) / len(s["pazymiai"])
    averages.append(average)
    print(f"{i + 1}-ojo studento vidurkis: {average}")

print(f"Vidurkis yra didesnis: ", end="")
print(
    students[0]["vardas"] + " " + students[0]["pavarde"] if averages[0] > averages[1] else students[1]["vardas"] + " " +
                                                                                           students[1]["pavarde"])

print("------------------9 uzd.---------------------")
products = {
    "pieštukas": 132,
    "trintukas": 2,
    "liniuotė": 78,
    "skriestuvas": 8,
    "penalas": 19
}

for k, product in products.items():
    print(f"- Prekės \"{k}\" liko {product} vnt. ")
prod_sum = sum(products.values())
print(f"Bendras visų prekių kiekis: {prod_sum}")
print(f"Prekių vidurkis: {prod_sum / len(products)}")
prod_min = min(products.values())
for k, product in products.items():
    if product == prod_min:
        print(f"Prekė su mažiausiu kiekiu: {k}")

print("-----------------10 uzd.---------------------")
employee1 = {
    "vardas": "Antanas",
    "pavardė": "Pavardė",
    "telefonas": "+370-675-58965",
    "profesija": "statybininkas",
    "etatas": "pilnas",
    "atlyginimas": "3000"
}
employee2 = {
    "vardas": "Birutė",
    "pavardė": "Birauskienė",
    "telefonas": "+370-675-58965",
    "atlyginimas": "1000"
}
# for k in employee1:
#     if k not in employee2:
#         employee2[k] = input(f"Savybės \"{k}\" antras darbuotojas neturi, prašau ją įvesti: ")

missing_keys = employee1.keys() - employee2.keys()
for k in missing_keys:
    employee2[k] = input(f"Savybės \"{k}\" antras darbuotojas neturi, prašau ją įvesti: ")

print(employee1)
print(employee2)

print("-----------------11 uzd.---------------------")
bakery1 = {
    "pavadinimas": "Danutės pyragai",
    "darbuotojų_kiekis": 12,
    "adresas": "Putvinskio g. 25",
    "kiekiai": {
        "Tinginys": 30,
        "Keksiukas": 200,
        "Kankorėžis": 120,
        "Pono tortas": 8,
        "Maskarponė": 40,
        "Šokoladinis pyragas": 13,
        "Kanelė": 300
    }
}
bakery2 = {
    "pavadinimas": "Kepyklėlė",
    "darbuotojų_kiekis": 20,
    "adresas": "Donelaičio g. 5",
    "kiekiai": {
        "Tinginys": 10,
        "Keksiukas": 100,
        "Kankorėžis": 220,
        "Pono tortas": 15,
        "Maskarponė": 18,
        "Šokoladinis pyragas": 10,
        "Kanelė": 400
    }
}
bakery3 = {
    "pavadinimas": "Adelės skanumynai",
    "darbuotojų_kiekis": 15,
    "adresas": "Gedimino g. 5",
    "kiekiai": {
        "Tinginys": 12,
        "Keksiukas": 112,
        "Kankorėžis": 180,
        "Pono tortas": 20,
        "Maskarponė": 20,
        "Šokoladinis pyragas": 15,
        "Kanelė": 100
    }
}
bakeries = [bakery1, bakery2, bakery3]
most_profitable_bakery = bakeries[0]
least_average_bakery = bakeries[0]
for b in bakeries:
    b_sum = sum(b["kiekiai"].values())
    if (b_sum * 1.5) > (sum(most_profitable_bakery["kiekiai"].values()) * 1.5):
        most_profitable_bakery = b
    day_avg = b_sum / 7
    if day_avg < (sum(least_average_bakery["kiekiai"].values()) / 7):
        least_average_bakery = b

print(f"Pelningiausia kepykla: {most_profitable_bakery["pavadinimas"]}")
print(f"Kepykla su mažiausiu vidurkiu: {least_average_bakery["pavadinimas"]}")

print("-----------------12 uzd.---------------------")
print("-----------------13 uzd.---------------------")
print("-----------------14 uzd.---------------------")
print("-----------------15 uzd.---------------------")
company1 = {
    "name": "Telia",
    "age": 30,
    "employees": 2000,
    "profit": 10000000
}
company2 = {
    "name": "Tele-2",
    "age": 20,
    "employees": 1500,
    "profit": 20000000
}
company3 = {
    "name": "Bitė",
    "age": 25,
    "employees": 1000,
    "profit": 2000000
}
companies = [company1, company2, company3]
for c in companies:
    print(f"Įmonės pavadinimas: {c["name"]}, pelnas: {c["profit"]}")
age_sum = sum(company["age"] for company in companies)
print(f"Įmonių vidutinis amžius: {age_sum / len(companies)}")
print(f"Darbuotojų kiekis: {sum([company["employees"] for company in companies])}")
print(f"Bendras pelnas: {sum(company["profit"] for company in companies)}")

print("-----------------16 uzd.---------------------")
print("-----------------17 uzd.---------------------")
print("-----------------18 uzd.---------------------")
store = {
    "pavadinimas": "Segebutė",
    "adresas": "Pranciškaus g. 4",
    "darbuotojų kiekis": 12,
    "prekių sąrašas": [
        {
            "pavadinimas": "pieštukas", "kodas": 111, "kaina": 2, "savikaina": 1, "kiekis": 56
        },
        {
            "pavadinimas": "trintukas", "kodas": 222, "kaina": 1, "savikaina": 0.5, "kiekis": 34
        },
        {
            "pavadinimas": "tušinukas", "kodas": 333, "kaina": 5, "savikaina": 3, "kiekis": 101
        }
    ]
}
print(f"Parduotuvės pavadinimas: {store["pavadinimas"]}, adresas: {store["adresas"]}")
print("Prekės: ")
for product in store["prekių sąrašas"]:
    print(f"Prekė: {product["pavadinimas"]}. Kiekis: {product["kiekis"]}")

print(f"Iš viso prekių: {sum([p["kiekis"] for p in store["prekių sąrašas"]])}")
max_count = max([p["kiekis"] for p in store["prekių sąrašas"]])
min_count = min([p["kiekis"] for p in store["prekių sąrašas"]])
for p in store["prekių sąrašas"]:
    if p["kiekis"] == min_count:
        print(f"Mažiausiai ({min_count}) yra prekių su šiuo pavadinimu: {p["pavadinimas"]}")
    if p["kiekis"] == max_count:
        print(f"Daugiausiai ({max_count}) yra prekių su šiuo pavadinimu: {p["pavadinimas"]}")

print("-----------------19 uzd.---------------------")
print("-----------------20 uzd.---------------------")

# ----------------------------------------------------------------------------------------------
# ------------------------------------------------TUPLES----------------------------------------
print("------------------1 uzd.---------------------")
programs = ("module1", "module22", "module4444", "module333")
print("Visi moduliai:")
for p in programs:
    print(f"-{p}. ", end="")
max_length_progr = programs[0]
for p in programs:
    if len(p) > len(max_length_progr):
        max_length_progr = p
print()
print(f"Ilgiausias modulio pavadinimas: {max_length_progr}")

print("------------------2 uzd.---------------------")
months = ('sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis',
          'liepa', 'rugpjutis', 'rugsejis', 'spalis', 'lapkritis', 'gruodis')
winter = months[-1:] + months[0:2]
spring = months[2:5]
summer = months[5:8]
autumn = months[8:11]
print(f"Žiema: {winter}")
print(f"Pavasaris: {spring}")
print(f"Vasara: {summer}")
print(f"Ruduo: {autumn}")

# ----------------------------------------------------------------------------------------------
# --------------------------------------------------SETS----------------------------------------
print("------------------1 uzd.---------------------")
prog_languages = ["c++", "python", "python", "javascript", "python", "c#", "javascript"]
print("Programavimo kalbos: ")
print(prog_languages)
unique_prog_languages = set(prog_languages)
print("Unikalios programavimo kalbos: ")
print(unique_prog_languages)
