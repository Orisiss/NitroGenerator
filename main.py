import requests
import secrets
import hashlib
from tkinter import Tk, filedialog
url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
    "authority": "api.discord.gx.games",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v=1"05";"Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
}

def create_link(file_path):
    cryptomatic_hash = secrets.token_hex(32)

    data = {
        "partnerUserId": cryptomatic_hash
    }

    response = requests.post(url, headers=headers, json=data)

    link = "https://discord.com/billing/partner-promotions/1180231712274387115/" + response.text
    pureLink = link.replace('{"token":"', '').replace('"}', '').replace('token:', '')

    with open(file_path, "a") as file:
        file.write(pureLink + "\n")

def generate_links_infinite(file_path):
    try:
        while True:
            create_link(file_path)
    except KeyboardInterrupt:
        print("Programme arrêté par l'utilisateur.")

def generate_links_count(file_path):
    try:
        count = int(input("Entrez le nombre de liens à créer : "))
        for _ in range(count):
            create_link(file_path)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except KeyboardInterrupt:
        print("Programme arrêté par l'utilisateur.")

choice = input("Tapez 1 pour générer des liens à l'infini ou 2 pour choisir le nombre de liens à créer : ")
if choice == "1":
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    generate_links_infinite(file_path)
elif choice == "2":
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    generate_links_count(file_path)
else:
    print("Choix invalide.")
