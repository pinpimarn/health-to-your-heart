import tkinter as tk
from tkinter import ttk
import tkmacosx as tmc
from PIL import ImageTk, Image
from data_analysis import *
from playsound import playsound
import webbrowser
from progressbar import ProgressBar
from app_controller import *


class MyApp(tk.Tk):

    def __init__(self, data_ana: DataAnalytic):
        super().__init__()
        self.data_ana = data_ana
        self.lan = tk.StringVar()
        self.title('Health To Your Heart')
        self.cb1 = tk.StringVar('')
        self.cb2 = tk.StringVar('')
        self.height = tk.StringVar()
        self.weight = tk.StringVar()
        self.bmi = tk.StringVar()
        self.smoking = tk.StringVar()
        self.alc = tk.StringVar()
        self.stroke = tk.StringVar()
        self.diff = tk.StringVar()
        self.sex = tk.StringVar()
        self.age = tk.StringVar()
        self.dia = tk.StringVar()
        self.phy = tk.StringVar()
        self.gen = tk.StringVar()
        self.sleep = tk.StringVar('')
        self.asth = tk.StringVar()
        self.kidney = tk.StringVar()
        self.skin = tk.StringVar()
        self.init_components()

    def init_components(self):
        playsound('click sound.wav')
        self.configure(bg='#A72727')
        self.bgimg = ImageTk.PhotoImage(file="pic/bg.png")
        self.bg = tk.Label(self, image=self.bgimg)
        self.bg.place(x=0, y=0)
        self.geometry('1080x608')
        self.resizable(0, 0)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground='#F1716B', background='#FBEBCB')
        self.option_add("*TCombobox*Listbox*Background", '#FBEBCB')
        self.option_add("*TCombobox*Listbox*Font", ('Comic Sans MS', 15))
        style.configure("TRadiobutton", fieldbackground='#F1716B', background='#F5BFBA', font=('Comic Sans MS', 20))
        self.menu_button()
        self.th = ImageTk.PhotoImage(Image.open("pic/th.png"))
        self.eng = ImageTk.PhotoImage(Image.open("pic/eng.png"))
        tk.Button(self, image=self.th,
                  command=self.lan_th,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=400, y=450)
        tk.Button(self, image=self.eng,
                  command=self.lan_eng,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=580, y=450)

    def loadingb(self):
        pb = ProgressBar()
        pb.run()

    def lan_th(self):
        self.exit()
        ui = MyAppTH(self.data_ana)
        ui.run()

    def lan_eng(self):
        self.exit()
        ui = MyAppENG(self.data_ana)
        ui.run()

    def reset_boxes(self):
        self.cb1.set('')
        self.cb2.set('')
        self.height.set('')
        self.weight.set('')
        self.smoking.set(None)
        self.alc.set(None)
        self.stroke.set(None)
        self.diff.set(None)
        self.sex.set('')
        self.age.set('')
        self.dia.set(None)
        self.phy.set(None)
        self.gen.set('')
        self.sleep.set('')
        self.asth.set(None)
        self.kidney.set(None)
        self.skin.set(None)

    def menu_button(self):
        self.img1 = ImageTk.PhotoImage(Image.open("pic/3.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("pic/5.png"))
        tk.Button(self, image=self.img1,
                  command=self.toggle_win,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=5, y=10)

    def kno_menu_button(self):
        pass

    def lr_button(self):
        self.left = ImageTk.PhotoImage(Image.open("pic/left.png"))
        self.right = ImageTk.PhotoImage(Image.open("pic/right.png"))
        tk.Button(self, image=self.left,
                  command=self.remedy_page1,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=750, y=520)
        tk.Button(self, image=self.right,
                  command=self.remedy_page2,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=850, y=520)

    def back_button(self):
        pass

    def toggle_win(self):
        pass

    def exit(self):
        playsound('click sound.wav')
        self.destroy()

    def dele(self):
        playsound('click sound.wav')
        self.f1.destroy()

    def run(self):
        self.mainloop()

    def analytic_page(self):
        pass

    def analytic_components(self):
        pass

    def basic_graph_analytic(self):
        pass

    def sup_graph_analytic(self):
        pass

    def load_column(self, data_ana: DataAnalytic):
        playsound('click sound.wav')
        cols = data_ana.get_columns()
        self.col_name_var['values'] = [name for name in cols]
        chart_types = ['pie', 'bar', 'barh']
        self.chart_type_var['values'] = [name for name in chart_types]

    def self_check_handler(self):
        pass

    def back_to_check(self):
        pass

    def check_all_fill(self):
        pass

    def result_page(self):
        pass

    def bmi_cal(self):
        pass

    def knowledge_handler(self):
        pass

    def info_page(self):
        pass

    def sym_page(self):
        pass

    def cau_page(self):
        pass

    def risk_page(self):
        pass

    def prevention_page(self):
        pass

    def remedy_page1(self):
        pass

    def remedy_page2(self):
        pass

    def check_num(self):
        pass


class MyAppENG(MyApp):

    def kno_menu_button(self):
        self.bttn_info = ImageTk.PhotoImage(Image.open("pic/bttn-info.png"))
        self.bttn_sym = ImageTk.PhotoImage(Image.open("pic/bttn-sym.png"))
        self.bttn_cau = ImageTk.PhotoImage(Image.open("pic/bttn-causes.png"))
        self.bttn_ris = ImageTk.PhotoImage(Image.open("pic/bttn-risks.png"))
        tk.Button(self, image=self.bttn_info,
                  command=self.info_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=280, y=520)
        tk.Button(self, image=self.bttn_sym,
                  command=self.sym_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=420, y=520)
        tk.Button(self, image=self.bttn_cau,
                  command=self.cau_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=560, y=520)
        tk.Button(self, image=self.bttn_ris,
                  command=self.risk_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=700, y=520)

    def back_button(self):
        self.back = ImageTk.PhotoImage(Image.open("pic/back.png"))
        tk.Button(self, image=self.back,
                  command=self.knowledge_handler,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=950, y=50)

    def toggle_win(self):
        self.f1 = tk.Frame(self, width=400, height=608, bg='#FBEBCB', highlightbackground="#F1716B",
                           highlightthickness=2)
        self.f1.place(x=0, y=0)

        def bttn(x, y, text, bcolor, fcolor, cmd):
            def on_enter(e):
                togButton['background'] = bcolor
                togButton['foreground'] = '#F1716B'

            def on_leave(e):
                togButton['background'] = fcolor
                togButton['foreground'] = '#F1716B'

            togButton = tmc.Button(self.f1, text=text,
                                   width=395,
                                   height=38,
                                   fg='#F1716B',
                                   font=('Arial', 15),
                                   border=0,
                                   bg=fcolor,
                                   activeforeground='#F1716B',
                                   activebackground='#F1716B',
                                   command=cmd)

            togButton.bind("<Enter>", on_enter)
            togButton.bind("<Leave>", on_leave)
            togButton.place(x=x, y=y)

        bttn(0, 80, 'M A I N   M E N U', '#DCA6A0', '#ECD6D4', self.init_components)
        bttn(0, 117, 'A N A L Y T I C S', '#DCA6A0', '#ECD6D4', self.analytic_page)
        bttn(0, 154, 'S E L F - C H E C K', '#DCA6A0', '#ECD6D4', self.self_check_handler)
        bttn(0, 191, 'K N O W L E D G E    C E N T E R', '#DCA6A0', '#ECD6D4', self.knowledge_handler)
        bttn(0, 228, 'H O T L I N E S', '#DCA6A0', '#ECD6D4', self.hotline_handler)
        bttn(0, 265, 'E X I T', '#DCA6A0', '#ECD6D4', self.exit)

        tk.Button(self.f1, image=self.img2, border=0, command=self.dele, bg='#12c4c0',
                  activebackground='#12c4c0').place(x=5, y=10)

    def analytic_page(self):
        self.dele()
        self.bgimg2 = ImageTk.PhotoImage(file="pic/background2.png")
        self.bg2 = tk.Label(self, image=self.bgimg2)
        self.bg2.place(x=0, y=0)
        self.menu_button()
        self.ana_menu1 = ImageTk.PhotoImage(Image.open("pic/basic.png"))
        self.ana_menu2 = ImageTk.PhotoImage(Image.open("pic/superior.png"))

        # TableShower.init_components(self, self)
        tk.Button(self, image=self.ana_menu1,
                  command=self.basic_graph_analytic,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=280, y=200)
        tk.Button(self, image=self.ana_menu2,
                  command=self.sup_graph_analytic,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=600, y=200)

    def analytic_components(self):
        self.dele()
        self.bgimg2 = ImageTk.PhotoImage(file="pic/background2.png")
        self.bg2 = tk.Label(self, image=self.bgimg2)
        self.bg2.place(x=0, y=0)
        self.menu_button()
        playsound('click sound.wav')
        self.col_name_var = ttk.Combobox(self, textvariable=self.cb1, width=15, font=('Comic Sans MS', 30))
        self.col_name_var['state'] = 'readonly'
        self.chart_type_var = ttk.Combobox(self, textvariable=self.cb2, width=15, font=('Comic Sans MS', 30))
        self.chart_type_var['state'] = 'readonly'
        self.load_column(self.data_ana)
        label2 = tk.Label(text="Data", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        label2.place(x=230, y=200)
        label3 = tk.Label(text="Chart Type", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        label3.place(x=550, y=200)
        self.col_name_var.place(x=100, y=250)
        self.chart_type_var.place(x=450, y=250)
        self.back = ImageTk.PhotoImage(Image.open("pic/back.png"))
        tk.Button(self, image=self.back,
                  command=self.analytic_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=950, y=50)

    def basic_graph_analytic(self):
        self.analytic_components()
        plot = ChartPlot()
        label = tk.Label(text="Note: Based on information from all survey respondents.", bg='#F5BFBA', fg='#C74744',
                         font=('Comic Sans MS', 20))
        label.place(x=100, y=150)
        self.button1 = tk.Button(self, text="Plot!", width=7, font=('Comic Sans MS', 25),
                                 command=lambda: plot.basic_plot(self.data_ana.data,
                                                                 str(self.cb1.get()), str(self.cb2.get())))
        self.button1.place(x=800, y=250)
        self.cb1.set('')
        self.cb2.set('')

    def sup_graph_analytic(self):
        self.analytic_components()
        plot = ChartPlot()
        label = tk.Label(text="Note: Based on information from all survey respondents 'with heart disease'.",
                         bg='#F5BFBA', fg='#C74744',
                         font=('Comic Sans MS', 20))
        label.place(x=100, y=150)
        self.button1 = tk.Button(self, text="Plot!", width=7, font=('Comic Sans MS', 25),
                                 command=lambda: plot.double_plot(self.data_ana.data,
                                                                  str(self.cb1.get()), str(self.cb2.get())))
        self.button1.place(x=800, y=250)
        self.cb1.set('')
        self.cb2.set('')

    def self_check_handler(self):
        self.dele()
        self.bgimg3 = ImageTk.PhotoImage(file="pic/bg-selfcheck.png")
        self.bg3 = tk.Label(self, image=self.bgimg3)
        self.bg3.place(x=0, y=0)

        # Sex label
        sex_label = tk.Label(text="Sex: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        sex_label.place(x=580, y=185)
        self.sex_var = ttk.Combobox(self, textvariable=self.sex, width=7, font=('Comic Sans MS', 20))
        self.sex_var['values'] = ('Male', 'Female')
        self.sex_var['state'] = 'readonly'
        self.sex_var.place(x=680, y=185)

        # BMI label
        height_label = tk.Label(text="Height(cm.): ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        height_label.place(x=130, y=130)
        self.height_entry = tk.Entry(self, width=20, bg='#FBECCB', textvariable=self.height, font=('Comic Sans MS', 20))
        self.height_entry.place(x=260, y=130)
        weight_label = tk.Label(text="Weight(kg.): ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        weight_label.place(x=130, y=185)
        self.weight_entry = tk.Entry(self, width=20, bg='#FBECCB', textvariable=self.weight, font=('Comic Sans MS', 20))
        self.weight_entry.place(x=260, y=185)

        # Age label
        age_label = tk.Label(text="Age: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        age_label.place(x=580, y=130)
        self.age_var = ttk.Combobox(self, textvariable=self.age, width=7, font=('Comic Sans MS', 20))
        self.age_var['values'] = ('18-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                                  '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older')
        self.age_var['state'] = 'readonly'
        self.age_var.place(x=680, y=130)

        # Sleep time label
        sleep_label = tk.Label(text="Average sleep hours per one day: ", bg='#F5BFBA', fg='#C74744',
                               font=('Comic Sans MS', 20))
        sleep_label.place(x=130, y=240)
        self.sleep_var = ttk.Combobox(self, textvariable=self.sleep, width=5, font=('Comic Sans MS', 20))
        self.sleep_var['values'] = [n for n in range(24)]
        self.sleep_var['state'] = 'readonly'
        self.sleep_var.place(x=455, y=240)

        # Stroke label
        stroke_label = tk.Label(text="Do you have a stroke?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        stroke_label.place(x=130, y=350)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.stroke, style='TRadiobutton')
        rb1.place(x=350, y=350)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.stroke, style='TRadiobutton')
        rb2.place(x=420, y=350)

        # Diffwalking label
        diff_label = tk.Label(text="Feel difficulty walking?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        diff_label.place(x=580, y=405)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.diff, style='TRadiobutton')
        rb1.place(x=800, y=405)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.diff, style='TRadiobutton')
        rb2.place(x=870, y=405)

        # Alcohol label
        alc_label = tk.Label(text="Are you a heavy drinker?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        alc_label.place(x=130, y=405)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.alc, style='TRadiobutton')
        rb1.place(x=380, y=405)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.alc, style='TRadiobutton')
        rb2.place(x=450, y=405)

        # Physical Activity
        phy_label = tk.Label(text="Do you exercise regularly?: ", bg='#F5BFBA', fg='#C74744',
                             font=('Comic Sans MS', 20))
        phy_label.place(x=130, y=460)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.phy, style='TRadiobutton')
        rb1.place(x=390, y=460)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.phy, style='TRadiobutton')
        rb2.place(x=460, y=460)

        # Diabetic label
        dia_label = tk.Label(text="Diabetic?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        dia_label.place(x=580, y=295)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.dia, style='TRadiobutton')
        rb1.place(x=700, y=295)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.dia, style='TRadiobutton')
        rb2.place(x=770, y=295)
        rb2 = ttk.Radiobutton(self, text='No(borderline diabetes)', value='No, borderline diabetes', variable=self.dia,
                              style='TRadiobutton')
        rb2.place(x=830, y=295)

        # Asthma label
        asth_label = tk.Label(text="Asthma?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        asth_label.place(x=580, y=350)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.asth, style='TRadiobutton')
        rb1.place(x=700, y=350)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.asth, style='TRadiobutton')
        rb2.place(x=770, y=350)

        # Kidney label
        kidney_label = tk.Label(text="Have kidney disease?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        kidney_label.place(x=580, y=460)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.kidney, style='TRadiobutton')
        rb1.place(x=800, y=460)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.kidney, style='TRadiobutton')
        rb2.place(x=870, y=460)

        # Skin label
        skin_label = tk.Label(text="Skin cancer?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        skin_label.place(x=130, y=295)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.skin, style='TRadiobutton')
        rb1.place(x=350, y=295)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.skin, style='TRadiobutton')
        rb2.place(x=420, y=295)

        # General Health label
        gen_label = tk.Label(text="How was your health?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        gen_label.place(x=580, y=240)
        self.gen_var = ttk.Combobox(self, textvariable=self.gen, width=10, font=('Comic Sans MS', 20))
        self.gen_var['values'] = ('Poor', 'Fair', 'Good', 'Very good', 'Excellent')
        self.gen_var['state'] = 'readonly'
        self.gen_var.place(x=800, y=240)

        # Smoke label
        gen_label = tk.Label(text="You smoked > 100 cigarettes in your entire life?", bg='#F5BFBA', fg='#C74744',
                             font=('Comic Sans MS', 20))
        gen_label.place(x=130, y=515)
        rb1 = ttk.Radiobutton(self, text='Yes', value='Yes', variable=self.smoking, style='TRadiobutton')
        rb1.place(x=600, y=515)
        rb2 = ttk.Radiobutton(self, text='No', value='No', variable=self.smoking, style='TRadiobutton')
        rb2.place(x=670, y=515)
        self.menu_button()
        self.check_all_fill()

    def back_to_check(self):
        self.back = ImageTk.PhotoImage(Image.open("pic/back.png"))
        tk.Button(self, image=self.back,
                  command=self.self_check_handler,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=950, y=50)
        self.reset_boxes()

    def check_all_fill(self):
        prototype = [self.height.get(), self.weight.get(), self.smoking.get(), self.alc.get(), self.stroke.get(),
                     self.diff.get(), self.sex.get(), self.age.get(), self.dia.get(), self.phy.get(),
                     self.gen.get(), self.sleep.get(), self.asth.get(), self.kidney.get(), self.skin.get()]
        ccount = 1
        for i in prototype:
            self.check_num()
            if len(i.strip()) == 0:
                fill_label = tk.Label(text="Please fill in all blocks", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 30))
                fill_label.place(x=400, y=550)
                if ccount > 1:
                    playsound('warning.wav')
                fill_label.after(2000, fill_label.destroy)
                self.button1 = tk.Button(self, text="Check!", width=7, font=('Comic Sans MS', 25),
                                         command=self.check_all_fill)
                self.button1.place(x=850, y=550)
                break
            elif ccount == 15:
                playsound('click sound.wav')
                fill_label = tk.Label(text="Are you ready to see the result?", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 30))
                fill_label.place(x=350, y=550)
                self.button1 = tk.Button(self, text="Yes!", width=7, font=('Comic Sans MS', 25),
                                         command=self.bmi_cal)
                self.button1.place(x=850, y=550)
            else:
                ccount += 1

    def result_page(self):
        self.loadingb()
        if self.result == 'Yes':
            self.yesimg = ImageTk.PhotoImage(file="pic/yes.png")
            self.yes = tk.Label(self, image=self.yesimg)
            self.yes.place(x=0, y=0)
        else:
            self.noimg = ImageTk.PhotoImage(file="pic/no.png")
            self.no = tk.Label(self, image=self.noimg)
            self.no.place(x=0, y=0)
        self.menu_button()
        self.back_to_check()

    def hotline_handler(self):
        self.dele()
        self.f2 = tk.Frame(self, width=1080, height=608, bg='#F5BFBA')
        self.f2.place(x=0, y=0)
        webbrowser.open('https://www.apollo247.com/specialties')
        self.init_components()

    def knowledge_handler(self):
        self.dele()
        self.bgimg4 = ImageTk.PhotoImage(file="pic/bg-knowledge.png")
        self.bg4 = tk.Label(self, image=self.bgimg4)
        self.bg4.place(x=0, y=0)
        self.menu_button()
        self.kno_menu1 = ImageTk.PhotoImage(Image.open("pic/what.png"))
        self.kno_menu2 = ImageTk.PhotoImage(Image.open("pic/protect.png"))
        self.kno_menu3 = ImageTk.PhotoImage(Image.open("pic/remedy.png"))

        tk.Button(self, image=self.kno_menu1,
                  command=self.info_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=150, y=230)
        tk.Button(self, image=self.kno_menu2,
                  command=self.prevention_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=450, y=230)
        tk.Button(self, image=self.kno_menu3,
                  command=self.remedy_page1,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=750, y=230)

    def bmi_cal(self):
        playsound('click sound2.wav')
        self.dele()
        if self.height.get().isnumeric() and self.weight.get().isnumeric():
            height = float(self.height.get())
            weight = float(self.weight.get())
            height /= 100
            self.bmi = weight / height * height
        else:
            fill_label = tk.Label(text="Please fill with numbers", bg='#F5BFBA',
                                  fg='#C74744', font=('Comic Sans MS', 20))
            fill_label.place(x=750, y=50)
            fill_label.after(3000, fill_label.destroy)
            raise ValueError("The input must be numbers")

        self.user_data_lst = ['Null', self.bmi, self.smoking.get(), self.alc.get(), self.stroke.get(), 'Null',
                              'Null', self.diff.get(), self.sex.get(), self.age.get(), 'Null', self.dia.get(),
                              self.phy.get(),
                              self.gen.get(), float(self.sleep.get()), self.asth.get(), self.kidney.get(),
                              self.skin.get()]
        cl = AppController()
        self.result = cl.ml(self.user_data_lst)
        self.menu_button()
        self.result_page()

    def info_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.info = ImageTk.PhotoImage(file="pic/info.png")
        self.info_bg = tk.Label(self, image=self.info)
        self.info_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def sym_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.sym = ImageTk.PhotoImage(file="pic/symptoms.png")
        self.sym_bg = tk.Label(self, image=self.sym)
        self.sym_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def cau_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.cau = ImageTk.PhotoImage(file="pic/causes.png")
        self.cau_bg = tk.Label(self, image=self.cau)
        self.cau_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def risk_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.ris = ImageTk.PhotoImage(file="pic/risks.png")
        self.ris_bg = tk.Label(self, image=self.ris)
        self.ris_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def prevention_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.pre = ImageTk.PhotoImage(file="pic/prevention_bg.png")
        self.pre_bg = tk.Label(self, image=self.pre)
        self.pre_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()

    def remedy_page1(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.medi = ImageTk.PhotoImage(file="pic/medi.png")
        self.medi_bg = tk.Label(self, image=self.medi)
        self.medi_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.lr_button()

    def remedy_page2(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.sur = ImageTk.PhotoImage(file="pic/surge.png")
        self.sur_bg = tk.Label(self, image=self.sur)
        self.sur_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.lr_button()

    def check_num(self):
        if self.height.get() != "":
            if not self.height.get().isnumeric():
                playsound('warning.wav')
                fill_label = tk.Label(text="Please fill with numbers", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=750, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("The input must be numbers")
            elif float(self.height.get()) < 0 or float(self.height.get()) > 300:
                playsound('warning.wav')
                fill_label = tk.Label(text="Please fill appropriate numbers", bg='#F5BFBA',
                                          fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=750, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("The input must be appropriate numbers")
        if self.weight.get() != "":
            if not self.weight.get().isnumeric():
                playsound('warning.wav')
                fill_label = tk.Label(text="Please fill with numbers", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=750, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("The input must be numbers")
            elif float(self.weight.get()) < 0:
                playsound('warning.wav')
                fill_label = tk.Label(text="Please fill appropriate numbers", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=750, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("The input must be appropriate numbers")


class MyAppTH(MyApp):

    def kno_menu_button(self):
        self.bttn_info = ImageTk.PhotoImage(Image.open("picTH/bttn-info.png"))
        self.bttn_sym = ImageTk.PhotoImage(Image.open("picTH/bttn-sym.png"))
        self.bttn_cau = ImageTk.PhotoImage(Image.open("picTH/bttn-causes.png"))
        self.bttn_ris = ImageTk.PhotoImage(Image.open("picTH/bttn-risks.png"))
        tk.Button(self, image=self.bttn_info,
                  command=self.info_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=280, y=520)
        tk.Button(self, image=self.bttn_sym,
                  command=self.sym_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=420, y=520)
        tk.Button(self, image=self.bttn_cau,
                  command=self.cau_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=560, y=520)
        tk.Button(self, image=self.bttn_ris,
                  command=self.risk_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=700, y=520)

    def back_button(self):
        self.back = ImageTk.PhotoImage(Image.open("picTH/back.png"))
        tk.Button(self, image=self.back,
                  command=self.knowledge_handler,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=950, y=50)

    def toggle_win(self):
        self.f1 = tk.Frame(self, width=400, height=608, bg='#FBEBCB', highlightbackground="#F1716B",
                           highlightthickness=2)
        self.f1.place(x=0, y=0)

        # buttons
        def bttn(x, y, text, bcolor, fcolor, cmd):
            def on_entera(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = '#F1716B'

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground'] = '#F1716B'

            myButton1 = tmc.Button(self.f1, text=text,
                                   width=395,
                                   height=38,
                                   fg='#F1716B',
                                   font=('Arial', 15),
                                   border=0,
                                   bg=fcolor,
                                   activeforeground='#F1716B',
                                   activebackground='#F1716B',
                                   command=cmd)

            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x, y=y)

        bttn(0, 80, 'เ ม นู ห ลั ก', '#DCA6A0', '#ECD6D4', self.init_components)
        bttn(0, 117, 'วิ เ ค ร า ะ ห์ ข้ อ มู ล', '#DCA6A0', '#ECD6D4', self.analytic_page)
        bttn(0, 154, 'เ ช็ ค หั ว ใ จ ข อ ง คุ ณ', '#DCA6A0', '#ECD6D4', self.self_check_handler)
        bttn(0, 191, 'ศู น ย์ ค ว า ม รู้', '#DCA6A0', '#ECD6D4', self.knowledge_handler)
        bttn(0, 228, 'ป รึ ก ษ า', '#DCA6A0', '#ECD6D4', self.hotline_handler)
        bttn(0, 265, 'อ อ ก', '#DCA6A0', '#ECD6D4', self.exit)

        tk.Button(self.f1, image=self.img2, border=0, command=self.dele, bg='#12c4c0',
                  activebackground='#12c4c0').place(x=5, y=10)

    def analytic_page(self):
        self.dele()
        self.bgimg2 = ImageTk.PhotoImage(file="picTH/background2.png")
        self.bg2 = tk.Label(self, image=self.bgimg2)
        self.bg2.place(x=0, y=0)
        self.menu_button()
        self.ana_menu1 = ImageTk.PhotoImage(Image.open("picTH/basic.png"))
        self.ana_menu2 = ImageTk.PhotoImage(Image.open("picTH/superior.png"))

        # TableShower.init_components(self, self)
        tk.Button(self, image=self.ana_menu1,
                  command=self.basic_graph_analytic,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=280, y=200)
        tk.Button(self, image=self.ana_menu2,
                  command=self.sup_graph_analytic,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=600, y=200)

    def analytic_components(self):
        self.dele()
        self.bgimg2 = ImageTk.PhotoImage(file="pic/background2.png")
        self.bg2 = tk.Label(self, image=self.bgimg2)
        self.bg2.place(x=0, y=0)
        self.menu_button()
        playsound('click sound.wav')
        self.col_name_var = ttk.Combobox(self, textvariable=self.cb1, width=15, font=('Comic Sans MS', 30))
        self.col_name_var['state'] = 'readonly'
        self.chart_type_var = ttk.Combobox(self, textvariable=self.cb2, width=15, font=('Comic Sans MS', 30))
        self.chart_type_var['state'] = 'readonly'
        self.load_column(self.data_ana)
        label2 = tk.Label(text="ข้อมูล", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        label2.place(x=230, y=200)
        label3 = tk.Label(text="ประเภทแผนภูมิ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        label3.place(x=550, y=200)
        self.col_name_var.place(x=100, y=250)
        self.chart_type_var.place(x=450, y=250)
        self.back = ImageTk.PhotoImage(Image.open("picTH/back.png"))
        tk.Button(self, image=self.back,
                  command=self.analytic_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=950, y=50)

    def basic_graph_analytic(self):
        self.analytic_components()
        plot = ChartPlot()
        label = tk.Label(text="หมายเหตุ: ข้อมูลนี้มีการวิเคราะห์มาจากผู้กรอกแบบสอบถามทั้งหมด", bg='#F5BFBA',
                         fg='#C74744',
                         font=('Comic Sans MS', 20))
        label.place(x=100, y=150)
        self.button1 = tk.Button(self, text="ดูกราฟ!", width=7, font=('Comic Sans MS', 25),
                                 command=lambda: plot.basic_plot(self.data_ana.data,
                                                                 str(self.cb1.get()), str(self.cb2.get())))
        self.button1.place(x=800, y=250)
        self.cb1.set('')
        self.cb2.set('')

    def sup_graph_analytic(self):
        self.analytic_components()
        plot = ChartPlot()
        label = tk.Label(text="หมายเหตุ: ข้อมูลนี้มีการวิเคราะห์มาจากผู้กรอกแบบสอบถามที่เป็นโรคหัวใจ",
                         bg='#F5BFBA', fg='#C74744',
                         font=('Comic Sans MS', 20))
        label.place(x=100, y=150)
        self.button1 = tk.Button(self, text="ดูกราฟ!", width=7, font=('Comic Sans MS', 25),
                                 command=lambda: plot.double_plot(self.data_ana.data,
                                                                  str(self.cb1.get()),
                                                                  str(self.cb2.get())))
        self.button1.place(x=800, y=250)
        self.cb1.set('')
        self.cb2.set('')

    def self_check_handler(self):
        self.dele()
        self.bgimg3 = ImageTk.PhotoImage(file="picTH/bg-selfcheck.png")
        self.bg3 = tk.Label(self, image=self.bgimg3)
        self.bg3.place(x=0, y=0)

        # Sex label
        sex_label = tk.Label(text="เพศ: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        sex_label.place(x=580, y=185)
        self.sex_var = ttk.Combobox(self, textvariable=self.sex, width=7, font=('Comic Sans MS', 20))
        self.sex_var['values'] = ('Male', 'Female')
        self.sex_var['state'] = 'readonly'
        self.sex_var.place(x=680, y=185)

        # BMI label
        height_label = tk.Label(text="ส่วนสูง(ซม.): ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        height_label.place(x=130, y=130)
        self.height_entry = tk.Entry(self, width=20, bg='#FBECCB', textvariable=self.height, font=('Comic Sans MS', 20))
        self.height_entry.place(x=260, y=130)
        weight_label = tk.Label(text="น้ำหนัก(กก.): ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        weight_label.place(x=130, y=185)
        self.weight_entry = tk.Entry(self, width=20, bg='#FBECCB', textvariable=self.weight, font=('Comic Sans MS', 20))
        self.weight_entry.place(x=260, y=185)

        # Age label
        age_label = tk.Label(text="อายุ: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        age_label.place(x=580, y=130)
        self.age_var = ttk.Combobox(self, textvariable=self.age, width=7, font=('Comic Sans MS', 20))
        self.age_var['values'] = ('18-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                                  '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older')
        self.age_var['state'] = 'readonly'
        self.age_var.place(x=680, y=130)

        # Sleep time label
        sleep_label = tk.Label(text="เวลานอนโดยเฉลี่ยในหนึ่งวัน(ชม.): ", bg='#F5BFBA', fg='#C74744',
                               font=('Comic Sans MS', 20))
        sleep_label.place(x=130, y=240)
        self.sleep_var = ttk.Combobox(self, textvariable=self.sleep, width=5, font=('Comic Sans MS', 20))
        self.sleep_var['values'] = [n for n in range(24)]
        self.sleep_var['state'] = 'readonly'
        self.sleep_var.place(x=455, y=240)

        # Stroke label
        stroke_label = tk.Label(text="มีโรคหลอดเลือดหัวใจ?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        stroke_label.place(x=130, y=350)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.stroke, style='TRadiobutton')
        rb1.place(x=350, y=350)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.stroke, style='TRadiobutton')
        rb2.place(x=420, y=350)

        # Diffwalking label
        diff_label = tk.Label(text="คุณเดินลำบากหรือไม่?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        diff_label.place(x=580, y=405)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.diff, style='TRadiobutton')
        rb1.place(x=800, y=405)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.diff, style='TRadiobutton')
        rb2.place(x=870, y=405)

        # Alcohol label
        alc_label = tk.Label(text="คุณดื่มแอลกอฮอล์หนักไหม?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        alc_label.place(x=130, y=405)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.alc, style='TRadiobutton')
        rb1.place(x=380, y=405)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.alc, style='TRadiobutton')
        rb2.place(x=450, y=405)

        # Physical Activity
        phy_label = tk.Label(text="ออกกำลังกายเป็นประจำไหม?: ", bg='#F5BFBA', fg='#C74744',
                             font=('Comic Sans MS', 20))
        phy_label.place(x=130, y=460)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.phy, style='TRadiobutton')
        rb1.place(x=390, y=460)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.phy, style='TRadiobutton')
        rb2.place(x=460, y=460)

        # Diabetic label
        dia_label = tk.Label(text="เป็นเบาหวาน?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        dia_label.place(x=580, y=295)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.dia, style='TRadiobutton')
        rb1.place(x=700, y=295)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.dia, style='TRadiobutton')
        rb2.place(x=770, y=295)
        rb2 = ttk.Radiobutton(self, text='ไม่(เบาหวานแฝง)', value='No, borderline diabetes', variable=self.dia,
                              style='TRadiobutton')
        rb2.place(x=840, y=295)

        # Asthma label
        asth_label = tk.Label(text="หอบหืด?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        asth_label.place(x=580, y=350)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.asth, style='TRadiobutton')
        rb1.place(x=700, y=350)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.asth, style='TRadiobutton')
        rb2.place(x=770, y=350)

        # Kidney label
        kidney_label = tk.Label(text="เป็นโรคไตไหม?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        kidney_label.place(x=580, y=460)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.kidney, style='TRadiobutton')
        rb1.place(x=800, y=460)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.kidney, style='TRadiobutton')
        rb2.place(x=870, y=460)

        # Skin label
        skin_label = tk.Label(text="เป็นมะเร็งผิวหนัง?: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        skin_label.place(x=130, y=295)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.skin, style='TRadiobutton')
        rb1.place(x=350, y=295)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.skin, style='TRadiobutton')
        rb2.place(x=420, y=295)

        # General Health label
        gen_label = tk.Label(text="สุขภาพโดยรวมของคุณ: ", bg='#F5BFBA', fg='#C74744', font=('Comic Sans MS', 20))
        gen_label.place(x=580, y=240)
        self.gen_var = ttk.Combobox(self, textvariable=self.gen, width=10, font=('Comic Sans MS', 20))
        # self.gen_var['text'] = ('แย่', 'ปานกลาง', 'ดี', 'ดีมาก', 'ดีสุดๆ')
        self.gen_var['values'] = ('Poor', 'Fair', 'Good', 'Very good', 'Excellent')
        self.gen_var['state'] = 'readonly'
        self.gen_var.place(x=800, y=240)

        # Smoke label
        gen_label = tk.Label(text="คุณสูบบุหรี่มากกว่า 100 มวนในชีวิตนี้ไหม?", bg='#F5BFBA', fg='#C74744',
                             font=('Comic Sans MS', 20))
        gen_label.place(x=130, y=515)
        rb1 = ttk.Radiobutton(self, text='ใช่', value='Yes', variable=self.smoking, style='TRadiobutton')
        rb1.place(x=600, y=515)
        rb2 = ttk.Radiobutton(self, text='ไม่', value='No', variable=self.smoking, style='TRadiobutton')
        rb2.place(x=670, y=515)
        self.menu_button()
        self.check_all_fill()

    def back_to_check(self):
        self.back = ImageTk.PhotoImage(Image.open("picTH/back.png"))
        tk.Button(self, image=self.back,
                  command=self.self_check_handler,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=950, y=50)
        self.reset_boxes()

    def check_all_fill(self):
        prototype = [self.height.get(), self.weight.get(), self.smoking.get(), self.alc.get(), self.stroke.get(),
                     self.diff.get(), self.sex.get(), self.age.get(), self.dia.get(), self.phy.get(),
                     self.gen.get(), self.sleep.get(), self.asth.get(), self.kidney.get(), self.skin.get()]
        ccount = 1
        for i in prototype:
            self.check_num()
            if len(i.strip()) == 0:
                fill_label = tk.Label(text="โปรดกรอกข้อมูลให้ครบ", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 30))
                fill_label.place(x=400, y=550)
                if ccount > 1:
                    playsound('warning.wav')
                fill_label.after(2000, fill_label.destroy)
                self.button1 = tk.Button(self, text="ตรวจ!", width=7, font=('Comic Sans MS', 25),
                                         command=self.check_all_fill)
                self.button1.place(x=850, y=550)
                break
            elif ccount == 15:
                playsound('click sound.wav')
                fill_label = tk.Label(text="คุณพร้อมที่จะดูผลวิเคราะห์แล้วหรือยัง?", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 30))
                fill_label.place(x=350, y=550)
                self.button1 = tk.Button(self, text="พร้อม!", width=7, font=('Comic Sans MS', 25),
                                         command=self.bmi_cal)
                self.button1.place(x=850, y=550)
            else:
                ccount += 1

    def result_page(self):
        self.loadingb()
        if self.result == 'Yes':
            self.yesimg = ImageTk.PhotoImage(file="picTH/yes.png")
            self.yes = tk.Label(self, image=self.yesimg)
            self.yes.place(x=0, y=0)
        else:
            self.noimg = ImageTk.PhotoImage(file="picTH/no.png")
            self.no = tk.Label(self, image=self.noimg)
            self.no.place(x=0, y=0)
        self.menu_button()
        self.back_to_check()

    def hotline_handler(self):
        self.dele()
        self.f2 = tk.Frame(self, width=1080, height=608, bg='#F5BFBA')
        self.f2.place(x=0, y=0)
        webbrowser.open('https://www.bumrungrad.com/th/blog-news/line-heart-center')
        self.init_components()

    def bmi_cal(self):
        playsound('click sound2.wav')
        self.dele()
        if self.height.get().isnumeric() and self.weight.get().isnumeric():
            height = float(self.height.get())
            weight = float(self.weight.get())
            height /= 100
            self.bmi = weight / height * height
        else:
            fill_label = tk.Label(text="กรุณากรอกตัวเลข", bg='#F5BFBA',
                                  fg='#C74744', font=('Comic Sans MS', 20))
            fill_label.place(x=750, y=50)
            fill_label.after(3000, fill_label.destroy)
            raise ValueError("กรุณากรอกตัวเลข")

        self.user_data_lst = ['Null', self.bmi, self.smoking.get(), self.alc.get(), self.stroke.get(), 'Null',
                              'Null', self.diff.get(), self.sex.get(), self.age.get(), 'Null', self.dia.get(),
                              self.phy.get(),
                              self.gen.get(), float(self.sleep.get()), self.asth.get(), self.kidney.get(),
                              self.skin.get()]
        cl = AppController()
        self.result = cl.ml(self.user_data_lst)
        self.menu_button()
        self.result_page()

    def knowledge_handler(self):
        self.dele()
        self.bgimg4 = ImageTk.PhotoImage(file="picTH/bg-knowledge.png")
        self.bg4 = tk.Label(self, image=self.bgimg4)
        self.bg4.place(x=0, y=0)
        self.menu_button()
        self.kno_menu1 = ImageTk.PhotoImage(Image.open("picTH/what.png"))
        self.kno_menu2 = ImageTk.PhotoImage(Image.open("picTH/protect.png"))
        self.kno_menu3 = ImageTk.PhotoImage(Image.open("picTH/remedy.png"))

        tk.Button(self, image=self.kno_menu1,
                  command=self.info_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=150, y=230)
        tk.Button(self, image=self.kno_menu2,
                  command=self.prevention_page,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=450, y=230)
        tk.Button(self, image=self.kno_menu3,
                  command=self.remedy_page1,
                  border=0,
                  bg='#F1716B',
                  activebackground='#F1716B').place(x=750, y=230)

    def info_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.info = ImageTk.PhotoImage(file="picTH/info.png")
        self.info_bg = tk.Label(self, image=self.info)
        self.info_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def sym_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.sym = ImageTk.PhotoImage(file="picTH/symptoms.png")
        self.sym_bg = tk.Label(self, image=self.sym)
        self.sym_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def cau_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.cau = ImageTk.PhotoImage(file="picTH/causes.png")
        self.cau_bg = tk.Label(self, image=self.cau)
        self.cau_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def risk_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.ris = ImageTk.PhotoImage(file="picTH/risks.png")
        self.ris_bg = tk.Label(self, image=self.ris)
        self.ris_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.kno_menu_button()

    def prevention_page(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.pre = ImageTk.PhotoImage(file="picTH/prevention_bg.png")
        self.pre_bg = tk.Label(self, image=self.pre)
        self.pre_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()

    def remedy_page1(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.medi = ImageTk.PhotoImage(file="picTH/medi.png")
        self.medi_bg = tk.Label(self, image=self.medi)
        self.medi_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.lr_button()

    def remedy_page2(self):
        playsound('click sound2.wav')
        self.f1.destroy()
        self.sur = ImageTk.PhotoImage(file="picTH/surge.png")
        self.sur_bg = tk.Label(self, image=self.sur)
        self.sur_bg.place(x=0, y=0)
        self.back_button()
        self.menu_button()
        self.lr_button()

    def check_num(self):
        if self.height.get() != "":
            if not self.height.get().isnumeric():
                playsound('warning.wav')
                fill_label = tk.Label(text="กรุณากรอกตัวเลขให้เหมาะสม", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=700, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("กรุณากรอกตัวเลขให้เหมาะสม")
            elif float(self.height.get()) < 0 or float(self.height.get()) > 300:
                playsound('warning.wav')
                fill_label = tk.Label(text="กรุณากรอกตัวเลขให้เหมาะสม", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=700, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("กรุณากรอกตัวเลขให้เหมาะสม")
        if self.weight.get() != "":
            if not self.weight.get().isnumeric():
                playsound('warning.wav')
                fill_label = tk.Label(text="กรุณากรอกตัวเลขให้เหมาะสม", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=700, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("กรุณากรอกตัวเลขให้เหมาะสม")
            elif float(self.height.get()) < 0:
                playsound('warning.wav')
                fill_label = tk.Label(text="กรุณากรอกตัวเลขให้เหมาะสม", bg='#F5BFBA',
                                      fg='#C74744', font=('Comic Sans MS', 20))
                fill_label.place(x=700, y=50)
                fill_label.after(3000, fill_label.destroy)
                raise ValueError("กรุณากรอกตัวเลขให้เหมาะสม")
