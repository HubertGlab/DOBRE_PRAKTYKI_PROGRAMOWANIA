from singleton import *
from adapter import *
from factory import *


"""singleton test"""
catalog1 = LibraryCatalog()
catalog2 = LibraryCatalog()
catalog1.add_book("Book 1")
catalog2.add_book("Book 2")
print('\033[95mSingleton:\033[0;0m')
print(catalog1.get_books())

"""adapter test"""
print('\033[95mAdapter:\033[0;0m')
json_data = '''
[
    {"title": "Book 1"},
    {"title": "Book 2"},
    {"title": "Book 3"}
]
'''
print("JSON Result:", BookDataAdapter.adapt_from_json(json_data))

csv_data = """title
Book 1
Book 2
Book 3
"""
print("CSV Result:", BookDataAdapter.adapt_from_csv(csv_data))

xml_data = '''
<library>
    <book>
        <title>Book 1</title>
    </book>
    <book>
        <title>Book 2</title>
    </book>
    <book>
        <title>Book 3</title>
    </book>
</library>
'''
print("XML Result:", BookDataAdapter.adapt_from_xml(xml_data))

"""Factory test"""
print('\033[95mFactory:\033[0;0m')
student = UserFactory.create_user("Student", 'std')
teacher = UserFactory.create_user("Teacher", 'tch')
librarian = UserFactory.create_user("Librarian", 'lib')

print('student permission ', student.get_permissions())
print('teacher permission ', teacher.get_permissions())
print('librarian permission ', librarian.get_permissions())

"""Observer test"""
print('\033[95mObserver:\033[0;0m')
student = UserFactory.create_user("Student", "Alice")
catalog1 = LibraryCatalog()
catalog1.subscribe(student)
catalog1.add_book('Book 1')
catalog1.unsubscribe(student)
catalog1.add_book('Book 2')

