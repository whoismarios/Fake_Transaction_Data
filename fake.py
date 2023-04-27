import csv
from faker import Faker

fake = Faker()

# Define the number of transactions to generate
num_transactions = 1000

# Create a list of transactions
transactions = []
for i in range(num_transactions):
    # Generate fake data for each transaction
    name = fake.name()
    date = fake.date_between(start_date='-1y', end_date='today')
    amount = fake.pyfloat(left_digits=3, right_digits=2, positive=True)
    category = fake.random_element(elements=('Food', 'Transport', 'Entertainment', 'Shopping', 'Bills'))

    # Append the transaction to the list
    transactions.append([name, date, amount, category])

# Export the transactions to a CSV file
with open('transactions.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name', 'Date', 'Amount', 'Category'])  # Write the header row
    for transaction in transactions:
        writer.writerow(transaction)
