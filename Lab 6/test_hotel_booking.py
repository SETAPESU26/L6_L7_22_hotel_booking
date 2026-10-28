import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# =======================================================================
# Test Suite: Unit Tests for hotel_booking
# Target: 100% Statement and 100% Branch Coverage
# =======================================================================

# -----------------------------------------------------------------------
# Tests for booking_cost(room, nights, guests, is_peak_season)
# -----------------------------------------------------------------------

def test_standard_two_nights():
    """Initial test case: 2 nights in standard room without peak or extra guests."""
    assert booking_cost("standard", 2, 2, False) == 4000


def test_booking_cost_single_night_single_guest():
    """Boundary test: 1 night, 1 guest (minimum valid input)."""
    assert booking_cost("standard", 1, 1, False) == 2000


def test_booking_cost_unknown_room_raises():
    """Verify ValueError is raised when room is not in ROOM_RATE."""
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("villa", 2, 2, False)


def test_booking_cost_zero_nights_raises():
    """Verify ValueError is raised when nights < 1 (zero nights)."""
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_booking_cost_negative_nights_raises():
    """Verify ValueError is raised when nights < 1 (negative nights)."""
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("deluxe", -2, 2, False)


def test_booking_cost_peak_season():
    """Verify 25% peak season rate increase."""
    # Deluxe rate = 3500; peak rate = 3500 + 3500 // 4 = 4375. 2 nights = 8750.
    assert booking_cost("deluxe", 2, 2, True) == 8750


def test_booking_cost_extra_guests():
    """Verify extra guest surcharge (500 per extra guest per night)."""
    # Standard: 2000 * 2 nights = 4000. 4 guests -> (4 - 2) * 500 * 2 = 2000. Total = 6000.
    assert booking_cost("standard", 2, 4, False) == 6000


def test_booking_cost_extended_stay_6_nights_no_discount():
    """Verify boundary condition: 6 nights gets no discount."""
    # Deluxe: 3500 * 6 = 21000.
    assert booking_cost("deluxe", 6, 2, False) == 21000


def test_booking_cost_extended_stay_7_nights_discount():
    """Verify boundary condition: 7 nights gets 10% discount."""
    # Suite: 6000 * 7 = 42000. Discount = 4200. Total = 37800.
    assert booking_cost("suite", 7, 2, False) == 37800


def test_booking_cost_all_modifiers_combined():
    """Verify peak season, extra guests, and extended stay all combined."""
    # Suite: 6000 + 1500 = 7500. 8 nights * 7500 = 60000.
    # Extra guests: 3 extra * 500 * 8 = 12000. Subtotal = 72000.
    # 10% discount: 7200. Total = 64800.
    assert booking_cost("suite", 8, 5, True) == 64800


# -----------------------------------------------------------------------
# Tests for cancellation_refund(amount, days_before, is_member)
# -----------------------------------------------------------------------

def test_full_refund():
    """Initial test case: >= 7 days notice yields full refund."""
    assert cancellation_refund(1000, 10, False) == 1000


def test_cancellation_refund_boundary_7_days():
    """Boundary test: exactly 7 days notice yields 100% refund."""
    assert cancellation_refund(5000, 7, False) == 5000


def test_cancellation_refund_boundary_7_days_member():
    """Boundary test: 7 days notice for member returns full amount immediately."""
    assert cancellation_refund(5000, 7, True) == 5000


def test_cancellation_refund_moderate_notice_non_member():
    """Moderate notice (2-6 days): non-member receives 50% refund."""
    # 5000 // 2 = 2500.
    assert cancellation_refund(5000, 5, False) == 2500


def test_cancellation_refund_boundary_2_days_member():
    """Boundary test: exactly 2 days notice with membership bonus (+25%)."""
    # 5000 // 2 + 5000 // 4 = 2500 + 1250 = 3750.
    assert cancellation_refund(5000, 2, True) == 3750


def test_cancellation_refund_boundary_1_day_non_member():
    """Boundary test: 1 day notice non-member receives 0 refund."""
    assert cancellation_refund(4000, 1, False) == 0


def test_cancellation_refund_late_notice_member():
    """Late notice (< 2 days): member receives 25% membership bonus refund."""
    # 0 + 4000 // 4 = 1000.
    assert cancellation_refund(4000, 0, True) == 1000


# -----------------------------------------------------------------------
# Tests for room_upgrade(room, is_member, rooms_free)
# -----------------------------------------------------------------------

def test_room_upgrade_no_rooms_free():
    """When rooms_free == 0, returns original room regardless of membership."""
    assert room_upgrade("standard", True, 0) == "standard"
    assert room_upgrade("deluxe", True, 0) == "deluxe"


def test_room_upgrade_standard_member():
    """Standard room upgrades to deluxe for members when rooms are free."""
    assert room_upgrade("standard", True, 2) == "deluxe"


def test_room_upgrade_standard_non_member():
    """Standard room stays standard for non-members."""
    assert room_upgrade("standard", False, 2) == "standard"


def test_room_upgrade_deluxe_member():
    """Deluxe room upgrades to suite for members when rooms are free."""
    assert room_upgrade("deluxe", True, 1) == "suite"


def test_room_upgrade_deluxe_non_member():
    """Deluxe room stays deluxe for non-members."""
    assert room_upgrade("deluxe", False, 1) == "deluxe"


def test_room_upgrade_suite_member():
    """Suite room remains suite for members (highest tier)."""
    assert room_upgrade("suite", True, 5) == "suite"


def test_room_upgrade_suite_non_member():
    """Suite room remains suite for non-members."""
    assert room_upgrade("suite", False, 5) == "suite"
