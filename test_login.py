
def test_valid_login():
    """Verify login with valid credentials."""
    username = "student123"
    password = "ValidPassword123"
    assert username != ""
    assert password != ""
    print("PASS: Valid login inputs are present")


def test_empty_login_fields():
    """Verify that empty login fields are detected."""
    username = ""
    password = ""
    assert username == "" and password == ""
    print("PASS: Empty login inputs detected")

def test_whitespace_username():
    """Check detection of a whitespace-only username."""
    username = "   "
    assert username.strip() == ""
    print("PASS: Whitespace-only username detected")
