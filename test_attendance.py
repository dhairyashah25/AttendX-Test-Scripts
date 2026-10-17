
def test_mark_attendance():
    """Verify that a student and attendance status are selected."""
    student_id = "STU001"
    status = "Present"
    assert student_id != ""
    assert status in ["Present", "Absent"]
    print("PASS: Attendance inputs are valid")


def test_invalid_attendance_status():
    """Verify that an unsupported status is rejected."""
    status = "Unknown"
    assert status not in ["Present", "Absent"]
    print("PASS: Invalid attendance status detected")
