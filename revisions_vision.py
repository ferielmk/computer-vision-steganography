
import cv2

# Charger l'image d'origine
img_avant = cv2.imread("fifi-angry.png", 0)
if img_avant is None:
    print("Erreur lors du chargement de l'image")
    exit(0)

# Sauvegarder l'image d'origine
cv2.imwrite("image_apres.jpg", img_avant)

# Charger l'image avec le message caché
img_apres = cv2.imread("image_apres.jpg", 0)
h, w = img_apres.shape

# Message à cacher
message_secret = "this is a secret"
code_ascii = [ord(caractere) for caractere in message_secret]

# Cacher le message dans les bits de poids faible des pixels
message_index = 0
for i in range(h):
    for j in range(w):
        pixel_value = img_apres[i, j]
        
        # Extraire le poids fort du pixel
        poids_fort = pixel_value & ~1  # Effacer le poids faible
        
        # Vérifier s'il reste des caractères à cacher
        if message_index < len(code_ascii):
            # Récupérer le prochain caractère du message
            caractere_a_cacher = code_ascii[message_index]
            # Mettre à jour le poids faible du pixel
            nouveau_pixel_value = poids_fort | (caractere_a_cacher & 1)
            img_apres[i, j] = nouveau_pixel_value
            message_index += 1
        else:
            break  # Si tous les caractères ont été cachés, sortir de la boucle

# Enregistrez l'image avec le message caché
cv2.imwrite("image_with_hidden_message.jpg", img_apres)

# Extraire le message caché
texte_decouvert = ""
message_index = 0
max_message_length = len(code_ascii)

for i in range(h):
    for j in range(w):
        if message_index >= max_message_length:
            break
        
        pixel_value = img_apres[i, j]
        
        # Extraire le poids faible (le dernier bit)
        poids_faible = pixel_value & 1
        
        # Ajouter le bit au message
        texte_decouvert += str(poids_faible)
        message_index += 1

# Convertir les octets en caractères ASCII
message = ""
while texte_decouvert:
    octet = texte_decouvert[:8]
    texte_decouvert = texte_decouvert[8:]
    message += chr(int(octet, 2))

print("Message caché extrait :", message)
