from flat import Bill, Flatmates
from report import PdfReport


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2023: ")

name1 = input("What is your name? ")
days_in_house1 = int(
    input(f"How many days {name1} stay in the house durning the bill period? "))

name2 = input("What is your name? ")
days_in_house2 = int(
    input(f"How many days {name2} stay in the house durning the bill period? "))


the_bill = Bill(amount, period)
flatmate1 = Flatmates(name1, days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.peroid}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
