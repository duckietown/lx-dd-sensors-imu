"""Sanity tests for the IMU student solution.

Run from the LX root with:

    pytest tests/

These tests import ``solution.imu_math``, a pure-Python module with no
ROS dependency, so they can run both inside the editor container and
on a plain host Python.
"""

import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / 'packages' / 'solution'))

from solution.imu_math import quaternion_to_euler  # noqa: E402


def _approx(a, b, tol=1e-6):
    return abs(a - b) < tol


def test_identity_quaternion():
    roll, pitch, yaw = quaternion_to_euler(0.0, 0.0, 0.0, 1.0)
    assert _approx(roll, 0.0)
    assert _approx(pitch, 0.0)
    assert _approx(yaw, 0.0)


def test_roll_90_deg():
    s = math.sin(math.pi / 4)
    c = math.cos(math.pi / 4)
    roll, pitch, yaw = quaternion_to_euler(s, 0.0, 0.0, c)
    assert _approx(roll, math.pi / 2)
    assert _approx(pitch, 0.0)
    assert _approx(yaw, 0.0)


def test_pitch_45_deg():
    s = math.sin(math.pi / 8)
    c = math.cos(math.pi / 8)
    roll, pitch, yaw = quaternion_to_euler(0.0, s, 0.0, c)
    assert _approx(roll, 0.0)
    assert _approx(pitch, math.pi / 4)
    assert _approx(yaw, 0.0)


def test_yaw_90_deg():
    s = math.sin(math.pi / 4)
    c = math.cos(math.pi / 4)
    roll, pitch, yaw = quaternion_to_euler(0.0, 0.0, s, c)
    assert _approx(roll, 0.0)
    assert _approx(pitch, 0.0)
    assert _approx(yaw, math.pi / 2)


def _euler_to_quaternion(roll, pitch, yaw):
    """ZYX roll / pitch / yaw (rad) -> (x, y, z, w). Inverse of the function under test."""
    cr, sr = math.cos(roll / 2), math.sin(roll / 2)
    cp, sp = math.cos(pitch / 2), math.sin(pitch / 2)
    cy, sy = math.cos(yaw / 2), math.sin(yaw / 2)
    return (sr * cp * cy - cr * sp * sy,
            cr * sp * cy + sr * cp * sy,
            cr * cp * sy - sr * sp * cy,
            cr * cp * cy + sr * sp * sy)


def _rotation_matrix(roll, pitch, yaw):
    """R = Rz(yaw) @ Ry(pitch) @ Rx(roll), the ZYX convention."""
    ca, sa = math.cos(roll), math.sin(roll)
    cb, sb = math.cos(pitch), math.sin(pitch)
    cg, sg = math.cos(yaw), math.sin(yaw)
    return (
        (cg * cb, cg * sb * sa - sg * ca, cg * sb * ca + sg * sa),
        (sg * cb, sg * sb * sa + cg * ca, sg * sb * ca - cg * sa),
        (-sb, cb * sa, cb * ca),
    )


def _same_rotation(a, b, tol=1e-6):
    """Compare two roll/pitch/yaw triples by the rotation they describe."""
    ra, rb = _rotation_matrix(*a), _rotation_matrix(*b)
    return all(abs(ra[i][j] - rb[i][j]) < tol for i in range(3) for j in range(3))


def test_gimbal_lock_pitch_90():
    # pitch = +pi/2: roll and yaw are no longer separable, so the returned triple
    # cannot equal the one that built the quaternion. It must still describe the
    # same rotation, which is what this asserts.
    original = (math.radians(20.0), math.pi / 2, math.radians(50.0))
    roll, pitch, yaw = quaternion_to_euler(*_euler_to_quaternion(*original))
    assert _approx(pitch, math.pi / 2)
    assert _same_rotation((roll, pitch, yaw), original)


def test_gimbal_lock_pitch_minus_90():
    original = (math.radians(20.0), -math.pi / 2, math.radians(50.0))
    roll, pitch, yaw = quaternion_to_euler(*_euler_to_quaternion(*original))
    assert _approx(pitch, -math.pi / 2)
    assert _same_rotation((roll, pitch, yaw), original)


def test_round_trip_away_from_the_poles():
    # Away from gimbal lock the original angles come back unchanged.
    for roll_deg, pitch_deg, yaw_deg in [(0, 0, 0), (20, 40, 50), (-35, -60, 170),
                                         (10, 89, -120), (-90, 30, 45)]:
        original = tuple(math.radians(v) for v in (roll_deg, pitch_deg, yaw_deg))
        got = quaternion_to_euler(*_euler_to_quaternion(*original))
        assert _same_rotation(got, original), (roll_deg, pitch_deg, yaw_deg)


def test_non_unit_quaternion_does_not_raise():
    # Rounding can push the asin argument outside [-1, 1] on a quaternion that is
    # not exactly unit length. Published quaternions are only unit to a few
    # decimals, so this must be handled rather than raise.
    s = math.sin(math.pi / 4) * 1.0000001
    c = math.cos(math.pi / 4) * 1.0000001
    _, pitch, _ = quaternion_to_euler(0.0, s, 0.0, c)
    assert _approx(pitch, math.pi / 2, tol=1e-3)
