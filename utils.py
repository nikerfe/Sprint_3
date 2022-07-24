import random

def generate_email(name, surname, number_stream):
    return (name + '_' + surname + '_' + number_stream + '_' + str(random.randrange(0,999)) + '@yandex.ru')