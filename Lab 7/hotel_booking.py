def nights_stayed(days):
    """
    Calculates the number of nights stayed given a day range in the format 'checkin-checkout'.
    Returns the integer count of nights, or None if input is invalid.
    """
    if not isinstance(days, str):
        return None
    days = days.strip()
    parts = days.split('-')
    if len(parts) != 2:
        return None
    try:
        check_in = int(parts[0].strip())
        check_out = int(parts[1].strip())
    except ValueError:
        return None
    if check_out < check_in:
        return None
    return check_out - check_in


def room_floor(room_code):
    """
    Extracts the floor number from a room code formatted as '<Building>-<RoomNumber>' (e.g. 'D-305').
    The floor is indicated by the first digit of the room number.
    Returns the floor as an integer, or None if input is invalid.
    """
    if not isinstance(room_code, str):
        return None
    room_code = room_code.strip()
    parts = room_code.split('-')
    if len(parts) < 2:
        return None
    number = parts[1].strip()
    if not number or not number[0].isdigit():
        return None
    return int(number[0])


def booking_label(names_csv):
    """
    Generates a booking summary label from a comma-separated list of guest names (e.g. 'ravi, priya' -> 'Ravi +1').
    Returns formatted label string, or None if input is invalid or contains no valid guest names.
    """
    if not isinstance(names_csv, str):
        return None
    names = [n.strip() for n in names_csv.split(',') if n.strip()]
    if not names:
        return None
    lead = names[0]
    capitalized_lead = lead[0].upper() + lead[1:]
    return f"{capitalized_lead} +{len(names) - 1}"


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)


if __name__ == "__main__":
    main()
