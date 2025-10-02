#!/usr/bin/env python3
"""
Simple test script to verify the application structure
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print("✓ Flask imported successfully")
    except ImportError as e:
        print(f"✗ Flask import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print("✓ PIL imported successfully")
    except ImportError as e:
        print(f"✗ PIL import failed: {e}")
        return False
    
    try:
        import cv2
        print("✓ OpenCV imported successfully")
    except ImportError as e:
        print(f"✗ OpenCV import failed: {e}")
        return False
    
    try:
        import numpy
        print("✓ NumPy imported successfully")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
        return False
    
    return True

def test_directories():
    """Test if required directories exist"""
    print("\nTesting directories...")
    
    required_dirs = [
        'uploads',
        'outputs',
        'templates',
        'static/css',
        'static/js'
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✓ Directory exists: {dir_path}")
        else:
            print(f"✗ Directory missing: {dir_path}")
            all_exist = False
    
    return all_exist

def test_files():
    """Test if required files exist"""
    print("\nTesting files...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        'static/css/style.css',
        'static/js/main.js'
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ File exists: {file_path}")
        else:
            print(f"✗ File missing: {file_path}")
            all_exist = False
    
    return all_exist

def test_app_syntax():
    """Test if app.py has valid syntax"""
    print("\nTesting app.py syntax...")
    
    try:
        with open('app.py', 'r') as f:
            code = f.read()
        compile(code, 'app.py', 'exec')
        print("✓ app.py has valid Python syntax")
        return True
    except SyntaxError as e:
        print(f"✗ Syntax error in app.py: {e}")
        return False

def main():
    print("=" * 50)
    print("AI Product Promotion Editor - Test Suite")
    print("=" * 50)
    
    tests = [
        test_directories,
        test_files,
        test_app_syntax,
        test_imports
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    print("\n" + "=" * 50)
    if all(results):
        print("✓ All tests passed!")
        print("=" * 50)
        return 0
    else:
        print("✗ Some tests failed")
        print("=" * 50)
        return 1

if __name__ == '__main__':
    sys.exit(main())
