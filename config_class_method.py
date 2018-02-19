import json
from os.path import splitext, exists

class Config(object):
    def __init__(self, source=None, params=None):
        self._source = source
        self._params = params
        storage_init(self)


    def set_params(self, params):
        self._params = params
        storage_init(self)


    def set_source(self, source):
        self._source = source
        storage_init(self)


    def storage_init(self):
        if self._params and self._source not self.storage:
            self._storage = ConfigStorage(self._source, self._params)


    def get_params(self):
        return self._storage.restore_data()


    def save_params(self):
        self._storage.save_data()


    def restore_params(self):
        self._params = self._storage.restore_data()



class ConfigStorage(object):
    def __init__(self, path, data):
        self.path = source_path
        self.data = data
        self.savers = { '.txt': lambda data, f: f.write(self.data),
                        '.json': lambda data, f: json.dump(data, f, indetn=4)
        }
        self.loaders = { '.txt': lambda f: f.read(),
                        '.json': lambda f: json.load(f)
        }


    def get_saver(path):
        filename, ext = splitext(path)
        return ext


    def save_data(self):
        if not exists(self.path):
            raise ValueError("File doesn't exist")
        saver = get_saver(os.path.splitext(path)[1])
        with open(self.path, 'w') as f:
            saver(self.data, f)


    def restore_data(self):
        loader = get_loader(os.path.splitext(path)[1])
        with open(self.path) as f:
            result = loader(self.data, f)
        return result

