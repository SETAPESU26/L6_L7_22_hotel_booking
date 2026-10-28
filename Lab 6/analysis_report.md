# Lab 6: Code and Branch Coverage Analysis Report

**Student Name:** Akash G Kuradagi  
**SRN:** PES1UG24AM022  
**Department / Course:** Software Engineering: Testing and Architecture (SETA)  
**Assigned Repository:** `SETAPESU26/L6_L7_22_hotel_booking`  
**Fork Repository:** `akashgkuradagi/L6_L7_22_hotel_booking`  
**Application Under Test:** Hotel Booking System (`hotel_booking.py`)  

---

## 1. Executive Summary

This laboratory exercise focuses on understanding, measuring, and systematically improving **Code (Line) Coverage** and **Branch Coverage** for the assigned Python module `hotel_booking.py`. 

Using Python's `coverage.py` and `pytest` testing frameworks:
- **Baseline (Initial):** 44% Line Coverage, 37% Branch Coverage.
- **Code Coverage Target ($\ge 90\%$):** Achieved **100% Statement Coverage** (32/32 statements in `hotel_booking.py`, 73/73 total).
- **Branch Coverage Target ($\ge 90\%$):** Achieved **100% Branch Coverage** (22/22 branches evaluated in `hotel_booking.py`, 103/103 total statements & branches).

---

## 2. Theoretical Background: Line vs. Branch Coverage

| Metric | Definition | Limitation |
| :--- | :--- | :--- |
| **Line / Statement Coverage** | Measures the percentage of executable statements executed at least once during test execution. | Fails to detect whether decision logic evaluated to alternate outcomes (e.g., an `if` condition without an `else` might only ever evaluate to `True`, ignoring the `False` fallthrough path). |
| **Branch / Decision Coverage** | Measures whether every control structure (`if`, `elif`, `else`, `while`) evaluated to both `True` and `False` outcomes. | Requires systematically testing all logical edges of the control-flow graph (CFG), including boundary conditions and compound boolean sub-expressions. |

---

## 3. Architecture of Application Under Test (`hotel_booking.py`)

The application consists of three core business logic functions:

### 3.1 `booking_cost(room, nights, guests, is_peak_season)`
- **Validates Input:**
  - Checks if `room` exists in `ROOM_RATE = {"standard": 2000, "deluxe": 3500, "suite": 6000}`. If not, raises `ValueError("unknown room")`.
  - Checks if `nights < 1`. If so, raises `ValueError("invalid nights")`.
- **Peak Season Surcharge:** If `is_peak_season` is `True`, rate increases by 25% (`rate += rate // 4`).
- **Extra Guest Surcharge:** If `guests > 2`, adds `(guests - 2) * 500 * nights`.
- **Extended Stay Discount:** If `nights >= 7`, discounts 10% (`total -= total // 10`).

### 3.2 `cancellation_refund(amount, days_before, is_member)`
- **Tier 1 ($\ge 7$ days):** Full refund (`100%`).
- **Tier 2 ($2 \le \text{days} < 7$):** Half refund (`50%`).
- **Tier 3 ($< 2$ days):** No refund (`0%`).
- **Membership Bonus:** If `is_member` is `True`, adds an extra `25%` bonus refund (`amount // 4`), applicable in Tiers 2 and 3.

### 3.3 `room_upgrade(room, is_member, rooms_free)`
- **Availability Gate:** If `rooms_free == 0`, returns the requested room unchanged.
- **Standard Upgrade:** If `room == "standard"` and `is_member`, upgrades to `"deluxe"`.
- **Deluxe Upgrade:** If `room == "deluxe"` and `is_member`, upgrades to `"suite"`.
- **Fallback:** Returns existing room unchanged.

---

## 4. Initial Baseline Coverage Analysis

### 4.1 Initial Test Suite (`test_hotel_booking.py`)
The starter repository provided two basic test cases:
1. `test_standard_two_nights()`: Covered standard booking for 2 nights off-peak.
2. `test_full_refund()`: Covered early cancellation ($\ge 7$ days).

