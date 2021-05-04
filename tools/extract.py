import rarfile
my_rar = rarfile.open('Annot_7398.rar')
my_rar.extractall('./extracted') # specify which folder to extract to
my_rar.close()
