
def print_menu():
    print('-' * 30)
    print('   PyHouse - Welcome ')
    print('-' * 30)

    print('[1] Register new Item')
    print('[2] Display Catalog')
    print('[3] Display Items with no stock')
    print('[4] Update Stock manually')
    print('[5] Print stock value')
    print('[6] Remove item')
    print('[7] Show removed items')
    print('[8] List Categories')

    print('[x] Exit')

def print_header(title):
    print('\n\n') # 2 blank lines
    print('-' * 80)
    print(title)
    print('-' * 80)