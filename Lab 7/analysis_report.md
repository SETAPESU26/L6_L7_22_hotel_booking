# Lab 7: Fuzzing for Input Validation Bugs — Analysis Report

**Student Name:** Akash G Kuradagi  
**SRN:** PES1UG24AM022  
**Department / Course:** Software Engineering: Testing and Architecture (SETA)  
**Assigned Repository:** `SETAPESU26/L6_L7_22_hotel_booking`  
**Fork Repository:** `akashgkuradagi/L6_L7_22_hotel_booking`  
**Application Under Test:** Hotel Booking Input Processor (`hotel_booking.py` / `processor.py`)  

---

## 1. Executive Summary

This laboratory exercise explores **Fuzz Testing** (property-based testing) as an automated security, reliability, and quality assurance technique. Using Python's **Hypothesis** framework and **pytest**, we test, uncover, and systematically eliminate input validation vulnerabilities in the assigned module `hotel_booking.py`.

### Key Outcomes:
- **Baseline Behavior:** The initial application works as expected when provided with standard "happy-path" inputs (e.g. `"12-15"`, `"D-305"`, `"ravi, priya"`), but harbors critical unhandled exceptions when encountering malformed, empty, or non-string inputs.
- **Fuzzing Uncovered Defects:** Automated fuzz testing with `@given(st.text() | st.none())` uncovered **10 distinct uncaught failure modes** across all three functions (`nights_stayed`, `room_floor`, and `booking_label`), resulting in immediate crashes (`ValueError`, `AttributeError`, `IndexError`).
- **Defensive Programming Hardening:** All three functions were refactored and defensively hardened against arbitrary inputs (checking types, token boundaries, and conversion safety).
- **Post-Hardening Fuzzing Results:** Re-running the property test suite achieved **100% pass rate** (3 passed in 0.84s) over hundreds of randomized Unicode strings, boundary conditions, and `None` values without a single crash.

---

## 2. Theoretical Background: Fuzz Testing vs. Unit Testing

| Dimension | Traditional Unit Testing | Fuzz / Property-Based Testing (Hypothesis) |
| :--- | :--- | :--- |
| **Input Source** | Hardcoded by developer based on assumptions | Generated dynamically across massive input spaces |
| **Coverage Scope** | Tests what the developer *thinks* could go wrong | Discovers unexpected edge cases the developer *never imagined* |
| **Test Assertion** | Specific output equals expected value (`assert f(x) == y`) | Invariant properties (e.g. `no_crash`, round-trip consistency, ordering) |
| **Failure Analysis** | Shows failure on single hardcoded input | Automatically **minimizes (shrinks)** input to smallest reproducer |
| **Security Impact** | Misses subtle parsing and injection vulnerabilities | Uncovers DoS, malformed input crashes, and boundary overflows |

---

## 3. Step-by-Step Lab Execution

### Step 1: Environment & Dependency Installation
The required dependencies for property-based fuzz testing were installed:
```bash
pip install hypothesis
pip install pytest
```
- **Hypothesis version:** `6.170.15`
- **Pytest version:** `9.2.0`
- **Python version:** `3.13.7`

---

### Step 2: Running the Buggy Application
We executed the starter script `processor.py` (`hotel_booking.py`) with standard inputs:
```text
PS C:\Users\agkur\L6_L7_22_hotel_booking\Lab 7> python processor.py
==== Running nights_stayed ====
Enter check-in and check-out day (e.g. 12-15): 12-15
Nights: 3

==== Running room_floor ====
Enter a room code (e.g. D-305): D-305
Floor: 3

==== Running booking_label ====
Enter guest names as CSV (e.g. ravi, priya): ravi, priya
Booking Label: Ravi +1
```

![Figure 1: Step 2 — Initial Buggy Application Run](screenshots/step2_buggy_processor_output.png)

*Observation:* While standard inputs succeed, none of the functions implement any input sanitization, type inspection, or length checks.

---

### Step 3: Completing the Fuzz Test Suite (`test_processor.py` / `test_hotel_booking.py`)
Using Hypothesis's `@given` decorator and composite strategies (`st.text() | st.none()`), we implemented no-crash invariant tests:

```python
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
```

---

### Step 4: Running Fuzz Tests Against Buggy Script
Executing `pytest test_processor.py` immediately exposed crashes across all three functions:

![Figure 2: Step 4 — Pytest Failing Output Showing Hypothesis Traceback](screenshots/step4_pytest_failing_output.png)

#### Detailed Hypothesis Shrinking & Failure Analysis:
1. **`nights_stayed` Failures:**
   - `s = None` $\rightarrow$ `AttributeError: 'NoneType' object has no attribute 'split'`
   - `s = ''` $\rightarrow$ `ValueError: not enough values to unpack (expected 2, got 1)`
   - `s = '-'` $\rightarrow$ `ValueError: invalid literal for int() with base 10: ''`
