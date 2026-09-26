from enrollment import (
    cancel_enrollment,
    count_enrolled,
    enroll_user,
    is_user_enrolled,
)


def test_enroll_user() -> None:
    enrollments = []
    enroll_user(enrollments, 1, 1, 1)
    assert len(enrollments) == 1


def test_is_user_enrolled() -> None:
    enrollments = []
    enroll_user(enrollments, 1, 1, 1)
    assert is_user_enrolled(enrollments, 1, 1) is True
    assert is_user_enrolled(enrollments, 2, 1) is False


def test_duplicate_enrollment_forbidden() -> None:
    enrollments = []
    enroll_user(enrollments, 1, 1, 1)
    result = enroll_user(enrollments, 1, 1, 1)
    assert result is None
    assert len(enrollments) == 1


def test_cancel_enrollment() -> None:
    enrollments = []
    enroll_user(enrollments, 1, 1, 1)
    assert cancel_enrollment(enrollments, 1) is True
    assert len(enrollments) == 0


def test_count_enrolled() -> None:
    enrollments = []
    enroll_user(enrollments, 1, 1, 5)
    enroll_user(enrollments, 2, 1, 5)
    assert count_enrolled(enrollments, 5) == 2
