from fonctionnalite import *

def afficher_menu(taches):
    afficher_taches(taches)
    print("\nMenu:")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Quitter")

if __name__ == "__main__":
    taches = charger_taches()  # Assurez-vous que cette fonction est bien définie pour charger les tâches
 
    while True:
        afficher_menu(taches)
        choix = input("Entrez votre choix : ")
 
        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            supprimer_tache(taches)
        elif choix == "3":
            marquer_comme_terminee(taches)
        elif choix == "4":
            sauvegarder_taches(taches)
            print("Sortie du gestionnaire de tâches.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")