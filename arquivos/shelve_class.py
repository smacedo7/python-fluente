import shelve

shelf_file = shelve.open('mydata')

shelf_file['cats'] = ['cat1', 'cat2', 'cat3']
shelf_file.close()

shelf_file = shelve.open('mydata')
shelf_file['rats'] = ['ratattouile', 'mr_bom_box']
print(shelf_file['cats'])
print(shelf_file['rats'])
shelf_file.close()

shelf_file = shelve.open('mydata')
print(shelf_file.keys()) # KeysView(<shelve.DbfilenameShelf object at 0x102e3ff10>)
print(list(shelf_file.keys()))