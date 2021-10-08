import requests

response=requests.post("https://www.flickr.com/services/rest/?method=flickr.blogs.postPhoto&api_key=1eecff9b9ad0216ec7fe11768e88270c&oauth_token=72157720817611623-1dc7afa74b39c1e5")

code=response.status_code
print(code)

assert code==200, "Request failed"


print(response)
