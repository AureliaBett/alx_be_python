from datetime import datetime, date, time, timedelta, timezone
def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    return current_date

def calculate_future_date(current_date, number_of_days):
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date)
    return future_date

if __name__ == "__main__":

    today = display_current_datetime()
    number_of_days =int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(today, number_of_days)
