# with open("weather_data.csv") as file:
#      datas = file.readlines()
#
# data_list = []
# for data in datas:
#     data_tup = data.strip().split(",")
#     data_list.append(data_tup)
# print(data_list)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature= []
#     i = 0
#     for row in data:
#         if i == 0:
#             i+=1
#             continue
#         i+=1
#         temperature.append(int(row[1]))
# print(temperature)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
#
# avg_temp = round(data["temp"].mean(), 2)
# max_temp = data["temp"].max()
# print(avg_temp)
# print(max_temp)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(((9*monday.temp)/5)+32)


import pandas
data = pandas.read_csv("Squirrel_Data.csv")
color_data = data["Primary Fur Color"]

gray = 0
cinnamon = 0
black = 0

for row in color_data:
    if row == "Gray":
        gray+=1
    elif row == "Black":
        black+=1
    elif row == "Cinnamon":
        cinnamon+=1

data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count":[gray, black, cinnamon]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")