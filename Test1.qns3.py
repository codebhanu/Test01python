salary = input("Please enter your salary in Germany: ")
country = input("Enter the country you want to migrate to: ")

def convertSalary(salary, country):
    if country == "Canada":
        converted_salary = salary
        currency_name = "CAD"
    elif country == "USA":
        converted_salary = salary * 1.18 / 1.0
        currency_name = "USD"
    elif country == "Cambodia":
        converted_salary = salary * 4847.38 / 1.0
        currency_name = "Cambodian riel"
    elif country == "United Kingdom":
        converted_salary = salary * 0.91 / 1.0
        currency_name = "Pound Sterling"
    else:
        print("Error: Invalid country entered")
        return None
    average_salary = {
        "Canada": 64000,
        "USA": 56516,
        "Cambodia": 5649856,
        "United Kingdom": 35423
    }
    if converted_salary > average_salary[country]:
        rich_or_poor = "rich"
    else:
        rich_or_poor = "poor"
    print("You will be", rich_or_poor, "in", country, "with a salary of", round(converted_salary, 2), currency_name)


try:
    salary = float(salary.replace(",", ""))
except ValueError:
    print("Error: Invalid salary entered")
    exit()

convertSalary(salary, country)
