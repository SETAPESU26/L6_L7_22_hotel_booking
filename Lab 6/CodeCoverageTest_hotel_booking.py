import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# ==========================================
# Test Suite 1: Line / Code Coverage Tests
# Target: 100% Statement Coverage
# ==========================================

def test_booking_cost_standard_regular():
    """Test standard room booking under regular conditions to cover base lines."""
    # 2 nights * 2000 = 4000
    cost = booking_cost("standard", 2, 2, False)
    assert cost == 4000


def test_booking_cost_unknown_room_raises_value_error():
    """Test line 6: raise ValueError('unknown room') when room not in ROOM_RATE."""
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("penthouse", 3, 2, False)


def test_booking_cost_invalid_nights_raises_value_error():
    """Test line 8: raise ValueError('invalid nights') when nights < 1."""
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_booking_cost_peak_season():
    """Test line 11: rate increase during peak season (+25%)."""
    # Deluxe: 3500 + 3500 // 4 = 3500 + 875 = 4375 * 2 nights = 8750
    cost = booking_cost("deluxe", 2, 2, True)
    assert cost == 8750


def test_booking_cost_extra_guests():
    """Test line 14: extra guest surcharge when guests > 2."""
    # Standard: 2000 * 2 = 4000 + (4 - 2) * 500 * 2 = 4000 + 2000 = 6000
    cost = booking_cost("standard", 2, 4, False)
    assert cost == 6000


def test_booking_cost_extended_stay_discount():
    """Test line 16: 10% discount for extended stay >= 7 nights."""
    # Suite: 6000 * 7 nights = 42000. 10% discount = 4200. Total = 37800
    cost = booking_cost("suite", 7, 2, False)
    assert cost == 37800


def test_cancellation_refund_early_notice():
    """Test lines 21-22: full refund when cancelled >= 7 days before."""
    refund = cancellation_refund(10000, 7, False)
    assert refund == 10000


def test_cancellation_refund_moderate_notice_member():
    """Test lines 23-24 & 27-28: half refund + member bonus for 2 <= days < 7."""
    # 5000 // 2 = 2500; Member bonus: 5000 // 4 = 1250; Total = 3750
    refund = cancellation_refund(5000, 3, True)
    assert refund == 3750


def test_cancellation_refund_late_notice_non_member():
    """Test lines 25-26 & 29: zero refund when cancelled < 2 days before."""
    refund = cancellation_refund(5000, 1, False)
    assert refund == 0


def test_room_upgrade_no_rooms_available():
    """Test lines 33-34: return unchanged room when rooms_free == 0."""
    result = room_upgrade("standard", True, 0)
    assert result == "standard"


def test_room_upgrade_standard_member():
    """Test lines 35-36: upgrade standard to deluxe for member."""
    result = room_upgrade("standard", True, 3)
    assert result == "deluxe"


def test_room_upgrade_deluxe_member():
    """Test lines 37-38: upgrade deluxe to suite for member."""
    result = room_upgrade("deluxe", True, 2)
    assert result == "suite"


def test_room_upgrade_suite_or_non_member():
    """Test line 39: fallback return room when no upgrade applies."""
    result = room_upgrade("suite", True, 5)
    assert result == "suite"
