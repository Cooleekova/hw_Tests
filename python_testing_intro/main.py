from pprint import pprint

# Я работаю секретарем и мне постоянно приходят различные документы.
# Я должен быть очень внимателен чтобы не потерять ни один документ.
# Каталог документов хранится в следующем виде:

# documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
#       ]

# Перечень полок, на которых находятся документы хранится в следующем виде:

# directories = {
#         '1': ['2207 876234', '11-2'],
#         '2': ['10006'],
#         '3': []
#       }


# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды,
# а не названия функций. Функции должны иметь выразительное название, передающие её действие.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def check_document_existence(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def command_l(docs):
    info = list()
    for doc in docs:
        doc_info = f'{doc.get("type")} "{doc.get("number")}" "{doc.get("name")}"'
        info.append(doc_info)
    return info


pprint(command_l(documents))


def command_a_docs(docs, shelf, shelf_num, doc_type, doc_number, doc_name):
    new_doc = dict(type=doc_type, number=doc_number, name=doc_name)
    docs.append(new_doc)
    if shelf_num not in shelf.keys():
        return "Полки с таким номером нет!"
    else:
        for k, v in shelf.items():
            if k == shelf_num:
                v.append(doc_number)
    return docs, shelf


pprint(command_a_docs(documents, directories, '3', 'passport', '1234', 'Tatiana'))

# def command_p(docs):
#     num = input('введите номер документа ')
#     for doc in docs:
#       if num == doc["number"]:
#         return doc["name"]
#         elif num != doc["number"]:
#      return "\nДокумента с таким номером нет"


