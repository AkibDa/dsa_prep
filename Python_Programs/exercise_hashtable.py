arr = []

with open("nyc_weather.csv", "r") as f:
  for line in f:
    tokens = line.split(",")
    date = tokens[0]
    try:
      temperature = int(tokens[1])
      arr.append(temperature)
    except:
      print("Invalid temperature. Skipping...")
      
print(arr)
print("Max temperature:", max(arr[0:10]))

weather_dict = {}

with open("nyc_weather.csv", "r") as f:
  for line in f:
    tokens = line.split(",")
    date = tokens[0]
    try:
      temperature = int(tokens[1])
      weather_dict[date] = temperature
    except:
      print("Invalid temperature. Skipping...")
      
print(weather_dict)
print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])

count_dict = {}

with open("poem.txt", "r") as f:
  for line in f:
    words = line.split(" ")
    for word in words:
      word = word.lower().strip().replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("\"", "").replace("'", "")
      if word in count_dict:
        count_dict[word] += 1
      else:
        count_dict[word] = 1
    
print(count_dict)