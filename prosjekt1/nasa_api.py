import functions
import webbrowser
from datetime import date


def main():

	# Get API-key
	apikey = functions.get_env_property("NASA_API_KEY").strip()

	# Build url
	url = f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/"
	
		
	params = {"media_type": "image","date": str(date.today()), "api_key": apikey}		

	data = functions.get_request(url, params)
	
	image_url = data[0]["url"]
	
	webbrowser.open(image_url)
	

main()
