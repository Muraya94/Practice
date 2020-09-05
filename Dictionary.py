monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December", }

print(monthConversions.get("Nov"))
print(monthConversions["Dec"])
print(monthConversions.get("Huy"))
print(monthConversions.get("Huy", "Not a valid key."))
