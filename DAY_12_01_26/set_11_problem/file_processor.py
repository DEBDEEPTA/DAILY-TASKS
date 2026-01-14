from abc import ABC, abstractmethod
"""
Set 11 (File Processing System)
A tool processes different file formats.
Scenario:
Base class FileProcessor with method process()

Subclasses: CSVProcessor, JSONProcessor

Requirements:
Validate file structure before processing

Extract and summarize data differently

Use method overriding to handle formats
"""
class FileProcessor(ABC):

    @abstractmethod
    def process(self,path):
        pass

    @abstractmethod
    def validate(self,path):
        pass

    @abstractmethod
    def extract(self,path):
        pass

    @abstractmethod
    def summerize(self,path):
        pass
