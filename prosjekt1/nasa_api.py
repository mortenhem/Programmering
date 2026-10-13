import functions
from datetime import date
import requests
import io
import matplotlib.pyplot as plt
from PIL import Image


def main():
	"""Show Astronomy picture of the day from NASA."""
	# Get API-key
	apikey = functions.get_env_property("NASA_API_KEY").strip()

	# Build url
	url = f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/"

	params = {"media_type": "image","date": str(date.today()), "api_key": apikey}		

	data = functions.get_request(url, params)
	
	# Today
	data = data[0]

	title = data["title"]
	image_url = data["hdurl"]
	explanation = data["explanation"]
	media_type = data["media_type"]
	today = data["date"]

	# Check media type
	if media_type == "image":
		
		fetch_image = requests.get(image_url)
		img = Image.open(io.BytesIO(fetch_image.content))
	else:
		print("No picture today.")		
	# Show
	plt.figure(figsize=(10, 10))
	plt.imshow(img)
	plt.title(f"{title} {today}", fontsize=15)
	plt.show()

if __name__=="__main__":
	main()
