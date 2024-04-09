class PrintAll:
    def __init__(self):
        pass
    def execute(self, student_dict):
        try:
            print("\n==== student list ====\n")
            for i, j in student_dict.items():
                print('Name:{}'.format(i))
                for k, l in j.items():
                    print('   subject: {},score:{}'.format(k, l))
                print()
            print ("======================")

        except Exception as e:
            print(e)
          