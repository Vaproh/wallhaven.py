from wallhaven import WallhavenPY

client = WallhavenPY(api_key="api key here")
collection_data = client.get(endpoint="collections")
print(collection_data)

search_results = client.search(
    categories="111", purity="100", sorting="random", order="desc", page=1
)
print(search_results)
