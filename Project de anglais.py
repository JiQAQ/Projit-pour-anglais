def transport():
    return input("Quel transport prennez vous")
def veri_transport(tr):
    transport = ["Marche","Trotinette","Vélo","Transport en commun","Trotinette électrique","Voiture électrique","Moto","Voiture"]
    for i in range(len(transport)):
        if i == tr:
            if 