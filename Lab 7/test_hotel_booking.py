from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label

@given(st.text() | st.none())
def test_nights_stayed_no_crash(s):
    try:
        nights_stayed(s)
    except Exception as e:
        assert False, f"nights_stayed crashed with: {e}"

@given(st.text() | st.none())
def test_room_floor_no_crash(s):
    try:
        room_floor(s)
    except Exception as e:
        assert False, f"room_floor crashed with: {e}"

@given(st.text() | st.none())
def test_booking_label_no_crash(s):
    try:
        booking_label(s)
    except Exception as e:
        assert False, f"booking_label crashed with: {e}"
