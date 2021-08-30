import time,glob,os,csv,argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CsvWriter:
    '''
    CsvWriter contains the functions that will read the .csv files in the provided folder and
    also add the data from newly created/added files in the folder
    '''
    def __init__(self, directory):
        self.DIRECTORY_TO_WATCH = directory
        self.write_file="C:\\Users\\Karan\\Downloads\\combined.csv"
        os.chdir(self.DIRECTORY_TO_WATCH)
    

    def intital_scan(self):
        '''
        Scan the given directory for any csv files and add their rows to the combined file,
        also logs the no. of lines traversed for each file
        :param self:
        '''
        with open(self.write_file,"w", newline='') as csv_file_write:
            csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Source IP','Count','Events per Second'])
        try:
            for file in glob.glob("*.csv", recursive=True):
                with open(file,"r") as csv_file, open(self.write_file,"a", newline='') as csv_file_write:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0:
                            line_count += 1
                            continue
                        else:
                            csv_writer.writerow([row[0],row[1],row[2]])
                            line_count += 1
                    print(f'Processed {line_count} lines of {file} file.')
        except:
            print("Error in file:" + file + os.system.exc_info()[0] ) 

    def append(self, file_name):
        '''
        Adds the new file's data to the combined file when called,
        also logs the no. of lines traversed for new file.
        :param self:
        :param file_name: takes the file path to be read provided by event handler
        '''
        try:
            file_extension = os.path.splitext(file_name)
            if file_extension[1] ==".csv" :
                with open(file_name,"r") as csv_file, open(self.write_file,"a", newline='') as csv_file_write:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0:
                            line_count += 1
                            continue
                        else:
                            csv_writer.writerow([row[0],row[1],row[2]])
                            line_count += 1
                    print(f'Processed {line_count} lines of {file_name} file.')
            else:
                print("Not a csv file skipping the data read:" + file_name)
        except:
            print("Error in file:" + file_name + os.system.exc_info()[0] )

class Watcher:
    '''
    Creates an Observer and initializes the Handler class, which will monitor the
    provided directory for changes and calls relevant methods.
    '''
    def __init__(self, directory):
        self.DIRECTORY_TO_WATCH = directory
        self.observer = Observer()

    def run(self):
        '''
        Initializes Handler class, and Observer methods and keeps it alive until any error
        or keyboard interrupt is provided.
        '''
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    '''
    Contains event change handlers which notify and call the appropriate methods,
    when a new file is added to the monitored directory.
    '''
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            CsvWriter_Object_1 = CsvWriter(os.path.dirname(event.src_path))
            CsvWriter_Object_1.append(event.src_path)
        elif event.event_type == 'deleted':
            # Taken any action here when a file is modified.
            print("Received deleted event - %s." % event.src_path)

if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser(
        description="Csv Writer Script"
    )
    arg_parse.add_argument(
        "--Directory",
        action="store",
        required=True,
        help="Provide the full path of directory to be monitored, for e.g. 'C:\\Users\\Karan\\Downloads\\Engineering_test'",
        dest="directory"
    )
    args = arg_parse.parse_args()
    #Initially Run the Initial Scan of the provided directory to read all csv files and write their data
    CsvWriter_Object = CsvWriter(args.directory)
    CsvWriter_Object.intital_scan()
    #Initiate the Watcher method to Monitor changes in that directory and add new data to file if any .csv file 
    # added to directory
    Watcher_Object = Watcher(args.directory)
    Watcher_Object.run()