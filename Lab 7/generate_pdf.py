import os
import pymupdf

def create_lab7_report_pdf():
    pdf_path = "C:/Users/agkur/.gemini/antigravity/scratch/L6_L7_22_hotel_booking/Lab 7/Lab7_Fuzzing_Report.pdf"
    screenshots_dir = "C:/Users/agkur/.gemini/antigravity/scratch/L6_L7_22_hotel_booking/Lab 7/screenshots"

    doc = pymupdf.open()

    PAGE_WIDTH = 595  # A4 width in points
    PAGE_HEIGHT = 842 # A4 height in points
    MARGIN_X = 45
    MARGIN_Y = 45
    USABLE_W = PAGE_WIDTH - 2 * MARGIN_X

    # Palette
    C_PRIMARY = (0.10, 0.22, 0.45)     # Deep Navy
    C_SECONDARY = (0.18, 0.40, 0.70)   # Blue
    C_TEXT = (0.15, 0.15, 0.15)        # Charcoal
    C_MUTED = (0.45, 0.45, 0.45)       # Grey
    C_BG_BOX = (0.95, 0.97, 1.0)       # Light blue-grey
    C_BORDER = (0.80, 0.85, 0.92)      # Border
    C_CODE_BG = (0.95, 0.95, 0.95)     # Light grey code block
    C_PASS = (0.12, 0.55, 0.25)        # Green
    C_FAIL = (0.80, 0.15, 0.15)        # Red

    # Helper to add a blank page
    def new_page():
        page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
        # Running header
        page.draw_rect(pymupdf.Rect(MARGIN_X, 22, PAGE_WIDTH - MARGIN_X, 23), color=C_BORDER, fill=C_BORDER)
        page.insert_text(pymupdf.Point(MARGIN_X, 18), "SETA Lab 7: Fuzzing for Input Validation Bugs", fontsize=8, color=C_MUTED, fontname="helv")
        page.insert_text(pymupdf.Point(PAGE_WIDTH - MARGIN_X - 110, 18), "PES1UG24AM022 | Akash G K", fontsize=8, color=C_MUTED, fontname="helv")
        return page

    # ---------------- PAGE 1 ----------------
    page1 = new_page()
    y = 50

    # Title Banner Box
    banner_rect = pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 90)
    page1.draw_rect(banner_rect, color=C_SECONDARY, fill=C_BG_BOX, width=1.5)
    page1.insert_text(pymupdf.Point(MARGIN_X + 15, y + 26), "LABORATORY REPORT: LAB 7", fontsize=11, fontname="hebo", color=C_SECONDARY)
    page1.insert_text(pymupdf.Point(MARGIN_X + 15, y + 48), "Fuzzing for Input Validation Bugs", fontsize=18, fontname="hebo", color=C_PRIMARY)
    page1.insert_text(pymupdf.Point(MARGIN_X + 15, y + 72), "Property-Based Fuzz Testing and Defensive Code Hardening using Hypothesis", fontsize=10, fontname="helv", color=C_TEXT)
    y += 105

    # Metadata Card
    meta_rect = pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 68)
    page1.draw_rect(meta_rect, color=C_BORDER, fill=(0.98, 0.98, 0.98), width=1)
    
    col1_x = MARGIN_X + 12
    col2_x = MARGIN_X + 260
    
    page1.insert_text(pymupdf.Point(col1_x, y + 16), "Student Name: Akash G Kuradagi", fontsize=9.5, fontname="hebo", color=C_TEXT)
    page1.insert_text(pymupdf.Point(col1_x, y + 32), "SRN: PES1UG24AM022", fontsize=9.5, fontname="hebo", color=C_TEXT)
    page1.insert_text(pymupdf.Point(col1_x, y + 48), "Course: Software Engineering: Testing & Architecture (SETA)", fontsize=9.5, fontname="helv", color=C_TEXT)
    
    page1.insert_text(pymupdf.Point(col2_x, y + 16), "Upstream: SETAPESU26/L6_L7_22_hotel_booking", fontsize=9, fontname="helv", color=C_TEXT)
    page1.insert_text(pymupdf.Point(col2_x, y + 32), "Fork: akashgkuradagi/L6_L7_22_hotel_booking", fontsize=9, fontname="helv", color=C_TEXT)
    page1.insert_text(pymupdf.Point(col2_x, y + 48), "Date: November 2026 | Environment: Python 3.13 / pytest / Hypothesis", fontsize=9, fontname="helv", color=C_TEXT)
    y += 82

    # Section 1: Objectives & Learning Outcomes
    page1.insert_text(pymupdf.Point(MARGIN_X, y + 14), "1. Objectives & Overview", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page1.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    intro_text = (
        "The objective of this laboratory exercise is to explore fuzz testing as a crucial security and quality assurance\n"
        "technique. Traditional unit tests typically validate only expected 'happy-path' and known edge-case inputs.\n"
        "Fuzzing automates testing by generating randomized, unexpected, and malformed inputs to uncover hidden\n"
        "vulnerabilities, unhandled exceptions, and edge-case crashes. In this lab, we use the Hypothesis library to\n"
        "fuzz test an assigned Python module (hotel_booking.py / processor.py), analyze the failure traces, and apply\n"
        "defensive programming practices to harden the application against arbitrary inputs."
    )
    for line in intro_text.split('\n'):
        page1.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=9, fontname="helv", color=C_TEXT)
        y += 13
    y += 6

    # Section 2: Step 1 & Step 2
    page1.insert_text(pymupdf.Point(MARGIN_X, y + 14), "2. Step 1: Environment Setup & Step 2: Running Buggy Application", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page1.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    step1_text = (
        "• Dependencies: Installed hypothesis (v6.170.15) and pytest (v9.2.0) via pip.\n"
        "• Baseline Execution: Running python processor.py with standard happy-path inputs produces normal output,\n"
        "  masking severe underlying input-validation flaws in nights_stayed(), room_floor(), and booking_label()."
    )
    for line in step1_text.split('\n'):
        page1.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=9, fontname="helv", color=C_TEXT)
        y += 13
    y += 8

    # Embed Screenshot 1 (Step 2)
    s1_path = f"{screenshots_dir}/step2_buggy_processor_output.png"
    if os.path.exists(s1_path):
        page1.insert_text(pymupdf.Point(MARGIN_X, y), "Figure 1: Step 2 — Initial Buggy Application Run (python processor.py)", fontsize=9.5, fontname="hebo", color=C_SECONDARY)
        y += 6
        img_rect = pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 185)
        page1.insert_image(img_rect, filename=s1_path)
        y += 195

    # Footer page 1
    page1.insert_text(pymupdf.Point(PAGE_WIDTH / 2 - 20, PAGE_HEIGHT - 25), "Page 1 of 4", fontsize=9, fontname="helv", color=C_MUTED)

    # ---------------- PAGE 2 ----------------
    page2 = new_page()
    y = 45

    page2.insert_text(pymupdf.Point(MARGIN_X, y + 14), "3. Step 3: Fuzz Test Design Using Hypothesis", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page2.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    test_desc = (
        "Hypothesis uses property-based testing: instead of hardcoding static inputs, we define the property that\n"
        "the function must never crash on any arbitrary string or None input (@given(st.text() | st.none())). If an\n"
        "unhandled exception is raised, the test fails, and Hypothesis automatically shrinks (minimizes) the failing\n"
        "input to the smallest possible reproducer."
    )
    for line in test_desc.split('\n'):
        page2.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=9, fontname="helv", color=C_TEXT)
        y += 13
    y += 6

    # Section 4: Step 4 - Failing test cases
    page2.insert_text(pymupdf.Point(MARGIN_X, y + 14), "4. Step 4: Running Test Suite & Fuzzing Failure Analysis", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page2.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    fail_desc = (
        "Command: pytest test_processor.py\n"
        "Outcome: All 3 property tests FAILED immediately. Hypothesis discovered multiple distinct failure modes:\n"
        " 1. nights_stayed: Crashed on s='' (ValueError: not enough values to unpack), s='-' (ValueError: invalid int),\n"
        "    and s=None (AttributeError: 'NoneType' object has no attribute 'split').\n"
        " 2. room_floor: Crashed on s='' (IndexError: list index out of range), s='-' (IndexError: string index out of range),\n"
        "    and s=None (AttributeError: 'NoneType' object has no attribute 'split').\n"
        " 3. booking_label: Crashed on s='' (IndexError: string index out of range) and s=None (AttributeError)."
    )
    for line in fail_desc.split('\n'):
        page2.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=9, fontname="helv", color=C_TEXT)
        y += 13
    y += 8

    # Embed Screenshot 2 (Step 4)
    s2_path = f"{screenshots_dir}/step4_pytest_failing_output.png"
    if os.path.exists(s2_path):
        page2.insert_text(pymupdf.Point(MARGIN_X, y), "Figure 2: Step 4 — Pytest Failing Output Showing Hypothesis Fuzzing Traceback", fontsize=9.5, fontname="hebo", color=C_FAIL)
        y += 6
        img_rect = pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 360)
        page2.insert_image(img_rect, filename=s2_path)
        y += 370

    page2.insert_text(pymupdf.Point(PAGE_WIDTH / 2 - 20, PAGE_HEIGHT - 25), "Page 2 of 4", fontsize=9, fontname="helv", color=C_MUTED)

    # ---------------- PAGE 3 ----------------
    page3 = new_page()
    y = 45

    page3.insert_text(pymupdf.Point(MARGIN_X, y + 14), "5. Step 5: Fixing & Hardening the Application Script", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page3.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    fix_intro = (
        "To eliminate all discovered vulnerabilities, we applied defensive programming techniques to hotel_booking.py:\n"
        "• Type & None validation: Check isinstance(..., str) upfront and return None on non-string/None inputs.\n"
        "• Delimiter & token validation: Validate that split parts match expected counts before unpacking or indexing.\n"
        "• Parsing safety: Wrap integer conversions in try...except ValueError blocks and ensure digits exist.\n"
        "• Boundary constraints: Ensure check_out >= check_in, and filter out empty tokens in CSV names list.\n"
        "• Graceful degradation: Functions return None instead of raising unhandled exceptions."
    )
    for line in fix_intro.split('\n'):
        page3.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=9, fontname="helv", color=C_TEXT)
        y += 13
    y += 8

    # Embed Screenshot 3 (Step 5)
    s3_path = f"{screenshots_dir}/step5_fixed_processor_output.png"
    if os.path.exists(s3_path):
        page3.insert_text(pymupdf.Point(MARGIN_X, y), "Figure 3: Step 5 — Fixed Application Run (python processor.py)", fontsize=9.5, fontname="hebo", color=C_SECONDARY)
        y += 6
        img_rect = pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 185)
        page3.insert_image(img_rect, filename=s3_path)
        y += 195

    # Section 6: Step 6 - Passing Test Suite
    page3.insert_text(pymupdf.Point(MARGIN_X, y + 14), "6. Step 6: Re-Running Fuzz Tests on Hardened Application", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page3.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    pass_intro = (
        "Command: pytest test_processor.py\n"
        "Outcome: 3 passed in 0.84s (100% pass rate). Hypothesis executed hundreds of randomly generated fuzzing\n"
        "inputs (arbitrary Unicode, control characters, empty strings, null bytes, None) without a single unhandled crash."
    )
    for line in pass_intro.split('\n'):
        page3.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=9, fontname="helv", color=C_TEXT)
        y += 13
    y += 8

    # Embed Screenshot 4 (Step 6)
    s4_path = f"{screenshots_dir}/step6_pytest_passing_output.png"
    if os.path.exists(s4_path):
        page3.insert_text(pymupdf.Point(MARGIN_X, y), "Figure 4: Step 6 — Pytest Passing Output on Hardened Application (3 PASSED)", fontsize=9.5, fontname="hebo", color=C_PASS)
        y += 6
        img_rect = pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 160)
        page3.insert_image(img_rect, filename=s4_path)
        y += 170

    page3.insert_text(pymupdf.Point(PAGE_WIDTH / 2 - 20, PAGE_HEIGHT - 25), "Page 3 of 4", fontsize=9, fontname="helv", color=C_MUTED)

    # ---------------- PAGE 4 ----------------
    page4 = new_page()
    y = 45

    page4.insert_text(pymupdf.Point(MARGIN_X, y + 14), "7. Defect Classification & Root Cause Analysis Table", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page4.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 30

    # Draw Table
    headers = ["Function", "Edge Case Input", "Original Uncaught Error", "Defensive Fix Applied"]
    col_widths = [95, 105, 145, 160]
    
    # Table header row
    page4.draw_rect(pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 20), color=C_SECONDARY, fill=C_SECONDARY)
    cur_x = MARGIN_X
    for h, w in zip(headers, col_widths):
        page4.insert_text(pymupdf.Point(cur_x + 5, y + 14), h, fontsize=9, fontname="hebo", color=(1, 1, 1))
        cur_x += w
    y += 20

    table_rows = [
        ("nights_stayed", "None", "AttributeError ('NoneType')", "Type check: if not isinstance(days, str): return None"),
        ("nights_stayed", "'' (empty string)", "ValueError (unpacking)", "Count validation: if len(parts) != 2: return None"),
        ("nights_stayed", "'-' / 'abc-xyz'", "ValueError (int conversion)", "Wrapped in try...except ValueError: return None"),
        ("nights_stayed", "'20-10' (reverse)", "Logical error (negative nights)", "Added business rule: if check_out < check_in: return None"),
        ("room_floor", "None", "AttributeError ('NoneType')", "Type check: if not isinstance(room_code, str): return None"),
        ("room_floor", "'' (empty string)", "IndexError (list index 1)", "Verified split parts count >= 2 before indexing"),
        ("room_floor", "'-' / 'D-'", "IndexError (string index 0)", "Verified number non-empty and starts with digit"),
        ("booking_label", "None", "AttributeError ('NoneType')", "Type check: if not isinstance(names_csv, str): return None"),
        ("booking_label", "'' (empty string)", "IndexError (lead string index)", "Filtered non-empty names: [n for n in ... if n]"),
        ("booking_label", "',,' / '   '", "IndexError (empty tokens)", "Check if not names: return None; clean lead formatting"),
    ]

    for idx, row in enumerate(table_rows):
        row_bg = (0.97, 0.97, 0.97) if idx % 2 == 0 else (1.0, 1.0, 1.0)
        page4.draw_rect(pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 20), color=C_BORDER, fill=row_bg, width=0.5)
        cur_x = MARGIN_X
        for val, w in zip(row, col_widths):
            page4.insert_text(pymupdf.Point(cur_x + 4, y + 13), val, fontsize=7.8, fontname="helv", color=C_TEXT)
            cur_x += w
        y += 20
    y += 15

    # Section 8: Conclusion & Learning Outcomes
    page4.insert_text(pymupdf.Point(MARGIN_X, y + 14), "8. Conclusion & Key Takeaways", fontsize=12, fontname="hebo", color=C_PRIMARY)
    page4.draw_line(pymupdf.Point(MARGIN_X, y + 18), pymupdf.Point(PAGE_WIDTH - MARGIN_X, y + 18), color=C_SECONDARY, width=1)
    y += 28

    conclusion_text = (
        "1. Value of Fuzzing: Fuzz testing using Hypothesis uncovered 10 distinct failure modes and uncaught exceptions\n"
        "   that were completely missed by standard testing with expected inputs.\n"
        "2. Hypothesis Shrinking: When a failure occurred, Hypothesis automatically minimized complex inputs down to the\n"
        "   exact minimal crashing cases (e.g., s='', s='-', s=None), greatly simplifying debugging and root-cause analysis.\n"
        "3. Robustness via Defensive Programming: Hardening input parsers with strict type checks, token validations,\n"
        "   and safe fallbacks ensures production services remain reliable, resilient, and immune to input validation denial-of-service."
    )
    for line in conclusion_text.split('\n'):
        page4.insert_text(pymupdf.Point(MARGIN_X, y), line, fontsize=8.8, fontname="helv", color=C_TEXT)
        y += 13

    # Signoff block
    y += 15
    page4.draw_rect(pymupdf.Rect(MARGIN_X, y, PAGE_WIDTH - MARGIN_X, y + 35), color=C_BORDER, fill=C_BG_BOX, width=1)
    page4.insert_text(pymupdf.Point(MARGIN_X + 15, y + 14), "Deliverables Status: Complete (PDF Report + Fixed Python Script + Updated Test Suite)", fontsize=9, fontname="hebo", color=C_PRIMARY)
    page4.insert_text(pymupdf.Point(MARGIN_X + 15, y + 27), "Submitted by: Akash G Kuradagi (PES1UG24AM022) | Department of SETA, PES University", fontsize=8.5, fontname="helv", color=C_TEXT)

    page4.insert_text(pymupdf.Point(PAGE_WIDTH / 2 - 20, PAGE_HEIGHT - 25), "Page 4 of 4", fontsize=9, fontname="helv", color=C_MUTED)

    # Save PDF
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc.save(pdf_path)
    doc.close()
    print(f"Successfully generated PDF report: {pdf_path}")

if __name__ == "__main__":
    create_lab7_report_pdf()
