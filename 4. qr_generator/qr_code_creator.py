import qrcode
from .qr_code_utils import afficher_confirmation

def generer_qr_code(texte, nom_fichier='qr_code.png'):
    """
    Génère un QR code à partir du texte fourni et l'enregistre dans un fichier.
    
    :param texte: Le texte ou l'URL à convertir en QR code.
    :param nom_fichier: Le nom du fichier image dans lequel le QR code sera enregistré.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texte)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(nom_fichier)
    afficher_confirmation(nom_fichier)
