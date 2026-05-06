import pandas as pd, random as rd, tkinter as tk, os, sys

class RandGen:
    def __init__(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.user_list = []
        self.select_list = []
        self.select_amount = 0
        
    def loadScreen(self):
        self.root = tk.Tk()
        self.root.title("Random Generator")
        self.root.geometry("600x400")

        # frame
        l_frame = tk.Frame(self.root).pack(side="left", fill="both", expand=True, padx=10, pady=10)
        r_frame = tk.Frame(self.root).pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # left
        tk.Label(l_frame, text="목록").pack()
        scrollbar = tk.Scrollbar(l_frame)
        scrollbar.pack(side="right", fill="y")

        user_listbox = tk.Listbox(l_frame, yscrollcommand=scrollbar.set)
        user_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=user_listbox.yview)
        
        for row in self.user_list: user_listbox.insert("end", row)

        # right
        top_right = tk.LabelFrame(r_frame, text=f"당첨자 {self.select_amount}인", pady=5)
        top_right.pack(side="top", fill="both", expand=True, pady=(0, 10))
        self.select_listbox = tk.Listbox(top_right, yscrollcommand=scrollbar.set)
        self.select_listbox.pack(side="left", fill="both", expand=True)
        self.select_listbox.insert("end", "비어 있습니다.")

        bottom_right = tk.LabelFrame(r_frame, text="제어판", pady=5)
        bottom_right.pack(side="bottom", fill="both", expand=True, pady=(0, 10))

        # 오른쪽 아래 영역에 버튼 추가 예시
        btn_frame = tk.Frame(bottom_right) # 버튼들을 가로로 배치하기 위한 프레임
        btn_frame.pack(pady=5)

        btn_run = tk.Button(btn_frame, text="실행", width=10, command=self.random)
        btn_run.pack(side="left", padx=5)
    
    def loadData(self):
        path = "user_list.csv"
        if os.path.exists(path):
            header = pd.read_csv(path, nrows=0).columns.tolist()
            print(" | ".join(header))
            while True:
                data = str(input("사용자명이 들어있는 칼럼명을 입력하세요: "))
                if data in header: break
                else: continue
            self.user_list = pd.read_csv(path, usecols=[data]).iloc[:, 0].tolist()
        else:
            return False

    def insertData(self):
        while True:
            data = str(input("사용자명을 입력하세요. (미 입력시 입력 종료): "))
            if not data: 
                while True:
                    i = input("추첨할 인원을 입력하세요: ")
                    if i.isdigit():
                        self.select_amount = int(i)
                        break
                break
            self.user_list.append(data)
        return self.user_list
    
    def random(self):
        self.select_list = []            
        self.select_list = rd.sample(self.user_list, self.select_amount)
        self.select_listbox.delete(0, "end")
        for row in self.select_list:
            self.select_listbox.insert("end", row)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RandGen()

    if not app.loadData():
        if not app.insertData():
            print("실행 취소.")
            sys.exit()
        else:
            app.loadScreen()
    else:
        app.loadScreen()
    
    app.run()