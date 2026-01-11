from pathlib import Path

class FileFinder:
    def __init__(self, file_name):
        self.file_name = file_name
        self.directory = Path(r'D:\Users\Dorit\Documents\לימודים\John Bryce\DataEngineering\GitPlayground\Lessons\Class\08012026\HomeWork')
        self.full_path = self.directory / self.file_name 
        
    def file_exists(self):
        # Check the FULL path (folder + filename)
        return self.full_path.is_file()

    def get_file_details(self):
        if self.file_exists():
            return {
                "name": self.full_path.name,
                "size_bytes": self.full_path.stat().st_size,
                "extension": self.full_path.suffix
            }
        return f"File '{self.file_name}' not found in the specified directory."

if __name__ == '__main__':
    f1 = FileFinder('prime.py')
    print(f1.get_file_details())
    
    f2 = FileFinder('primeeee.py')
    print(f2.get_file_details())