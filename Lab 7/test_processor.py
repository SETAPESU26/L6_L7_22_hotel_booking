"""
Test processor module - alias/shim for test_hotel_booking.py
Ensures compatibility with generic lab handout commands (pytest test_processor.py).
"""
from test_hotel_booking import (
    test_nights_stayed_no_crash,
    test_room_floor_no_crash,
    test_booking_label_no_crash,
)
