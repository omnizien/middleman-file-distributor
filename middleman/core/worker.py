list_files = [{}]


class worker:

    @staticmethod
    def process_list(self, collection, title, mediatype, file):
        list_files.append([{'collection': collection, 'title': title, 'mediatype': mediatype, 'file': file}])
        # print(_collection[0][0]['collection'])
        print(list_files)

    @staticmethod
    def clear_list(self):
        list_files.clear()

    @staticmethod
    def pop_list_0th(self):
        print('pop')
        list_files.pop(0)

    @staticmethod
    def push_list_0th(self):
        return list_files[0][0]

    @staticmethod
    def get_list(self):
        return list_files
