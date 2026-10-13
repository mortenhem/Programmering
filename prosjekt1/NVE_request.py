from functions import get_request, get_env_property



def main():


	apikey = get_env_property("NVE_API_KEY")
	
	#url = "https://hydapi.nve.no/api/v1/Parameters"
	url = "https://hydapi.nve.no/api/v1/Stations"
	
	headers = {
			"accept": "application/json",
			"X-API-Key": apikey,
			}
	
	response = get_request(url, headers)

	
	data = response["data"]
	
	for k in range(10):
		station = data[k]
		id_ = station["stationId"]
		name = station["stationName"]
		river_name = station["riverName"]
		county = station["countyName"]
		area = station["areaReservoirs"]	
	
		

		# Skriver ut informasjon om det 10 første stasjonene.

		print("---------------------------")
		print(f"Navn: {name}(id-{id_})")
		print(f"Elv : {river_name}")
		print(f"Fylke: {county}")
		print(f"Areal: {area}")
		








if __name__=="__main__":
	
	main()




