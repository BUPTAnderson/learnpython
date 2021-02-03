class NewStyle:

    def __init__(self, name, description):
        self.name = name
        self.description = description


if __name__ == '__main__':
    new = NewStyle("new", "New style class")
    print(new)
    print(type(new))
    print(dir(new))
