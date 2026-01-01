# main.py
from browser_client import BrowserClient
import config
import time

def main():
    print("=" * 60)
    print("MINI PROJET P4-C1 : Ghost in the Browser")
    print("Automatisation après authentification")
    print("=" * 60)
    print()
    
    client = BrowserClient()
    
    try:
        # Étape 1 : Login
        print("\n[ÉTAPE 1] Authentification")
        print("-" * 60)
        client.login()
        
        # Étape 2 : Aller à la messagerie
        print("\n[ÉTAPE 2] Accès à la messagerie")
        print("-" * 60)
        client.navigate_to_messages()
        
        # Étape 3 : Sélectionner le destinataire
        print("\n[ÉTAPE 3] Recherche et sélection du destinataire")
        print("-" * 60)
        client.search_and_select_recipient()
        
        # Étape 4 : Envoyer le message
        print("\n[ÉTAPE 4] Envoi du message")
        print("-" * 60)
        client.send_message()
        
        print("\n" + "=" * 60)
        print("✓ SUCCÈS : Le navigateur a agi à ta place !")
        print("Le message a été envoyé à {}".format(config.RECIPIENT))
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
    
    finally:
        time.sleep(2)
        client.close()

if __name__ == "__main__":
    main()
