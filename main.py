from qr_generator.qr_code_creator import generer_qr_code

if __name__ == "__main__":
    texte = input("Entrez le texte ou l'URL à convertir en QR code : ")
    nom_fichier = input("Entrez le nom du fichier de sortie (par défaut 'qr_code.png') : ") or 'qr_code.png'
    generer_qr_code(texte, nom_fichier)