### 4.2 Baseline Results
```text
Name                    Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------
hotel_booking.py           32     18     22      6    37%   6, 8, 11, 14, 16, 23-29, 33-39
test_hotel_booking.py       6      0      0      0   100%
-------------------------------------------------------------------
TOTAL                      38     18     22      6    43%
```

- **Line Coverage:** 44% (18 lines missed).
- **Branch Coverage:** 37% (16 of 22 branch outcomes missed).
- **Untested Logic:** Error handling, peak season, guest surcharge, duration discounts, moderate and late cancellation refunds, membership bonuses, and all room upgrade scenarios.

---

## 5. Code Coverage Analysis & Test Design

### 5.1 Test Suite Implementation (`CodeCoverageTest_hotel_booking.py`)
To reach $\ge 90\%$ statement coverage, 13 targeted test cases were implemented:

1. `test_booking_cost_standard_regular`: Executes base execution path (lines 4, 5, 7, 9, 10, 12, 13, 15, 17).
2. `test_booking_cost_unknown_room_raises_value_error`: Executes exception handling line 6.
3. `test_booking_cost_invalid_nights_raises_value_error`: Executes exception handling line 8.
4. `test_booking_cost_peak_season`: Executes peak surcharge line 11.
5. `test_booking_cost_extra_guests`: Executes extra guest surcharge line 14.
6. `test_booking_cost_extended_stay_discount`: Executes long stay discount line 16.
7. `test_cancellation_refund_early_notice`: Executes full refund lines 21-22.
8. `test_cancellation_refund_moderate_notice_member`: Executes moderate notice & member bonus lines 23-24, 27-28, 29.
9. `test_cancellation_refund_late_notice_non_member`: Executes late cancellation lines 25-26, 29.
10. `test_room_upgrade_no_rooms_available`: Executes availability check lines 33-34.
11. `test_room_upgrade_standard_member`: Executes standard upgrade lines 35-36.
12. `test_room_upgrade_deluxe_member`: Executes deluxe upgrade lines 37-38.
13. `test_room_upgrade_suite_or_non_member`: Executes fallback return line 39.

### 5.2 Code Coverage Execution & Verification
```bash
coverage erase
coverage run -m pytest CodeCoverageTest_hotel_booking.py
coverage report -m
```

**Output:**
```text
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
CodeCoverageTest_hotel_booking.py      41      0   100%
hotel_booking.py                       32      0   100%
-----------------------------------------------------------------
TOTAL                                  73      0   100%
```

**Achieved Coverage:** **100% Line Coverage** (Threshold: $\ge 90\%$).

Screenshot saved at: `code_coverage_screenshot.png`

---

## 6. Branch Coverage Analysis & Test Design

### 6.1 Systematic Branch Matrix
Every decision point has been mapped to verify both `True` and `False` branch evaluation:

| Function | Line | Decision Expression | True Branch Test Case | False Branch Test Case |
| :--- | :--- | :--- | :--- | :--- |
| `booking_cost` | 5 | `room not in ROOM_RATE` | `test_booking_cost_room_not_in_room_rate_branch_true` | `test_booking_cost_standard_all_false_branches` |
| `booking_cost` | 7 | `nights < 1` | `test_booking_cost_nights_less_than_1_branch_true` | `test_booking_cost_standard_all_false_branches` |
| `booking_cost` | 10 | `is_peak_season` | `test_booking_cost_peak_season_branch_true` | `test_booking_cost_standard_all_false_branches` |
| `booking_cost` | 13 | `guests > 2` | `test_booking_cost_extra_guests_branch_true` (guests=3) | `test_booking_cost_guests_single_guest_branch_false` (guests=1, 2) |
| `booking_cost` | 15 | `nights >= 7` | `test_booking_cost_extended_stay_boundary_7_nights_branch_true` (nights=7) | `test_booking_cost_extended_stay_boundary_6_nights_branch_false` (nights=6) |
| `cancellation_refund` | 21 | `days_before >= 7` | `test_cancellation_refund_days_gte_7_non_member_branch_true` (days=7) | `test_cancellation_refund_moderate_boundary_6_days_non_member` (days=6) |
| `cancellation_refund` | 23 | `days_before >= 2` | `test_cancellation_refund_moderate_boundary_2_days_member` (days=2) | `test_cancellation_refund_late_boundary_1_day_non_member` (days=1) |
| `cancellation_refund` | 27 | `is_member` | `test_cancellation_refund_moderate_boundary_2_days_member` (True) | `test_cancellation_refund_moderate_boundary_6_days_non_member` (False) |
| `room_upgrade` | 33 | `rooms_free == 0` | `test_room_upgrade_rooms_free_zero_branch_true` (rooms_free=0) | `test_room_upgrade_standard_member_branch_true` (rooms_free=1) |
| `room_upgrade` | 35 | `room == "standard" and is_member` | `test_room_upgrade_standard_member_branch_true` (T & T) | `test_room_upgrade_standard_non_member_branch` (T & F), `test_room_upgrade_deluxe_member_branch_true` (F) |
| `room_upgrade` | 37 | `room == "deluxe" and is_member` | `test_room_upgrade_deluxe_member_branch_true` (T & T) | `test_room_upgrade_deluxe_non_member_branch` (T & F), `test_room_upgrade_suite_member_branch` (F) |

