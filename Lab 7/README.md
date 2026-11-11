# L6_L7_22_hotel_booking — Hotel Booking

Lab 7: Fuzz Testing for Input Validation Bugs

## About
Explores property-based fuzz testing using Python's **Hypothesis** framework to identify, analyze, and defensively harden input validation edge cases.

## Files

| File | Description |
|------|-------------|
| `hotel_booking.py` | Fixed, hardened application module |
| `processor.py` | Compatibility shim for `hotel_booking.py` |
| `test_hotel_booking.py` | Property-based fuzz test suite using Hypothesis |
| `test_processor.py` | Compatibility shim for `test_hotel_booking.py` |
| `analysis_report.md` | Comprehensive lab analysis report with embedded screenshots |
| `Lab7_Fuzzing_Report.pdf` | Formatted PDF submission document containing all screenshots and analysis |
| `screenshots/` | High-resolution terminal execution screenshots for Steps 2, 4, 5, and 6 |

## Quick Start

### 1. Run Application
```bash
python hotel_booking.py
# or
python processor.py
```

### 2. Run Fuzz Tests
```bash
pytest test_hotel_booking.py
# or
pytest test_processor.py
```
