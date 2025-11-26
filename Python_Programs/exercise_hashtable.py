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