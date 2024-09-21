class HomeTaskFiles:
    def __init__(self, file_list) -> None:
        self.file_list = file_list
        self.file_size = {}
        self.file_lines = {}

        for self.f_name in self.file_list:
            self.f = open (self.f_name, 'r', encoding='utf-8')
            with self.f:
                self.file_lines[self.f.name] = self.f.readlines()
                self.file_size[self.f.name] = len(self.file_lines[self.f.name])
                self.f.close()
        pass

    def write_new_file_by_size(self, new_file_name):                           
        self.file_size = dict(sorted(self.file_size.items(), key=lambda item:item[1]))
         
        self.new_f = open(new_file_name, 'w')
        with self.new_f:
            self.j = 0
            for k in list(self.file_size.keys()):
                self.new_f.write(str(k) + "\n")
                self.new_f.write(str(self.file_size[k]) + "\n")
                self.new_f.writelines(self.file_lines[k])
                if self.j < len(self.file_size):
                    self.j +=1
                    self.new_f.write("\n")

    

        
f = HomeTaskFiles(["1.txt", "2.txt", "3.txt"])
f.write_new_file_by_size("result.txt")
pass
