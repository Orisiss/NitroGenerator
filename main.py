import requests
"""
Discord nitro link generator.

Imports requests to make API calls, secrets and hashlib 
to generate random hashes, tkinter for the GUI, 
and os for file handling.

Contains functions to:

- Generate a nitro link and save it to a file
- Generate infinite links or a set number of links
- Open a GUI to select files and control link generation
- Handle starting and stopping link generation
"""
import secrets
import hashlib
from tkinter import Tk, filedialog, Label, Button, StringVar, Entry, messagebox

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

stop_generation = False

def create_link(file_path):
    global stop_generation

    cryptomatic_hash = secrets.token_hex(32)

    data = {
        "partnerUserId": cryptomatic_hash
    }

    response = requests.post(url, headers=headers, json=data)

    link = "https://discord.com/billing/partner-promotions/1180231712274387115/" + response.text
    pureLink = link.replace('{"token":"', '').replace('"}', '').replace('token:', '')

    with open(file_path, "a") as file:
        file.write(pureLink + "\n")

    if stop_generation:
        stop_generation = False

def generate_links_infinite(file_path):
    global stop_generation

    try:
        while True:
            if stop_generation:
                break
            create_link(file_path)
    except KeyboardInterrupt:
        messagebox.showinfo("Arrêt", "Programme arrêté par l'utilisateur.")

def generate_links_count(file_path, count):
    try:
        for _ in range(count):
            create_link(file_path)
        messagebox.showinfo("Succès", "Génération de liens terminée avec succès.")
    except KeyboardInterrupt:
        messagebox.showinfo("Arrêt", "Programme arrêté par l'utilisateur.")

def stop_generation():
    global stop_generation
    stop_generation = True

def start_generation(file_path, count_entry):
    try:
        count = int(count_entry.get())
        generate_links_count(file_path, count)
    except ValueError:
        print("Veuillez entrer un nombre valide.")

def open_gui():
    root = Tk()
    root.title("Générateur de Liens Discord")
    Label(root, text="Chemin du fichier pour sauvegarder les liens :").pack()
    file_path_var = StringVar()

    def choose_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        file_path_var.set(file_path)

    Label(root, text="Choisissez un emplacement pour enregistrer les liens :").pack(pady=10)
    Entry(root, textvariable=file_path_var, state="readonly", width=50).pack(pady=10)
    
    Button(root, text="Parcourir", command=choose_file).pack(pady=10)

    Label(root, text="Nombre de liens à créer (pour l'option 2) :").pack(pady=10)
    count_entry = Entry(root)
    count_entry.pack(pady=10)

    Button(root, text="Générer des liens à l'infini", command=lambda: generate_links_infinite(file_path_var.get())).pack(pady=10)
    Button(root, text="Choisir le nombre de liens à créer", command=lambda: start_generation(file_path_var.get(), count_entry)).pack(pady=10)
    Button(root, text="Arrêter la génération", command=stop_generation).pack(pady=10)

    root.mainloop()

def main():
    choice = input("Tapez 1 pour générer des liens à l'infini ou 2 pour choisir le nombre de liens à créer : ")
    if choice == "1":
        generate_links_infinite(input("Entrez le chemin du fichier de sortie : "))
    elif choice == "2":
        count = int(input("Entrez le nombre de liens à créer : "))
        generate_links_count(input("Entrez le chemin du fichier de sortie : "), count)
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    open_gui()