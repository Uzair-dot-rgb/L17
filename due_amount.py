def calculate_due_amount(total_amount, paid_amount):
    '''Calculate the due amount based on total and paid amounts.'''
    return total_amount - paid_amount
if __name__ == "__main__":
    total = 150.0
    paid = 45.5
    due = calculate_due_amount(total, paid)
    print(f"Total Amount: {total}, Paid Amount: {paid}, Due Amount: {due}")