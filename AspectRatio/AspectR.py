"""/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */"""
import requests
from PIL import Image
from io import BytesIO
 
def aspectR(url):
    r = requests.get(url)
    img = Image.open(BytesIO(r.content))
    print(f"El aspect ratio de la imagen es: {round(img.width/120)}:{round(img.height/120)}")
    

aspectR('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')
