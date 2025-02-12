import csv
import statistics

data = []
with open('titanic.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["Age"]:  
            data.append({
                "Survived": int(row["Survived"]),
                "Sex": row["Sex"],
                "Age": float(row["Age"])
            })

ages = sorted([row["Age"] for row in data])

#средний возраст среди 15 позиций
central_ages = ages[len(ages)//2 - 7 : len(ages)//2 + 8]
mean_age = sum(central_ages) / len(central_ages)

lower_bound = mean_age - 15
upper_bound = mean_age + 15

men_in_range = [row for row in data if row["Sex"] == "male" and lower_bound <= row["Age"] <= upper_bound]
survived_men = [row for row in men_in_range if row["Survived"] == 1]

print(f"Количество мужчин на борту в возрастном интервале {lower_bound:.2f}-{upper_bound:.2f} лет: {len(men_in_range)}")
print(f"Количество выживших мужчин в этом интервале: {len(survived_men)}")
