# EmptyFileGenerator
Create any number of empty files in the format "YYYYMMDD_NNNN.txt". (example: 20220401_0001.txt)

ちょっと必要でPythonの勉強を兼ねて作った。Git&GitHubの練習でアップした。
自分専用なのでいろいろと仕様がアレだが気にしない。

## How to use:
1. Change "init.txt"
2. Change NUMBER_OF_TIMES, which is the number of files you generate
3. Run

## Input
- "init.txt" format:

    line1: YYYYMMDD  # date
    
    line2: N         # number

- "init.txt" will be updated after run the program to prepare the next run.

## OUTPUT
- file name format:

    (YYYYMMDD)_(NNNN).txt
      
    example: 20220401_0001.txt
    
- Both date & number increase by 1 each time a file is generated.
