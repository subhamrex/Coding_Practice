
def find_id(list, search):
    for index, item in enumerate(list):
        if item['id'] == search:
            return index
    return -1


if __name__ == '__main__':
    list = [{'name': 'Rex', 'id': 'OP001', 'power': 'All mighty'},
            {'name': 'Kali', 'id': 'HK001', 'power': 'Techy'},
            {'name': 'Adi', 'id': 'M001', 'power': 'Musician'}]
    search = 'HK001'

    find = find_id(list, search)
    if find is -1:
        print("not found")
    else:
        print(f'found {search} at index {find}')
