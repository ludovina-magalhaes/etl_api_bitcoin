print("Teste dentro do Python")
import requests
print("Importação feita")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()
print(data)

