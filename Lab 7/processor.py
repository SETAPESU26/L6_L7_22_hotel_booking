"""
Processor module - alias/shim for hotel_booking.py
Ensures compatibility with generic lab handout commands (python processor.py).
"""
from hotel_booking import nights_stayed, room_floor, booking_label, main

if __name__ == "__main__":
    main()
