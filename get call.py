import requests

response=requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=a958b916dbe0dc13aac62dfcf0d53d9b&user_id=194114747%40N03&format=json&nojsoncallback=1")

code=response.status_code

assert code==200, "Request failed"


print(response)
print(type(response))
print(dir(response))
print(response.text)
print(response.content)
print(response.json())
print(response.cookies)
print(response.headers)
print(response.url)


jsonResponse = response.json()

print(jsonResponse["photos"]["perpage"])
print(jsonResponse["stat"])
