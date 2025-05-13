day = input("Enter a day: ")

match day:
    case "Monday" | "mon" | "Mon":
        print("Today is Monday")
    case "Tuesday" | "tue" | "Tue":
        print("Today is Tuesday")
    case "Wednesday" | "wed" | "Wed":
        print("Today is Wednesday")
    case "Thursday" | "thu" | "Thu":
        print("Today is Thursday")
    case "Friday" | "fri" | "Fri":
        print("Today is Friday")
    case "Saturday" | "sat" | "Sat":
        print("Today is Saturday")
    case "Sunday" | "sun" | "Sun":
        print("Today is Sunday")
    case _:
        print("Invalid day")