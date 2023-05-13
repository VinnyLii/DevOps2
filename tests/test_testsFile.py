import subprocess

def run_application():
    subprocess.run(["python", "TimeMgt.py"])

def run_tests():
    subprocess.run(["python", "test_TimeMgt.py"])

def main():
    print("Running application...")
    run_application()
    print("Running tests...")
    run_tests()
    print("Build completed successfully!")

if __name__ == "__main__":
    main()
