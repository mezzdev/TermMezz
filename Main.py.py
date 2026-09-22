from google import genai
from colorama import Fore, init
import getpass

init(autoreset=True)

WHITE = Fore.WHITE
RED = Fore.RED
GREEN = Fore.GREEN

print(WHITE + "=== TermMezz ===\n")
api_key = getpass.getpass("Entre ta clé API ( Gemini ) : ")

if not api_key:
    print(RED + "[!] Clé API manquante, va sur le site de Gemini pour t'en prendre une..")
    raise SystemExit

try:
    client = genai.Client(api_key=api_key)

except Exception as e:
    print(RED + "[!] Erreur :", e)
    raise SystemExit

while True:
    message = input(WHITE + "> ")

    if message.lower() == "quitter":
        print(RED + "[!] Fermeture de TermMezz...")
        break

    if not message.strip():
        continue

    try:
        response = client.models.generate_content(
    model="gemini-3.6-flash", 
    contents=message
)
 
        print(
    + GREEN
    + "TermMezz : "
    + WHITE
    + response.text
)

    except Exception as e:
        print(RED + "[!] Erreur API :", e)