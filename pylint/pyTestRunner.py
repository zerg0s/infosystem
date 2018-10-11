import sys
import unittest

print("[from Py:] Started:")
print("\n".join(sys.argv))
testFile = "test_file"

if len(sys.argv) < 2:
    tests = unittest.TestLoader().discover(".\\")

    result = unittest.TextTestRunner(verbosity=2).run(tests)
    fails = []
    if result.failures == fails:
        print("OK")
    else:
        print(result.failures)