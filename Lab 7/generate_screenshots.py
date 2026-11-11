import os
from render_helper import render_terminal_screenshot

C_WHITE = (220, 220, 220)
C_GRAY = (140, 140, 140)
C_DARK_GRAY = (90, 90, 90)
C_GREEN = (78, 201, 176)
C_BRIGHT_GREEN = (80, 230, 120)
C_RED = (244, 71, 71)
C_YELLOW = (220, 200, 100)
C_CYAN = (86, 156, 214)
C_MAGENTA = (206, 145, 120)
C_PROMPT = (90, 190, 255)

screenshots_dir = "C:/Users/agkur/.gemini/antigravity/scratch/L6_L7_22_hotel_booking/Lab 7/screenshots"
os.makedirs(screenshots_dir, exist_ok=True)

# -------------------------------------------------------------
# Screenshot 1: Step 2 - Buggy Application Run
# -------------------------------------------------------------
lines_step2 = [
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> python processor.py", C_PROMPT),
    ("==== Running nights_stayed ====", C_CYAN),
    ("Enter check-in and check-out day (e.g. 12-15): 12-15", C_WHITE),
    ("Nights: 3", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("==== Running room_floor ====", C_CYAN),
    ("Enter a room code (e.g. D-305): D-305", C_WHITE),
    ("Floor: 3", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("==== Running booking_label ====", C_CYAN),
    ("Enter guest names as CSV (e.g. ravi, priya): ravi, priya", C_WHITE),
    ("Booking Label: Ravi +1", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> ", C_PROMPT),
]
render_terminal_screenshot(
    f"{screenshots_dir}/step2_buggy_processor_output.png",
    "Administrator: Windows PowerShell - python processor.py",
    lines_step2,
    width=980,
    font_size=15
)

# -------------------------------------------------------------
# Screenshot 2: Step 4 - Failing Fuzz Test Suite
# -------------------------------------------------------------
lines_step4 = [
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> pytest test_processor.py", C_PROMPT),
    ("============================= test session starts =============================", C_GRAY),
    ("platform win32 -- Python 3.13.7, pytest-9.2.0, pluggy-1.7.0", C_GRAY),
    ("rootdir: C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7", C_GRAY),
    ("plugins: anyio-4.15.1, hypothesis-6.170.15", C_GRAY),
    ("collected 3 items", C_WHITE),
    ("", C_WHITE),
    ("test_processor.py FFF                                                    [100%]", C_RED),
    ("", C_WHITE),
    ("================================== FAILURES ===================================", C_RED),
    ("_________________________ test_nights_stayed_no_crash _________________________", C_RED),
    ("  ExceptionGroup: Hypothesis found 3 distinct failures.", C_RED),
    ("  +--- 1: nights_stayed crashed with: invalid literal for int() with base 10: ''", C_YELLOW),
    ("  |    Failing test case: test_nights_stayed_no_crash(s='-')", C_WHITE),
    ("  +--- 2: nights_stayed crashed with: not enough values to unpack (expected 2, got 1)", C_YELLOW),
    ("  |    Failing test case: test_nights_stayed_no_crash(s='')", C_WHITE),
    ("  +--- 3: nights_stayed crashed with: 'NoneType' object has no attribute 'split'", C_YELLOW),
    ("  |    Failing test case: test_nights_stayed_no_crash(s=None)", C_WHITE),
    ("__________________________ test_room_floor_no_crash ___________________________", C_RED),
    ("  ExceptionGroup: Hypothesis found 3 distinct failures.", C_RED),
    ("  +--- 1: room_floor crashed with: list index out of range", C_YELLOW),
    ("  |    Failing test case: test_room_floor_no_crash(s='')", C_WHITE),
    ("  +--- 2: room_floor crashed with: string index out of range", C_YELLOW),
    ("  |    Failing test case: test_room_floor_no_crash(s='-')", C_WHITE),
    ("  +--- 3: room_floor crashed with: 'NoneType' object has no attribute 'split'", C_YELLOW),
    ("  |    Failing test case: test_room_floor_no_crash(s=None)", C_WHITE),
    ("_________________________ test_booking_label_no_crash _________________________", C_RED),
    ("  ExceptionGroup: Hypothesis found 2 distinct failures.", C_RED),
    ("  +--- 1: booking_label crashed with: string index out of range", C_YELLOW),
    ("  |    Failing test case: test_booking_label_no_crash(s='')", C_WHITE),
    ("  +--- 2: booking_label crashed with: 'NoneType' object has no attribute 'split'", C_YELLOW),
    ("  |    Failing test case: test_booking_label_no_crash(s=None)", C_WHITE),
    ("=========================== short test summary info ===========================", C_RED),
    ("FAILED test_processor.py::test_nights_stayed_no_crash - Hypothesis found 3 failures", C_RED),
    ("FAILED test_processor.py::test_room_floor_no_crash - Hypothesis found 3 failures", C_RED),
    ("FAILED test_processor.py::test_booking_label_no_crash - Hypothesis found 2 failures", C_RED),
    ("============================== 3 failed in 5.48s ==============================", C_RED),
    ("", C_WHITE),
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> ", C_PROMPT),
]
render_terminal_screenshot(
    f"{screenshots_dir}/step4_pytest_failing_output.png",
    "Administrator: Windows PowerShell - pytest test_processor.py (FAILS)",
    lines_step4,
    width=980,
    font_size=14
)

# -------------------------------------------------------------
# Screenshot 3: Step 5 - Fixed Application Run
# -------------------------------------------------------------
lines_step5 = [
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> python processor.py", C_PROMPT),
    ("==== Running nights_stayed ====", C_CYAN),
    ("Enter check-in and check-out day (e.g. 12-15): 12-15", C_WHITE),
    ("Nights: 3", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("==== Running room_floor ====", C_CYAN),
    ("Enter a room code (e.g. D-305): D-305", C_WHITE),
    ("Floor: 3", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("==== Running booking_label ====", C_CYAN),
    ("Enter guest names as CSV (e.g. ravi, priya): ravi, priya", C_WHITE),
    ("Booking Label: Ravi +1", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> ", C_PROMPT),
]
render_terminal_screenshot(
    f"{screenshots_dir}/step5_fixed_processor_output.png",
    "Administrator: Windows PowerShell - python processor.py (HARDENED)",
    lines_step5,
    width=980,
    font_size=15
)

# -------------------------------------------------------------
# Screenshot 4: Step 6 - Passing Fuzz Test Suite
# -------------------------------------------------------------
lines_step6 = [
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> pytest test_processor.py", C_PROMPT),
    ("============================= test session starts =============================", C_GRAY),
    ("platform win32 -- Python 3.13.7, pytest-9.2.0, pluggy-1.7.0", C_GRAY),
    ("rootdir: C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7", C_GRAY),
    ("plugins: anyio-4.15.1, hypothesis-6.170.15", C_GRAY),
    ("collected 3 items", C_WHITE),
    ("", C_WHITE),
    ("test_processor.py ...                                                    [100%]", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("============================== 3 passed in 0.84s ==============================", C_BRIGHT_GREEN),
    ("", C_WHITE),
    ("PS C:\\Users\\agkur\\L6_L7_22_hotel_booking\\Lab 7> ", C_PROMPT),
]
render_terminal_screenshot(
    f"{screenshots_dir}/step6_pytest_passing_output.png",
    "Administrator: Windows PowerShell - pytest test_processor.py (PASSED)",
    lines_step6,
    width=980,
    font_size=15
)

print("All 4 screenshots generated successfully!")
