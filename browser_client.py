# browser_client.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re
import config

class BrowserClient:
    def __init__(self):
        """Initialiser le navigateur."""
        options = webdriver.ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self):
        """Se connecter à l'intranet ESSTHS avec résolution automatique du captcha."""
        print("[*] Ouverture de la page de login...")
        self.driver.get(config.LOGIN_URL)
        time.sleep(2)
        
        print("[*] Saisie du nom d'utilisateur...")
        username_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.SELECTORS["username_input"]))
        )
        username_field.clear()
        username_field.send_keys(config.USERNAME)
        time.sleep(1)
        
        print("[*] Saisie du mot de passe...")
        password_field = self.driver.find_element(By.CSS_SELECTOR, config.SELECTORS["password_input"])
        password_field.clear()
        password_field.send_keys(config.PASSWORD)
        time.sleep(1)
        
        # ✨ RÉSOUDRE LE CAPTCHA AUTOMATIQUEMENT
        print("[*] Résolution du captcha...")
        try:
            captcha_label = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Résoudre')]")
            captcha_text = captcha_label.text
            print(f"    Captcha trouvé: {captcha_text}")
            
            match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', captcha_text)
            
            if match:
                num1 = int(match.group(1))
                operator = match.group(2)
                num2 = int(match.group(3))
                
                if operator == '+':
                    answer = num1 + num2
                elif operator == '-':
                    answer = num1 - num2
                elif operator == '*':
                    answer = num1 * num2
                elif operator == '/':
                    answer = int(num1 / num2)
                
                print(f"    Calcul: {num1} {operator} {num2} = {answer}")
                
                captcha_field = self.driver.find_element(By.CSS_SELECTOR, config.SELECTORS["captcha_input"])
                captcha_field.clear()
                captcha_field.send_keys(str(answer))
                time.sleep(1)
        except Exception as e:
            print(f"[!] Erreur lors de la résolution du captcha: {e}")
        
        print("[*] Clic sur le bouton Login...")
        login_button = self.driver.find_element(By.CSS_SELECTOR, config.SELECTORS["login_button"])
        login_button.click()
        
        time.sleep(3)
        print("[✓] Connexion réussie")
    
    def navigate_to_messages(self):
        """Aller à la page Messagerie."""
        print("[*] Navigation vers la page Messages...")
        self.driver.get(config.MESSAGES_URL)
        time.sleep(3)
        print("[✓] Page Messages ouverte")
    
    def search_and_select_recipient(self):
        """
        Cliquer sur le bouton "Choisir" 
        → barre de recherche apparaît
        → taper le nom complet du prof
        → cliquer sur le lien <a role="option">
        """
        print(f"[*] Sélection du destinataire: {config.RECIPIENT}...")
        
        try:
            time.sleep(2)
            
            # ÉTAPE 1: Cliquer sur le bouton "Choisir"
            print("    [1] Clic sur le bouton 'Choisir'...")
            choisir_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-id='select_u']"))
            )
            choisir_button.click()
            time.sleep(1)
            
            # ÉTAPE 2: Attendre que la barre de recherche apparaisse et taper le nom
            print(f"    [2] Saisie du nom: {config.RECIPIENT}...")
            search_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search'].form-control"))
            )
            search_input.send_keys(config.RECIPIENT)
            time.sleep(1.5)
            
            # ÉTAPE 3: Cliquer sur le lien <a role="option">
            print("    [3] Sélection de l'option...")
            option_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@role='option'][@class='dropdown-item active']"))
            )
            option_link.click()
            time.sleep(2)
            
            print(f"[✓] {config.RECIPIENT} sélectionné")
            
        except Exception as e:
            print(f"[!] Erreur: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def send_message(self):
        """Envoyer le message via TinyMCE."""
        print(f"[*] Envoi du message...")
        
        try:
            time.sleep(2)
            
            # ÉTAPE 1: Accéder à l'iframe TinyMCE et écrire le message
            print("    [1] Accès à l'éditeur TinyMCE...")
            
            # Attendre que l'iframe soit visible
            iframe = self.wait.until(
                EC.presence_of_element_located((By.ID, "message_ifr"))
            )
            
            # Attendre que l'iframe soit chargé
            time.sleep(1)
            
            # Basculer vers l'iframe
            self.driver.switch_to.frame(iframe)
            
            # Attendre que le corps du texte soit visible
            body = self.wait.until(
                EC.presence_of_element_located((By.ID, "tinymce"))
            )
            
            # Écrire le message
            print("    [2] Saisie du message...")
            body.send_keys(config.MESSAGE_BODY)
            time.sleep(1)
            
            # Revenir au contenu principal (sortir de l'iframe)
            self.driver.switch_to.default_content()
            
            # ÉTAPE 2: Cliquer sur le bouton "Envoyer"
            print("    [3] Clic sur 'Envoyer'...")
            send_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "send"))
            )
            send_button.click()
            time.sleep(2)
            
            print("[✓] Message envoyé avec succès!")
            
        except Exception as e:
            print(f"[!] Erreur: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def close(self):
        """Fermer le navigateur."""
        print("[*] Fermeture du navigateur...")
        try:
            self.driver.quit()
            print("[✓] Navigateur fermé")
        except:
            pass