### 6.2 Boundary Value Analysis (BVA)
To ensure robustness, boundary conditions were tested:
- `nights`: 0 (invalid), 1 (minimum valid stay), 6 (no discount boundary), 7 (discount boundary).
- `guests`: 1, 2 (no surcharge boundary), 3 (surcharge threshold).
- `days_before`: 0, 1 (late cancellation), 2 (moderate refund boundary), 6 (moderate upper boundary), 7 (full refund boundary).

### 6.3 Branch Coverage Execution & Verification
```bash
coverage erase
coverage run --branch -m pytest BranchCoverageTest_hotel_booking.py
coverage report -m
```

**Output:**
```text
Name                                  Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------
BranchCoverageTest_hotel_booking.py      71      0      0      0   100%
hotel_booking.py                         32      0     22      0   100%
---------------------------------------------------------------------------------
TOTAL                                   103      0     22      0   100%
```

**Achieved Coverage:** **100% Branch Coverage** (Threshold: $\ge 90\%$).

Screenshot saved at: `branch_coverage_screenshot.png`

---

## 7. Comparative Analysis: Statement vs. Branch Coverage

A common pitfall in software engineering is equating 100% line coverage with thorough testing. 

1. **Implicit Else Fallthrough:**  
   In `booking_cost`, lines 10-11:
   ```python
   if is_peak_season:
       rate += rate // 4
   ```
   If a test suite executes only when `is_peak_season == True`, statement coverage is 100% for these lines. However, the branch condition is never evaluated for `is_peak_season == False`. Branch coverage detects this omitted testing path.

2. **Short-Circuit Evaluation in Compound Conditions:**  
   In `room_upgrade`:
   ```python
   if room == "standard" and is_member:
       return "deluxe"
   ```
   Line coverage is satisfied by testing `room = "standard"` with `is_member = True`. However, branch coverage requires testing when `room == "standard"` but `is_member = False`, ensuring the second boolean operand is tested and does not erroneously trigger the upgrade.

---

## 8. Version Control & Git Commit History

In compliance with the lab rubric requiring a minimum of two structured commits:

1. **Commit 1 (Code Coverage):**
   - Added `CodeCoverageTest_hotel_booking.py` (13 test cases achieving 100% statement coverage).
   - Added `code_coverage_screenshot.png` documenting 100% terminal output.
   - Message: `Add Code Coverage test suite and terminal verification screenshot`

2. **Commit 2 (Branch Coverage & Analysis Report):**
   - Added `BranchCoverageTest_hotel_booking.py` (23 test cases achieving 100% branch coverage).
   - Added `branch_coverage_screenshot.png` documenting 100% branch report.
   - Added `analysis_report.md` with complete analysis and student identification.
   - Updated `test_hotel_booking.py` with comprehensive test cases.
   - Message: `Add Branch Coverage test suite, terminal screenshot, and comprehensive analysis report`

---

## 9. Conclusion
Both Code Coverage and Branch Coverage requirements were exceeded, reaching **100% coverage** across both metrics. All deliverables, test files, terminal screenshots, and documentation have been produced, verified, committed, and pushed to the assigned GitHub repository.
