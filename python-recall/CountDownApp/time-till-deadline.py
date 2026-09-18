from datetime import datetime

user_input = input("enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline_date = datetime.strptime(input_list[1], "%d.%m.%Y")
today_date = datetime.today()

time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds()/60/60)
# print(f"Dear user! Time remaining for your goal: {goal} is {time_till.days} days")
print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")
# learn python:12.08.2026

# datetime is another data type

