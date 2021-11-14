from enum import Enum
from abc import ABC, abstractmethod
import json
import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom


class Book:
    def __init__(self):
        self._book_title = ''
        self._authors = list()
        self._ISBN_number = ''
        self._publisher = ''
        self._copyright_year = ''
        self._categories = list()

    @property
    def book_title(self):
        return self._book_title

    def fillListEntry(self, key):
        anotherKey = True
        inputs = list()
        while anotherKey:
            inputs.append(input(f'Enter {key}: '))
            anotherKey = askAgain(f'Do you want to add another {key}?')
        return inputs

    def InformationCollection(self):
        self._book_title = input('Enter book title: ')
        self._authors = self.fillListEntry('author name')
        self._ISBN_number = input('Enter ISBN number: ')
        self._publisher = input('Enter publisher name: ')
        self._copyright_year = input('Enter copyright year: ')
        self._categories = self.fillListEntry('category')

    def convertToDictionary(self):
        return {
            'title': self._book_title,
            'authors': self._authors,
            'ISBN': self._ISBN_number,
            'publisher': self._publisher,
            'copyright': self._copyright_year,
            'categories': self._categories,
        }


class BookList:
    def __init__(self):
        self._book_list = list()

    @property
    def book_list(self):
        return self._book_list

    def append_book(self, book):
        self._book_list.append(book)

    def save_book_list(self, format):
        self._book_list.sort(key=lambda x: x.book_title, reverse=False)

        for book in self._book_list:
            FormatFactory.save_book_as(book, format)


class Formats(Enum):
    JSON = 1
    YAML = 2
    XML = 3


class IFormat(ABC):
    @abstractmethod
    def write_to_file():
        pass

# Function for format in JSON
class JSON(IFormat):
    def write_to_file(self, book):
        bookData = book.convertToDictionary()
        with open('Books.txt', 'a+') as f:
            f.write('-'*10 + 'JSON ' + '-'*10 + '\n')
            json.dump(bookData, f, indent=4, sort_keys=True)
            f.write('\n\n')

# Function to format in YAML
class YAML(IFormat):
    def write_to_file(self, book):
        bookData = book.convertToDictionary()
        with open('Books.txt ', 'a+') as f:
            f.write('-'*10 + 'YAML' + '-'*10 + '\n')
            yaml.dump(bookData, f)
            f.write('\n\n')

# Function to format in XML
class XML(IFormat):
    @staticmethod
    def formatXML(elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

    def write_to_file(self, book):
        bookData = book.convertToDictionary()

        root = ET.Element('root')
        title = ET.SubElement(root, 'title').text = bookData['title']

        authors = ET.SubElement(root, 'authors')
        for i in bookData['authors']:
            ET.SubElement(authors, "element").text = i

        ISBN = ET.SubElement(root, 'ISBN').text = bookData['ISBN']

        publisher = ET.SubElement(
            root, 'publisher').text = bookData['publisher']
            
        copyright = ET.SubElement(
            root, 'copyright').text = bookData['copyright']

        categories = ET.SubElement(root, 'categories')
        for i in bookData['categories']:
            ET.SubElement(categories, "element").text = i

        with open('Books.txt', 'a+') as f:
            f.write('-'*10 + 'XML ' + '-'*10 + '\n')
            f.write(XML.formatXML(root))
            f.write('\n\n')


class FormatFactory:
    @staticmethod
    def save_book_as(book, format_type):
        if format_type == 'JSON':
            return JSON().write_to_file(book)
        elif format_type == 'YAML':
            return YAML().write_to_file(book)
        elif format_type == 'XML':
            return XML().write_to_file(book)

def selectFormatType():
    format_type = ''
    format_selected = False
    while not format_selected:
        print(f'Select the format you want to save the books in:\n')
        formats = [i.name for i in Formats]
        for i in formats:
            print(i)
        format_type = input('\nSelection> ')
        if format_type.upper() not in formats:
            print('Incorrect format')
        else:
            format_selected = True
    return format_type.upper()


def askAgain(question):
    answer = input(f'{question} (y/n): ')
    while answer.lower() != 'y' and answer.lower() != 'n':
        print("Please provide either 'y' or 'n'.")
        answer = input(f'{question} (y/n): ')
    if answer.lower() == 'y':
        return True
    else:
        return False


def main():
    book_list = BookList()
    anotherBook = True
    while anotherBook:
        book = Book()
        book.InformationCollection()
        save = askAgain('Would you like to save the entered book(s)?')
        if save:
            book_list.append_book(book)

        anotherBook = askAgain('Do you want to add another book?')

    format = selectFormatType()
    book_list.save_book_list(format)

    print('Saved your books to books.txt file')


if __name__ == '__main__':
    main()
