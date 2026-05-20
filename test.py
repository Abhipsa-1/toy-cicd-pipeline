print("Checking Python system logic...")

execution_result = 2 + 2
expected_result = 4

if execution_result == expected_result:
    print("SUCCESS: 2 + 2 equals 4. Python systems operational! ✅")
    exit(0) # 0 tells GitHub Actions everything passed perfectly
else:
    print(f"FAILURE: Expected {expected_result} but got {execution_result} ❌")
    exit(1) # 1 tells GitHub Actions that something broke!
