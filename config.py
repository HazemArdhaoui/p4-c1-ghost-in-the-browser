# config.py

BASE_URL = "https://essths.rnu.tn/intranet"
LOGIN_URL = "https://essths.rnu.tn/login"
MESSAGES_URL = f"{BASE_URL}/messages"

USERNAME = "type your email"
PASSWORD = "type your password"

RECIPIENT = "Alaeddine KHARRAT"
MESSAGE_SUBJECT = "Message automatique P4-C1"
MESSAGE_BODY = """Bonjour M. KHARRAT,

Ce message a été envoyé automatiquement par un script Python (Selenium)
dans le cadre du mini-projet P4-C1 : Ghost in the Browser.

Le navigateur a agi à ma place après authentification, accédant à la messagerie
et envoyant ce message sans intervention manuelle.

Ceci démontre le concept d'automatisation dans les interactions Web
et les risques associés à l'accès automatisé aux services Web.

Cordialement,
Étudiant"""

SELECTORS = {
    "username_input": "input[name='login']",
    "password_input": "input[name='password']",
    "captcha_input": "input[name='captcha_answer']",
    "login_button": "button.login-btn",
}

HEADLESS = False
