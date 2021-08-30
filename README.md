# Python Script to Read all csv files in a directory and write to a combined.csv file and monitor for new files and add the data form them to combined.csv

## How to install and use
1. Follow requirements.txt to install required packages using pip install -r requirements.txt
2. You can also change the location of the combined.csv file in the __init__ method of CsvWriter, as the write_file and provide a path there (don't put it in the same folder as it will try to re-write itself when it will be created)
3. Run csv_writer_script.py using python <file_name> --Directory <absolute_path_of_monitored_Directory> i.e. python csv_writer_script.py --Directory C:\\Users\\Karan\\Downloads\\Engineering_test
4. Exits the program on keyboard interrupt (Ctrl+C) or exit() command in terminal

## Usage

### Initial Run

When the program runs it will check for all existing csv files in the provided directory and write the data to the combined.csv file.

**Output**
```
Processed 5 lines of Asia Prod 1.csv file.
Processed 5 lines of Asia Prod 2.csv file.
Processed 5 lines of Asia Prod 3.csv file.
Processed 5 lines of Asia Prod 4 .csv file.
```

### File Changes in Directory

Subsequently it will initialize the Watcher and Handler class which will monitor that directory for any changes, and if file gets created in that
directory, it will trigger the append method of the CsvWriter class.

**Output**
```
Received created event - C:\\Users\\Karan\\Downloads\\Engineering_test\Asia Prod 5.csv.
Processed 5 lines of C:\\Users\\Karan\\Downloads\\Engineering_test\Asia Prod 5.csv file.
```

If the file will not be in csv format it will skip the reading and appending value to the combined.csv file.

**Output**
```
Received created event - C:\\Users\\Karan\\Downloads\\Engineering_test\requirements.txt.
Not a csv file skipping the data read:C:\\Users\\Karan\\Downloads\\Engineering_test\requirements.txt
```

### Removal of File 

It will log if any file is deleted from the monitored directory.


**Output**
```python
Received deleted event - C:\\Users\\Karan\\Downloads\\Engineering_test\requirements.txt.s
```
