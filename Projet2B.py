class TypeOrdinateur:
    DESKTOP = 'DESKTOP'
    LAPTOP = 'LAPTOP'
    MINIPC = 'MINIPC'


class Ordinateur:
    def __init__(self, marque, type, prix, stock):
        self.marque = marque
        self.type = type
        self.prix = prix
        self.stock = stock


class Administrateur:
    def __init__(self, nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passe = mot_de_passe


MAX_COMPUTERS = 100

ordinateurs = []
admin = Administrateur("admin", "password")
estAdmin = False


def ajouter_ordinateur():
    if len(ordinateurs) >= MAX_COMPUTERS:
        print("Le nombre maximum d'ordinateurs a été atteint.")
        return

    print("Ajouter un nouvel ordinateur :")

    marque = input("Marque : ")
    type = input("Type (DESKTOP, LAPTOP, MINIPC) : ")
    prix = int(input("Prix : "))
    stock = int(input("Stock : "))

    ordinateur = Ordinateur(marque, type, prix, stock)
    ordinateurs.append(ordinateur)

    print("L'ordinateur a été ajouté avec succès.")


def consulter_details_ordinateur():
    print("Sélectionnez l'ordinateur dont vous souhaitez consulter les détails :")

    for i, ordinateur in enumerate(ordinateurs):
        print(f"{i + 1}. {ordinateur.marque}")

    choix = int(input("Votre choix : "))

    if 1 <= choix <= len(ordinateurs):
        ordinateur = ordinateurs[choix - 1]

        print("Détails de l'ordinateur :")
        print(f"Marque : {ordinateur.marque}")
        print(f"Type : {ordinateur.type}")
        print(f"Prix : {ordinateur.prix}")
        print(f"Stock : {ordinateur.stock}")
    else:
        print("Choix invalide.")


def mettre_a_jour_stock():
    print("Sélectionnez l'ordinateur dont vous souhaitez mettre à jour le stock :")

    for i, ordinateur in enumerate(ordinateurs):
        print(f"{i + 1}. {ordinateur.marque}")

    choix = int(input("Votre choix : "))

    if 1 <= choix <= len(ordinateurs):
        nouveau_stock = int(input("Nouveau stock : "))
        ordinateurs[choix - 1].stock = nouveau_stock
        print("Le stock a été mis à jour avec succès.")
    else:
        print("Choix invalide.")


def se_connecter_en_tant_qu_admin():
    global estAdmin
    nom = input("Nom : ")
    mot_de_passe = input("Mot de passe : ")

    if nom == admin.nom and mot_de_passe == admin.mot_de_passe:
        estAdmin = True
        print("Vous êtes maintenant connecté en tant qu'administrateur.")
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")


def main():
    while True:
        print("\n=== Gestion de la boutique d'informatique ===")
        print("1. Ajouter un nouvel ordinateur")
        print("2.
