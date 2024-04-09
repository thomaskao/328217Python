
class AddStu:
    def __init__(self):
        self.student_dict = dict()

    def execute(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            return 

        else:
            self.student_dict[name]=dict()
            subject = input("  Please input a subject name or exit for ending: ")
            while subject!="exit":
                while True:
                    try: 
                        score = float(input(f"Please input {name}'s {subject} self.score or < 0 for discarding the subject:"))
                        if score>=0:
                            self.student_dict[name][subject]= score
                        # student_dict[name]={subject:score}
                            print(f"   Add {name}'s scores successfully")
                        break
                    except:
                        print(f"Wrong format with reason could not convert string to float: '{score}', try again")       
            
                subject = input("  Please input a subject name or exit for ending: ")     
      

        return self.student_dict



















