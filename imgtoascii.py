from PIL import Image
import pystyle
from pystyle import Colors, Colorate

intro = """
{+}-------------------------------------------------------------------{+}
                            *Image to ASCII*
{+}-------------------------------------------------------------------{+}

╔═════════════════════╗
║╔═══════════════════╗║
║║  ║Dev in python║  ║║
║║  ╔════════════════╝║
║║  ╠═════════════════╝
║╚══╣> @2025
╚═══╝> @ByMavtur
"""

def image_to_ascii(image_path, output_width=100):
    image = Image.open(image_path).convert('L')
    width, height = image.size
    aspect_ratio = height / width
    output_height = int(aspect_ratio * output_width * 0.55)
    image = image.resize((output_width, output_height))
    pixels = list(image.getdata())
    ascii_chars = "@%#*+=-:. "
    ascii_art = "\n".join(
        "".join(ascii_chars[pixel // 32] for pixel in pixels[i:i + output_width])
        for i in range(0, len(pixels), output_width)
    )
    return ascii_art

def main():
    while True:
        print(Colorate.Horizontal(Colors.blue_to_purple, intro))
        image_path = input("\nEntrer le chemin vers l'image : ")
        try:
            ascii_art = image_to_ascii(image_path)
            print("\n" + ascii_art)
        except Exception as e:
            print(f"Erreur : {e}")
        continuer = input("\nConvertir une autre image ? (y/n) : ").strip().lower()
        if continuer != 'y':
            break

if __name__ == "__main__":
    main()
