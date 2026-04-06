import google.generativeai as genai
import PIL.Image
import os
import sys

# Configuration de l'API via les Secrets GitHub
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Erreur : La clé GEMINI_API_KEY est manquante dans les Secrets GitHub.")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def run_hashtag_generator():
    upload_dir = "uploads/"
    
    # Vérifier si le dossier existe et contient des images
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
        print("Dossier 'uploads' créé. Ajoute une image dedans pour l'analyse.")
        return

    # Lister les images (.jpg, .png, .jpeg)
    files = [f for f in os.listdir(upload_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    
    if not files:
        print("Aucune image trouvée dans le dossier /uploads.")
        return

    # On prend la dernière image ajoutée
    latest_image_path = os.path.join(upload_dir, files[-1])
    print(f"📸 Analyse de l'image : {latest_image_path}")
    
    try:
        img = PIL.Image.open(latest_image_path)
        
        prompt = """
        Agis comme un expert en algorithme TikTok. 
        Analyse cette image issue d'une vidéo.
        1. Détermine la niche précise (ex: Manga, Gaming, Tech, Business).
        2. Donne les 5 meilleurs hashtags TikTok pour maximiser les vues.
        Format : #tag1 #tag2 #tag3 #tag4 #tag5
        """
        
        response = model.generate_content([prompt, img])
        
        print("\n" + "="*30)
        print("🚀 TES 5 HASHTAGS OPTIMISÉS :")
        print("="*30)
        print(response.text)
        print("="*30)

    except Exception as e:
        print(f"Erreur d'analyse : {e}")

if __name__ == "__main__":
    run_hashtag_generator()
