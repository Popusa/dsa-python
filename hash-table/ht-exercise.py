arr = []
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")

print(sum(arr[0:7])/len(arr[0:7]))

print(max(arr[0:10]))

weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")

print(weather_dict)

print(weather_dict['Jan 9'])

print(weather_dict['Jan 4'])