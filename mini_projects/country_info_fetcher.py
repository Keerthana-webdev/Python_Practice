import requests

country = input("Enter country: ")

url = f"https://restcountries.com/v3.1/name/{country}"

data = requests.get(url).json()

info = data[0]

print("Country:", info["name"]["common"])
print("Capital:", info["capital"][0])
print("Population:", info["population"])
print("Currency:", list(info["currencies"].keys())[0])