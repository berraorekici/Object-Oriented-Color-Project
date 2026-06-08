import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.color_base import InvalidColorValueError

print("=== RUNNING: Base Color & Exception Test ===")
print("\nTesting Custom Exception triggering:")
try:  
    raise InvalidColorValueError("Testing our custom security alarm!")
except InvalidColorValueError as e:
    print(f"✅ Success: Custom exception works perfectly! Message: {e}")

print("\n=== Base Color Test Completed ===")