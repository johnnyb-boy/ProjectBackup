import os

chemin = os.path.expanduser("~/Desktop")

for element in os.listdir(chemin):
    chemin_complet = os.path.join(chemin, element)
    if os.path.isfile(chemin_complet):
        print(f"{element}")
    elif os.path.isdir(chemin_complet):
        print(f"{element}/")