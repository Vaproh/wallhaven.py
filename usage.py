from wallhaven import WallhavenPY

client = WallhavenPY()

wall = client.search()

print(wall)

client.save_as_json(data=wall, file_path="test.json")