2. **`room_floor` Failures:**
   - `s = None` $\rightarrow$ `AttributeError: 'NoneType' object has no attribute 'split'`
   - `s = ''` $\rightarrow$ `IndexError: list index out of range` (only 1 element after split)
   - `s = '-'` $\rightarrow$ `IndexError: string index out of range` (number part is empty string `''`)
3. **`booking_label` Failures:**
   - `s = None` $\rightarrow$ `AttributeError: 'NoneType' object has no attribute 'split'`
   - `s = ''` $\rightarrow$ `IndexError: string index out of range` (lead name is empty `''`, accessing `lead[0]` fails)

---

### Step 5: Fixing and Hardening the Application Script
The application was hardened through defensive programming practices:
- **Type Safety:** Explicitly verify `isinstance(input, str)` upfront.
- **Token Count Verification:** Check length of split tokens before unpacking or indexing.
- **Conversion Safety:** Wrap string-to-integer conversions in `try...except ValueError`.
- **Domain Constraints:** Ensure `check_out >= check_in` and filter out whitespace-only names.
- **Graceful Error Handling:** Return `None` on any malformed input instead of letting unhandled exceptions crash the process.

```python
def nights_stayed(days):
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
    if not isinstance(names_csv, str):
        return None
    names = [n.strip() for n in names_csv.split(',') if n.strip()]
    if not names:
        return None
    lead = names[0]
    capitalized_lead = lead[0].upper() + lead[1:]
    return f"{capitalized_lead} +{len(names) - 1}"
```

Running the hardened application continues to work flawlessly on standard inputs:

![Figure 3: Step 5 — Fixed Application Run](screenshots/step5_fixed_processor_output.png)

---

### Step 6: Re-Running Fuzz Tests on the Hardened Application
Executing `pytest test_processor.py` on the hardened application:

```text
PS C:\Users\agkur\L6_L7_22_hotel_booking\Lab 7> pytest test_processor.py
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\agkur\L6_L7_22_hotel_booking\Lab 7
plugins: anyio-4.15.1, hypothesis-6.170.15
collected 3 items

test_processor.py ...                                                    [100%]

============================== 3 passed in 0.84s ==============================
```

![Figure 4: Step 6 — Pytest Passing Output on Hardened Application](screenshots/step6_pytest_passing_output.png)

---

## 4. Defect Classification & Root Cause Analysis

| Function | Malformed Input | Unhandled Exception (Buggy) | Root Cause | Hardened Fix |
| :--- | :--- | :--- | :--- | :--- |
| `nights_stayed` | `None` | `AttributeError` | Calling `.split()` on `NoneType` | `if not isinstance(days, str): return None` |
| `nights_stayed` | `""`, `"single"` | `ValueError` | Tuple unpacking expects 2 items, got 1 | `if len(parts) != 2: return None` |
| `nights_stayed` | `"-"`, `"a-b"` | `ValueError` | `int()` conversion fails on non-digits | `try...except ValueError: return None` |
| `nights_stayed` | `"20-10"` | Logical Error | Negative night count computed | `if check_out < check_in: return None` |
| `room_floor` | `None` | `AttributeError` | Calling `.split()` on `NoneType` | `if not isinstance(room_code, str): return None` |
| `room_floor` | `""`, `"Room"` | `IndexError` | Accessing index `[1]` on 1-element list | `if len(parts) < 2: return None` |
| `room_floor` | `"D-"`, `"-"` | `IndexError` | Accessing `number[0]` on empty string | `if not number: return None` |
| `room_floor` | `"D-ABC"` | `ValueError` | `int()` called on non-digit character | `if not number[0].isdigit(): return None` |
| `booking_label` | `None` | `AttributeError` | Calling `.split()` on `NoneType` | `if not isinstance(names_csv, str): return None` |
| `booking_label` | `""`, `",,"` | `IndexError` | `lead[0]` index error on empty token | Filter non-empty: `[n for n in ... if n]` |

---

## 5. Deliverables Verification Checklist

- [x] **Deliverable 1: PDF Document with Screenshots:** Generated and available at `Lab 7/Lab7_Fuzzing_Report.pdf`.
- [x] **Deliverable 2: Fixed Application Python Script:** Hardened implementations saved at `Lab 7/hotel_booking.py` and `Lab 7/processor.py`.
- [x] **Deliverable 3: Updated Test Suite Code:** Hypothesis fuzz tests implemented and verified at `Lab 7/test_hotel_booking.py` and `Lab 7/test_processor.py`.

---

## 6. Conclusion

Fuzz testing with Hypothesis demonstrates that programs that pass standard happy-path tests often fail catastrophically when subjected to randomized inputs. By adopting property-based testing and defensive programming, we ensure our software is resilient, secure, and production-ready.
