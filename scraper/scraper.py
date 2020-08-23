import requests
import base64
import json

with open('images.json') as jf:
	seesaw_icons = json.load(jf)
	for shortcut, img in seesaw_icons.items():
	    img_data = requests.get(img).content if not img.startswith('data:') else base64.b64decode(img.split('png;base64,')[1])
	    with open(f"../icons/{shortcut.strip(':')}.png", 'wb') as img_file:
	        img_file.write(img_data)
