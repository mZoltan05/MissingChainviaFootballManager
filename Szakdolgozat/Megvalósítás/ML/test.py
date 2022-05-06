import sys
def main():
    import sys
    import subprocess
    import pandas as pd
    output = subprocess.run(["python", "FindSimilarPlayer.py",'39014895'], capture_output=True)
    print (output)

if __name__ == "__main__":
    main()