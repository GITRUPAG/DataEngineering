from abc import ABC, abstractmethod
class pipeline(ABC):
    @abstractmethod
    def extract(self):
        pass
    def display(self):
        print("Display")

class CSV(pipeline):
    def extract(self):
        print("CSV file Extraction")
class API(pipeline):
    def extract(self):
        print("API data Extraction")


