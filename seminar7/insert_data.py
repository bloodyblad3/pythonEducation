def insert_data(data, sep=None):
    with open("note.txt", 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write("\n")
        else:
            file.write(sep.join(data))
            file.write("\n")