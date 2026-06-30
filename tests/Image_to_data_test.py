import subprocess

def run_tests(test, file):
    extension = file.split(".")[1]
    input = f"./input/test{test}.{extension}"
    expected = f"./expected_outputs/test{test}.csv"

    subprocess.run(["python", input])
    
    if(subprocess.run(["diff", "-b", f"./input/test{test}.csv" , expected], text = True, capture_output=True) == 0):
        return True
    else:
        return False

def main():
    passed = 0
    test_num = 1
    tests = ["input/test1.png", "input/test2.png", "input/test3.png", "input/test4.jpg", "input/test5.jpg", "input/test6.jpg"]

    for test in tests:
        subprocess.run(["python", "./../run_script.py", test])
        result = f"input/test{test_num}.csv"
        exp = f"expected_outputs/test{test_num}.csv"
        
        if subprocess.run(["fc", result, exp], text = True, capture_output=True) == 0:
            passed += 1

        test_num += 1

    print("Tests passed:", str(passed) + "/6")
    

if __name__ == "__main__":
    main()