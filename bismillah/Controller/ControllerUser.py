from Model.Database import Database

class User(Database):
    def __init__(self):
        super().__init__()

    def add (self):
        data_kelas = []
        data = self.find_data_by({"ket" : "kosong"})
        for i in data:
            data_kelas.append(i["kode"])