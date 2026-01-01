# Mini Projet P4-C1 : Ghost in the Browser

Automatisation après authentification sur l'intranet ESSTHS.  
Le script pilote un navigateur (Selenium) pour se connecter avec un compte étudiant,
accéder à la messagerie interne, sélectionner un professeur, puis envoyer automatiquement
un message.

## Objectif du projet

- Illustrer le concept de **"Ghost in the Browser"** : un programme qui agit à la place
  de l'utilisateur, sans exploiter de faille, mais en utilisant le navigateur comme intermédiaire.
- Montrer qu'une fois authentifié, un script peut effectuer les mêmes actions qu'un humain
  (messagerie, formulaires, etc.).

## Fonctionnalités

- Connexion automatique à l'intranet ESSTHS (login + mot de passe + captcha simple).
- Navigation vers la page **Messagerie**.
- Sélection automatique d'un destinataire (ex. `Alaeddine KHARRAT`) via le champ *Choisir*.
- Saisie d'un message dans l'éditeur TinyMCE.
- Clic sur le bouton **Envoyer** pour envoyer le message.

## Structure du projet

- `config.py`  
  Contient les URLs, les identifiants, les sélecteurs HTML et le contenu du message.

- `browser_client.py`  
  Classe `BrowserClient` qui pilote Selenium :
  - `login()` : authentification et résolution du captcha
  - `navigate_to_messages()` : accès à la messagerie
  - `search_and_select_recipient()` : choix du professeur
  - `send_message()` : rédaction et envoi du message

- `main.py`  
  Point d'entrée du programme. Enchaîne les 4 étapes principales.

- `requirements.txt`  
  Liste des dépendances Python (Selenium, etc.).

## Installation et exécution

