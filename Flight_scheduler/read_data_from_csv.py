import csv

with open("Flight_scheduler/data/currencyrates.csv", 'r') as file:
  lines = csv.reader(file)
  for line in lines:
    if 'Bangladeshi' in line[0]:
      l = line


taka_to_dollar = l[3]
# print(taka_to_dollar * 50)
# dollar_to_taka = l[3]
# usd_to_BDT = 50 * dollar_to_taka
# BDT_to_USD = 5000 * taka_to_dollar

# print(usd_to_BDT, BDT_to_USD)
