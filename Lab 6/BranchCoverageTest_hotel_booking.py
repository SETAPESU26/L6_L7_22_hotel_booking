import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# =======================================================================
# Test Suite 2: Branch Coverage Tests
# Target: 100% Branch Coverage (All Decision Outcomes & Edge Cases)
# =======================================================================

# -----------------------------------------------------------------------
# Function: booking_cost(room, nights, guests, is_peak_season)
# -----------------------------------------------------------------------

def test_booking_cost_room_not_in_room_rate_branch_true():
    """Branch True: room not in ROOM_RATE raises ValueError."""
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("presidential", 2, 2, False)


def test_booking_cost_nights_less_than_1_branch_true():
    """Branch True: nights < 1 (nights=0) raises ValueError."""
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_booking_cost_nights_negative_branch_true():
    """Branch True: nights < 1 (negative nights) raises ValueError."""
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", -3, 2, False)


def test_booking_cost_standard_all_false_branches():
    """All optional branches False: standard room, nights in [1, 6], guests <= 2, off-peak.
    - room not in ROOM_RATE: False
    - nights < 1: False (nights = 1)
    - is_peak_season: False
    - guests > 2: False (guests = 2)
    - nights >= 7: False (nights = 1)
    Total = 2000 * 1 = 2000
    """
    cost = booking_cost("standard", 1, 2, False)
    assert cost == 2000


def test_booking_cost_guests_single_guest_branch_false():
    """Boundary False: guests = 1 (guests <= 2)."""
    cost = booking_cost("standard", 2, 1, False)
    assert cost == 4000


def test_booking_cost_peak_season_branch_true():
    """Branch True: is_peak_season is True (+25% base rate).
    Standard: 2000 + 500 = 2500 per night * 3 = 7500.
    """
    cost = booking_cost("standard", 3, 2, True)
    assert cost == 7500


def test_booking_cost_extra_guests_branch_true():
    """Branch True: guests > 2 (boundary: guests = 3).
    Standard: 2000 * 2 = 4000; Extra: (3 - 2) * 500 * 2 = 1000; Total = 5000.
    """
    cost = booking_cost("standard", 2, 3, False)
    assert cost == 5000


def test_booking_cost_extended_stay_boundary_6_nights_branch_false():
    """Boundary False: nights = 6 (< 7, no discount).
    Deluxe: 3500 * 6 = 21000.
    """
    cost = booking_cost("deluxe", 6, 2, False)
    assert cost == 21000


def test_booking_cost_extended_stay_boundary_7_nights_branch_true():
    """Boundary True: nights = 7 (>= 7, 10% discount).
    Deluxe: 3500 * 7 = 24500. Discount = 24500 // 10 = 2450. Total = 22050.
    """
    cost = booking_cost("deluxe", 7, 2, False)
    assert cost == 22050


def test_booking_cost_suite_all_true_branches():
    """All optional branches True: suite room, peak season, extra guests, >= 7 nights.
    - Suite rate = 6000.
    - Peak season: rate += 6000 // 4 = 1500 -> rate = 7500.
    - Total base: 7500 * 8 nights = 60000.
    - Extra guests: (4 - 2) * 500 * 8 = 8000 -> total = 68000.
    - Extended stay discount: 68000 // 10 = 6800 -> total = 61200.
    """
    cost = booking_cost("suite", 8, 4, True)
    assert cost == 61200


# -----------------------------------------------------------------------
# Function: cancellation_refund(amount, days_before, is_member)
# -----------------------------------------------------------------------

def test_cancellation_refund_days_gte_7_non_member_branch_true():
    """Branch True: days_before >= 7 (boundary: 7 days) returns full amount."""
    refund = cancellation_refund(8000, 7, False)
    assert refund == 8000


def test_cancellation_refund_days_gte_7_member_branch_true():
    """Branch True: days_before >= 7 (10 days) returns full amount (early exit)."""
    refund = cancellation_refund(8000, 10, True)
    assert refund == 8000


def test_cancellation_refund_moderate_boundary_6_days_non_member():
    """Boundary: days_before = 6 (days_before >= 2 True, is_member False).
    Refund = 6000 // 2 = 3000.
    """
    refund = cancellation_refund(6000, 6, False)
    assert refund == 3000


def test_cancellation_refund_moderate_boundary_2_days_member():
    """Boundary: days_before = 2 (days_before >= 2 True, is_member True).
    Refund = 6000 // 2 + 6000 // 4 = 3000 + 1500 = 4500.
    """
    refund = cancellation_refund(6000, 2, True)
    assert refund == 4500


def test_cancellation_refund_late_boundary_1_day_non_member():
    """Boundary False: days_before = 1 (days_before < 2, is_member False).
    Refund = 0.
    """
    refund = cancellation_refund(4000, 1, False)
    assert refund == 0


def test_cancellation_refund_late_boundary_0_days_member():
    """Boundary: days_before = 0 (days_before < 2, is_member True).
    Refund = 0 + 4000 // 4 = 1000.
    """
    refund = cancellation_refund(4000, 0, True)
    assert refund == 1000


# -----------------------------------------------------------------------
# Function: room_upgrade(room, is_member, rooms_free)
# -----------------------------------------------------------------------

def test_room_upgrade_rooms_free_zero_branch_true():
    """Branch True: rooms_free == 0 returns original room immediately."""
    result = room_upgrade("standard", True, 0)
    assert result == "standard"


def test_room_upgrade_standard_member_branch_true():
    """Branch: room == 'standard' (True) and is_member (True) -> 'deluxe'."""
    result = room_upgrade("standard", True, 1)
    assert result == "deluxe"


def test_room_upgrade_standard_non_member_branch():
    """Branch: room == 'standard' (True) and is_member (False) -> returns 'standard'."""
    result = room_upgrade("standard", False, 1)
    assert result == "standard"


def test_room_upgrade_deluxe_member_branch_true():
    """Branch: room == 'deluxe' (True) and is_member (True) -> 'suite'."""
    result = room_upgrade("deluxe", True, 2)
    assert result == "suite"


def test_room_upgrade_deluxe_non_member_branch():
    """Branch: room == 'deluxe' (True) and is_member (False) -> returns 'deluxe'."""
    result = room_upgrade("deluxe", False, 2)
    assert result == "deluxe"


def test_room_upgrade_suite_member_branch():
    """Branch: room == 'suite' (not standard, not deluxe) and is_member True -> returns 'suite'."""
    result = room_upgrade("suite", True, 3)
    assert result == "suite"


def test_room_upgrade_suite_non_member_branch():
    """Branch: room == 'suite' and is_member False -> returns 'suite'."""
    result = room_upgrade("suite", False, 3)
    assert result == "suite"
