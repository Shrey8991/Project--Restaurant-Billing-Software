from tkinter import *
from tkinter import ttk, messagebox
import math, random,os
class bill_app:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1350x2000+0+0")
        self.root.title("Billing software")
        bg_color = "#074463"
        title = Label(self.root, text = "Restaurant Billing Software", bd =8, relief = GROOVE,bg = "gray26",fg="white",font = ("times new roman",20,"bold"),pady=2).pack(fill=X)


        #================================declaring variables==========================================
        #=============starter variables=====
        self.pt = IntVar()
        self.dv = IntVar()
        self.pp = IntVar()
        self.kd = IntVar()
        self.vc = IntVar()
        self.ff = IntVar()
        self.bp = IntVar()
        self.brp = IntVar()
        self.kb = IntVar()
        self.sms = IntVar()
        self.vm = IntVar()
        self.sv = IntVar()
        self.cb = IntVar()
        self.snd = IntVar()
        self.momo = IntVar()
        self.gb = IntVar()

        #=============main course variables=======
        self.bir = IntVar()
        self.pbm = IntVar()
        self.dam = IntVar()
        self.msd = IntVar()
        self.pap = IntVar()
        self.chm = IntVar()
        self.dlf = IntVar()
        self.mtp = IntVar()
        self.clc = IntVar()
        self.kdc = IntVar()
        self.c65 = IntVar()
        self.trt = IntVar()
        self.plr = IntVar()
        self.btrn = IntVar()
        self.prc = IntVar()
        self.vgp = IntVar()

        #===============desserts var============
        self.ice = IntVar()
        self.cus = IntVar()
        self.cld = IntVar()
        self.fal = IntVar()
        self.cake = IntVar()
        self.pudd = IntVar()
        self.swt = IntVar()
        self.srknd = IntVar()

        #==============total product price var=== 
        self.tsp = StringVar()
        self.mcp = StringVar()
        self.dsp = StringVar()

        self.st = StringVar()
        self.sc = StringVar()
        self.gst = StringVar()

        #=============customer var=========
        self.c_name= StringVar()
        self.c_pno = StringVar()
        self.c_bill = StringVar()
        x = random.randint(1000,9999)
        self.c_bill.set((str(x)))

        self.search_bill = StringVar()


        
        #===================Customer Detail Frame================================================
        F1 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Customer Details", font = ("times new roman",15,"bold"), fg="gold", bg="gray28")
        F1.place(x=0,y=52,width = 1350, height=80)

        cname_label = Label(F1, text="Customer Name", bg = "gray28", fg = "white", font=("times new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=2)
        cname_txt = Entry(F1,width=15,textvariable = self.c_name, font=("arial 15",12),bd=4,relief= SUNKEN).grid(row=0, column=1, padx=5,pady=2)

        cphone_label = Label(F1, text="Phone No.", bg = "gray28", fg = "white", font=("times new roman", 13, "bold")).grid(row=0, column=2, padx=20, pady=2)
        cphone_txt = Entry(F1,width=15,textvariable = self.c_pno, font=("arial 15",12),bd=4,relief= SUNKEN).grid(row=0, column=3, padx=5, pady=2)


        self.bill_list=[i.split(".")[0] for i in os.listdir("bills/")]
        
        cbill_label = Label(F1, text="Bill Number", bg = "gray28", fg = "white", font=("times new roman", 13, "bold")).grid(row=0, column=4, padx=20, pady=2)
        cbill_txt = ttk.Combobox(F1,width=15,textvariable = self.search_bill, values = self.bill_list).grid(row=0, column=5, padx=5, pady=2)
        
        bill_btn = Button(F1, text = "Search",command = self.find_bill, width=7, bd=4, font = "arial 12 bold").grid(row=0,column =6, padx=20, pady=10)


        #====================Starters dish frame===================================================

        F2 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Starters 1", font = ("times new roman",15,"bold"), fg="lightskyblue", bg=bg_color)   
        F2.place(x=5,y=135,width = 195, height=450)

        #==== adding a canvas to the frame====
        #c = Canvas(F2, bg = "yellow")
        #c.grid(row=15, column=0, sticky = "news")

        #====link a scrollbar to a canvas====
        #scroll = Scrollbar(F2,orient="vertical", command= c.yview)
        #scroll.grid(row=0, column=1, sticky='ns')
        #c.configure(yscrollcommand = scroll.set)

        #frame_buttons = Frame(c, bg="blue")
        #c.create_window((0, 0), window=frame_buttons, anchor='nw')

        

        paneer_label = Label(F2, text = "Paneer Tikka", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=0,column=0, padx=5,pady=5, sticky="w")
        paneer_txt = Entry(F2, width=3,textvariable = self.pt, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        dahi_label = Label(F2, text = "Dahi Vada", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=1,column=0, padx=5,pady=5, sticky="w")
        dahi_txt = Entry(F2, width=3,textvariable = self.dv, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        pani_label = Label(F2, text = "Pani Puri", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=2,column=0, padx=5,pady=5, sticky="w")
        pani_txt = Entry(F2, width=3,textvariable = self.pp, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        khaman_label = Label(F2, text = "Khaman Dhokla", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=3,column=0, padx=5,pady=5, sticky="w")
        khaman_txt = Entry(F2, width=3,textvariable = self.kd, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        cutlet_label = Label(F2, text = "Veg Cutlet", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=4,column=0, padx=5,pady=5, sticky="w")
        cutlet_txt = Entry(F2, width=3,textvariable = self.vc, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fries_label = Label(F2, text = "French Fries", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=5,column=0, padx=5,pady=5, sticky="w")
        fries_txt = Entry(F2, width=3,textvariable = self.ff, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        Bhel_label = Label(F2, text = "Bhel Puri", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=6,column=0, padx=5,pady=5, sticky="w")
        Bhel_txt = Entry(F2, width=3,textvariable = self.bp, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        bread_label = Label(F2, text = "Bread Pakora", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=7,column=0, padx=5,pady=5, sticky="w")
        bread_txt = Entry(F2, width=3,textvariable = self.brp, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)

        
        

        #===================== Starters 2====================================================

        F3 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Starters 2", font = ("times new roman",15,"bold"), fg="lightskyblue", bg=bg_color)   
        F3.place(x=205,y=135,width = 200, height=450)


        kabab_label = Label(F3, text = "Kabab", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=0,column=0, padx=5,pady=5, sticky="w")
        kabab_txt = Entry(F3, width=3,textvariable = self.kb, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        samosa_label = Label(F3, text = "Samosa", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=1,column=0, padx=5,pady=5, sticky="w")
        samosa_txt = Entry(F3, width=3,textvariable = self.sms, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        manchurian_label = Label(F3, text = "Veg Manchurian", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=2,column=0, padx=5,pady=5, sticky="w")
        manchurian_txt = Entry(F3, width=3,textvariable = self.vm, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        vada_label = Label(F3, text = "Sambar Vada", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=3,column=0, padx=5,pady=5, sticky="w")
        vada_txt = Entry(F3, width=3,textvariable = self.sv, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        ball_label = Label(F3, text = "Cheese Ball", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=4,column=0, padx=5,pady=5, sticky="w")
        ball_txt = Entry(F3, width=3,textvariable = self.cb, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sand_label = Label(F3, text = "Sandwich", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=5,column=0, padx=5,pady=5, sticky="w")
        sand_txt = Entry(F3, width=3,textvariable = self.snd, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        momos_label = Label(F3, text = "Momos", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=6,column=0, padx=5,pady=5, sticky="w")
        momos_txt = Entry(F3, width=3,textvariable = self.momo, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        garlic_label = Label(F3, text = "Garlic Bread", font = ("times new roman",12,"bold"),bg=bg_color, fg="lightgreen").grid(row=7,column=0, padx=5,pady=5, sticky="w")
        garlic_txt = Entry(F3, width=3,textvariable = self.gb, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)        

  
        #=====================  Main Course 1==============================================

        c = "darkslategray" # frame color
        f = "white"  # font color

        F4 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Main Course 1", font = ("times new roman",15,"bold"), fg="palegreen", bg=c)   
        F4.place(x=410,y=135,width = 200, height=450)


        c1_label = Label(F4, text = "Biryani", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=0,column=0, padx=5,pady=5, sticky="w")
        c1_txt = Entry(F4, width=3,textvariable = self.bir, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_label = Label(F4, text = "Paneer But Mas", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=1,column=0, padx=5,pady=5, sticky="w")
        c2_txt = Entry(F4, width=3,textvariable = self.pbm, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_label = Label(F4, text = "Dal Makhani", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=2,column=0, padx=5,pady=5, sticky="w")
        c3_txt = Entry(F4, width=3,textvariable = self.dam, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_label = Label(F4, text = "Masala Dosa", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=3,column=0, padx=5,pady=5, sticky="w")
        c4_txt = Entry(F4, width=3,textvariable = self.msd, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_label = Label(F4, text = "Paalak Paneer", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=4,column=0, padx=5,pady=5, sticky="w")
        c5_txt = Entry(F4, width=3,textvariable = self.pap, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_label = Label(F4, text = "Chana Masala", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=5,column=0, padx=5,pady=5, sticky="w")
        c6_txt = Entry(F4, width=3,textvariable = self.chm, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        c7_label = Label(F4, text = "Daal Fry", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=6,column=0, padx=5,pady=5, sticky="w")
        c7_txt = Entry(F4, width=3,textvariable = self.dlf, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        c8_label = Label(F4, text = "Matar Paneer", font = ("times new roman",12,"bold"),bg=c, fg=f).grid(row=7,column=0, padx=5,pady=5, sticky="w")
        c8_txt = Entry(F4, width=3,textvariable = self.mtp, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)  



        #=====================  Main Course 2================================================
        d = "darkslategray" # frame color
        e = "white"  # font color

        F5 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Main Course 2", font = ("times new roman",15,"bold"), fg="palegreen", bg=d)   
        F5.place(x=615,y=135,width = 200, height=450)


        d1_label = Label(F5, text = "Chilli Chicken", font = ("times new roman",12,"bold"), bg = d,fg=e).grid(row=0,column=0, padx=5,pady=5, sticky="w")
        d1_text = Entry(F5, width=3,textvariable = self.clc, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        d2_label = Label(F5, text = "Kadhai Chicken", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=1,column=0, padx=5,pady=5, sticky="w")
        d2_txt = Entry(F5, width=3,textvariable = self.kdc, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        d3_label = Label(F5, text = "Chicken 65", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=2,column=0, padx=5,pady=5, sticky="w")
        d3_txt = Entry(F5, width=3,textvariable = self.c65, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        d4_label = Label(F5, text = "Tandoori Roti", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=3,column=0, padx=5,pady=5, sticky="w")
        d4_txt = Entry(F5, width=3,textvariable = self.trt, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        d5_label = Label(F5, text = "Plain Roti", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=4,column=0, padx=5,pady=5, sticky="w")
        d5_txt = Entry(F5, width=3,textvariable = self.plr, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        d6_label = Label(F5, text = " Butter Naan", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=5,column=0, padx=5,pady=5, sticky="w")
        d6_txt = Entry(F5, width=3,textvariable = self.btrn, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        d7_label = Label(F5, text = "Plain Rice", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=6,column=0, padx=5,pady=5, sticky="w")
        d7_txt = Entry(F5, width=3,textvariable = self.prc, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        d8_label = Label(F5, text = "Veg Pulao", font = ("times new roman",12,"bold"),bg=d, fg=e).grid(row=7,column=0, padx=5,pady=5, sticky="w")
        d8_txt = Entry(F5, width=3,textvariable = self.vgp, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)             


        #=====================  Deserts =====================================================

        a = "darkolivegreen" # frame color
        b = "Antiquewhite1"  # font color

        F6 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Desserts", font = ("times new roman",15,"bold"), fg="gold", bg=a)   
        F6.place(x=820,y=135,width = 160, height=450)


        e1_label = Label(F6, text = "Ice-Cream", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=0,column=0, padx=5,pady=5, sticky="w")
        e1_text = Entry(F6, width=3,textvariable = self.ice, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        e2_label = Label(F6, text = "Custard", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=1,column=0, padx=5,pady=5, sticky="w")
        e2_txt = Entry(F6, width=3,textvariable = self.cus, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        e3_label = Label(F6, text = "Cold Drink", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=2,column=0, padx=5,pady=5, sticky="w")
        e3_txt = Entry(F6, width=3,textvariable = self.cld, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        e4_label = Label(F6, text = "Faluda", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=3,column=0, padx=5,pady=5, sticky="w")
        e4_txt = Entry(F6, width=3,textvariable = self.fal, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        e5_label = Label(F6, text = "Cake", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=4,column=0, padx=5,pady=5, sticky="w")
        e5_txt = Entry(F6, width=3,textvariable = self.cake, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        e6_label = Label(F6, text = "Pudding", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=5,column=0, padx=5,pady=5, sticky="w")
        e6_txt = Entry(F6, width=3,textvariable = self.pudd, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        e7_label = Label(F6, text = "Sweets", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=6,column=0, padx=5,pady=5, sticky="w")
        e7_txt = Entry(F6, width=3,textvariable = self.swt, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        e8_label = Label(F6, text = "Srikhand", font = ("times new roman",12,"bold"),bg=a, fg=b).grid(row=7,column=0, padx=5,pady=5, sticky="w")
        e8_txt = Entry(F6, width=3,textvariable = self.srknd, font = ("times new roman",16,"bold"),bd=2, relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)             


        #=============Bill Area===========================================================
        F7 = Frame(self.root, bd=8, relief=GROOVE)
        F7.place(x=990,y=135,width = 357, height=450)
        bill_label = Label(F7, text="Bill Area", font = "arial 15 bold", bd =7,relief = GROOVE).pack(fill=X)
        scrol = Scrollbar(F7, orient = VERTICAL)
        self.textarea = Text(F7, yscrollcommand=scrol.set)
        scrol.pack(side = RIGHT, fill=Y)
        scrol.config(command= self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        #==============Menu Button frame======================================================
        F8 = LabelFrame(self.root, bd=8, relief=GROOVE, text = "Bill Menu", font = ("times new roman",20,"bold"), fg="white", bg="gray17")   
        F8.place(x=0,y=587,relwidth = 1, height=148)

        m1 = Label(F8,text = "Total Starter's Price",bg="gray17",fg ="peachpuff", font =("times new roman", 14, "bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text = Entry(F8, width = 18,textvariable = self.tsp, font = "arial 10 bold",bd=6, relief = SUNKEN).grid(row=0, column =1, padx=10, pady=1)

        m2 = Label(F8,text = "Main Course Price",bg="gray17",fg ="peachpuff", font =("times new roman", 14, "bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_text = Entry(F8, width = 18,textvariable = self.mcp, font = "arial 10 bold",bd=6, relief = SUNKEN).grid(row=1, column =1, padx=10, pady=1)

        m3 = Label(F8,text = "Desserts Price",bg="gray17",fg ="peachpuff", font =("times new roman", 14, "bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_text = Entry(F8, width = 18,textvariable = self.dsp, font = "arial 10 bold",bd=6, relief = SUNKEN).grid(row=2, column =1, padx=10, pady=1)

        m4 = Label(F8,text = "Service Tax",bg="gray17",fg ="peachpuff", font =("times new roman", 14, "bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        m4_text = Entry(F8, width = 18,textvariable = self.st, font = "arial 10 bold",bd=6, relief = SUNKEN).grid(row=0, column =3, padx=10, pady=1)

        m5 = Label(F8,text = "Service Charge",bg="gray17",fg ="peachpuff", font =("times new roman", 14, "bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        m5_text = Entry(F8, width = 18,textvariable = self.sc, font = "arial 10 bold",bd=6, relief = SUNKEN).grid(row=1, column =3, padx=10, pady=1)

        m6 = Label(F8,text = "GST",bg="gray17",fg ="peachpuff", font =("times new roman", 14, "bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        m6_text = Entry(F8, width = 18,textvariable = self.gst, font = "arial 10 bold",bd=6, relief = SUNKEN).grid(row=2, column =3, padx=10, pady=1)

        #==========Button Frame inside the F8 frame ==========
        btn_f = Frame(F8, bd=7, relief = GROOVE)
        btn_f.place(x=735,y=-1,width=595,height=105)

        total_btn = Button(btn_f, command = self.total, text="Total",bg= "coral4", bd=5, fg="white", pady=15, width=10,height=1, font=("arial 14 bold")).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_f, command = self.bill_area, text="Generate Bill",bg= "coral4", bd=5, fg="white", pady=15, width=10,height=1, font=("arial 14 bold")).grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_f, command = self.clear_data, text="Clear",bg= "coral4", bd=5, fg="white", pady=15, width=10,height=1, font=("arial 14 bold")).grid(row=0,column=2,padx=5,pady=5)
        exit_btn = Button(btn_f,command = self.Exit_app, text="Exit",bg= "coral4", bd=5, fg="white", pady=15, width=10,height=1, font=("arial 14 bold")).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
       
        
    def total(self):

        #=====================================  Price of each item ==================
        # starters
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16 = 60,30,20,45,50,25,16,45,50,42,16,46,40,50,50,45

        # main course
        m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16 = 200,180,150,140,160,170,180,190,200,210,220,160,185,155,160,180

        #desserts
        d1,d2,d3,d4,d5,d6,d7,d8 = 50,45,40,80,45,60,45,50


        self.total_starter_price =  float(
            (self.pt.get()*s1) + (self.dv.get()*s2) + (self.pp.get()*s3) + (self.kd.get()*s4) +(self.vc.get()*s5) +(self.ff.get()*s6) +(self.bp.get()*s7) +(self.brp.get()*s8) +
            (self.kb.get()*s9) +(self.sms.get()*s10) +(self.vm.get()*s11) +(self.sv.get()*s12) +(self.cb.get()*s13) +(self.snd.get()*s14) +(self.momo.get()*s15) +(self.gb.get()*s16) 
        )
        self.tsp.set("Rs. "+str(self.total_starter_price))

        self.total_main_price = float(
            (self.bir.get()*m1) + (self.pbm.get()*m2) + (self.dam.get()*m3) + (self.msd.get()*m4) + (self.pap.get()*m5) + (self.chm.get()*m6) + (self.dlf.get()*m7) + (self.mtp.get()*m8) + 
            (self.clc.get()*m9) + (self.kdc.get()*m10) + (self.c65.get()*m11) + (self.trt.get()*m12) + (self.plr.get()*m13) + (self.btrn.get()*m14) + (self.prc.get()*m15) + (self.vgp.get()*m16) 
        )
        self.mcp.set("Rs. "+str(self.total_main_price))

        self.dessert_price= float(
            (self.ice.get()*d1) + (self.cus.get()*d2) + (self.cld.get()*d3) + (self.fal.get()*d4) + (self.cake.get()*d5) + (self.pudd.get()*d6) + (self.swt.get()*d7) + (self.srknd.get()*d8) 
        )
        self.dsp.set("Rs. "+str(self.dessert_price))

        self.overall_price = float((self.total_starter_price) + (self.total_main_price) + (self.dessert_price))
        self.st_val = round((self.overall_price*0.05),2)
        self.st.set("Rs "+ str(self.st_val))
        self.sc_val = round((self.overall_price*0.02),2)
        self.sc.set("Rs "+ str(self.sc_val))
        self.gst_val = round((self.overall_price*0.04),2)
        self.gst.set("Rs "+ str(self.gst_val))

        self.total_bill = float(self.overall_price + self.st_val + self.sc_val + self.gst_val)



    # I wwant the Welcome_bill function to run when we click on generate bill
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\tWelcome to Gorai Restaurant \n")
        self.textarea.insert(END, f"\n Bill Number : {self.c_bill.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()} ")
        self.textarea.insert(END, f"\n Phone Number : {self.c_pno.get()}")
        self.textarea.insert(END, f"\n========================================")
        self.textarea.insert(END, f"\nFood Items\t\tQuantity\t\t Price")
        self.textarea.insert(END, f"\n========================================")


    def bill_area(self):
        #=====================================  Price of each item ==================
        # starters
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16 = 60,30,20,45,50,25,16,45,50,42,16,46,40,50,50,45

        # main course
        m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16 = 200,180,150,140,160,170,180,190,200,210,220,160,185,155,160,180

        #desserts
        d1,d2,d3,d4,d5,d6,d7,d8 = 50,45,40,80,45,60,45,50


        if self.c_name.get() =="" or self.c_pno.get()=="":
            messagebox.showerror("                 Error", "Customer Details Missing")
        elif self.tsp.get()=="Rs. 0.0" and self.mcp.get()=="Rs. 0.0" and self.dsp.get()=="Rs. 0.0":
            messagebox.showerror("                 Error", "No Product Purchased")
        else:
            self.welcome_bill()
            #=====starters===
            if self.pt.get()!=0:
                self.textarea.insert(END, f"\n Paneer Tikka \t\t {self.pt.get()} \t\t {s1*self.pt.get()}")
            if self.dv.get()!=0:
                self.textarea.insert(END, f"\n Dahi Vada \t\t {self.dv.get()} \t\t {s2*self.dv.get()}")
            if self.pp.get()!=0:
                self.textarea.insert(END, f"\n Pani Puri \t\t {self.pp.get()} \t\t {s3*self.pp.get()}")
            if self.kd.get()!=0:
                self.textarea.insert(END, f"\n khaman Dhokla \t\t {self.kd.get()} \t\t {s4*self.kd.get()}")
            if self.vc.get()!=0:
                self.textarea.insert(END, f"\n Veg Cutlet \t\t {self.vc.get()} \t\t {s5*self.vc.get()}")
            if self.ff.get()!=0:
                self.textarea.insert(END, f"\n French Fries \t\t {self.ff.get()} \t\t {s6*self.ff.get()}")
            if self.bp.get()!=0:
                self.textarea.insert(END, f"\n Bhel Puri \t\t {self.bp.get()} \t\t {s7*self.bp.get()}")
            if self.brp.get()!=0:
                self.textarea.insert(END, f"\n Bread Pakora \t\t {self.brp.get()} \t\t {s8*self.brp.get()}")
            if self.kb.get()!=0:
                self.textarea.insert(END, f"\n Kabab         \t\t {self.kb.get()} \t\t {s9*self.kb.get()}")
            if self.sms.get()!=0:
                self.textarea.insert(END, f"\n Samosa \t\t {self.sms.get()} \t\t {s10*self.sms.get()}")
            if self.vm.get()!=0:
                self.textarea.insert(END, f"\n Veg Manchurian \t\t {self.vm.get()} \t\t {s11*self.vm.get()}")
            if self.sv.get()!=0:
                self.textarea.insert(END, f"\n Sambar Vada \t\t {self.sv.get()} \t\t {s12*self.sv.get()}")
            if self.cb.get()!=0:
                self.textarea.insert(END, f"\n Cheese ball \t\t {self.cb.get()} \t\t {s13*self.cb.get()}")
            if self.snd.get()!=0:
                self.textarea.insert(END, f"\n Sandwich \t\t {self.snd.get()} \t\t {s14*self.snd.get()}")
            if self.momo.get()!=0:
                self.textarea.insert(END, f"\n Momos \t\t {self.momo.get()} \t\t {s15*self.momo.get()}")
            if self.gb.get()!=0:
                self.textarea.insert(END, f"\n Garlic Bread \t\t {self.gb.get()} \t\t {s16*self.gb.get()}")


            #====== main course======
            if self.bir.get()!=0:
                self.textarea.insert(END, f"\n Biryani \t\t {self.bir.get()} \t\t {m1*self.bir.get()}")
            if self.pbm.get()!=0:
                self.textarea.insert(END, f"\n Paneer But Mas\t\t {self.pbm.get()} \t\t {m2*self.pbm.get()}")
            if self.dam.get()!=0:
                self.textarea.insert(END, f"\n Daal Makhani \t\t {self.dam.get()} \t\t {m3*self.dam.get()}")
            if self.msd.get()!=0:
                self.textarea.insert(END, f"\n Masala Dosa \t\t {self.msd.get()} \t\t {m4*self.msd.get()}")
            if self.pap.get()!=0:
                self.textarea.insert(END, f"\n Palak Paneer \t\t {self.pap.get()} \t\t {m5*self.pap.get()}")
            if self.chm.get()!=0:
                self.textarea.insert(END, f"\n Chana Masala \t\t {self.chm.get()} \t\t {m6*self.chm.get()}")
            if self.dlf.get()!=0:
                self.textarea.insert(END, f"\n Daal Fry \t\t {self.dlf.get()} \t\t {m7*self.dlf.get()}")
            if self.mtp.get()!=0:
                self.textarea.insert(END, f"\n Matar Paneer \t\t {self.mtp.get()} \t\t {m8*self.mtp.get()}")
            if self.clc.get()!=0:
                self.textarea.insert(END, f"\n Chili Chicken \t\t {self.clc.get()} \t\t {m9*self.clc.get()}")
            if self.kdc.get()!=0:
                self.textarea.insert(END, f"\n Kadhai Chicken \t\t {self.kdc.get()} \t\t {m10*self.kdc.get()}")
            if self.c65.get()!=0:
                self.textarea.insert(END, f"\n Chicken 65 \t\t {self.c65.get()} \t\t {m11*self.c65.get()}")
            if self.trt.get()!=0:
                self.textarea.insert(END, f"\n Tandoori Roti \t\t {self.trt.get()} \t\t {m12*self.trt.get()}")
            if self.plr.get()!=0:
                self.textarea.insert(END, f"\n Plain Roti \t\t {self.plr.get()} \t\t {m13*self.plr.get()}")
            if self.btrn.get()!=0:
                self.textarea.insert(END, f"\n Butter naan \t\t {self.btrn.get()} \t\t {m14*self.btrn.get()}")
            if self.prc.get()!=0:
                self.textarea.insert(END, f"\n Plain Rice \t\t {self.prc.get()} \t\t {m15*self.prc.get()}")
            if self.vgp.get()!=0:
                self.textarea.insert(END, f"\n Veg Pulao \t\t {self.vgp.get()} \t\t {m16*self.vgp.get()}")

            #======= desserts=========
            if self.ice.get()!=0:
                self.textarea.insert(END, f"\n Ice Cream \t\t {self.ice.get()} \t\t {d1*self.ice.get()}")
            if self.cus.get()!=0:
                self.textarea.insert(END, f"\n Custard \t\t {self.cus.get()} \t\t {d2*self.cus.get()}")
            if self.cld.get()!=0:
                self.textarea.insert(END, f"\n Cold Drinks \t\t {self.cld.get()} \t\t {d3*self.cld.get()}")
            if self.fal.get()!=0:
                self.textarea.insert(END, f"\n Faluda \t\t {self.fal.get()} \t\t {d4*self.fal.get()}")
            if self.cake.get()!=0:
                self.textarea.insert(END, f"\n Cake \t\t {self.cake.get()} \t\t {d5*self.cake.get()}")
            if self.pudd.get()!=0:
                self.textarea.insert(END, f"\n Pudding \t\t {self.pudd.get()} \t\t {d6*self.pudd.get()}")
            if self.swt.get()!=0:
                self.textarea.insert(END, f"\n Sweets \t\t {self.swt.get()} \t\t {d7*self.swt.get()}")
            if self.srknd.get()!=0:
                self.textarea.insert(END, f"\n Srikhand \t\t {self.srknd.get()} \t\t {d8*self.srknd.get()}")


            self.textarea.insert(END, f"\n----------------------------------------")
            if self.st.get()!="Rs 0.0":
                self.textarea.insert(END, f"Service Tax\t\t\t {self.st.get()}")
            if self.sc.get()!="Rs 0.0":
                self.textarea.insert(END, f"\nService Charge\t\t\t {self.sc.get()}")
            if self.gst.get()!="Rs 0.0":
                self.textarea.insert(END, f"\nGST\t\t\t {self.gst.get()}")

            self.textarea.insert(END, f"\nTotal Bill : \t\t\t Rs {round((self.total_bill),2)}")
            self.textarea.insert(END, f"\n----------------------------------------")
            self.save_bill()

    
    def save_bill(self):
        op = messagebox.askyesno("                 Save Bill", " Do you want to save the bill?")
        if op>0:
            self.bill_data = self.textarea.get("1.0", END)
            f1=open("bills/"+str(self.c_bill.get())+ ".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("                 Saved",f"Bill No.: {self.c_bill.get()} saved successfully")
        else:
            return


    #========find and fetch saved bills==========
    def find_bill(self):
        if self.search_bill.get() == "":
            messagebox.showerror("                  Error", "Select a bill number")
        elif self.search_bill.get() not in self.bill_list:
            messagebox.showerror("                  Error"," Enter a valid bill number")
        else:
            f1 = open(f"bills/{self.search_bill.get()}.txt","r")
            self.textarea.delete('1.0',END)
            for d in f1:
                self.textarea.insert(END,d)
            f1.close()
        
    #============ clear the fields(clear buttomn par kaam karenge)=
    def clear_data(self):
        op = messagebox.askyesno("                  Clear","Do you really want to clear?")
        if op>0:
            #=============starter variables=====
            self.pt.set(0)
            self.dv.set(0)
            self.pp.set(0)
            self.kd.set(0)
            self.vc.set(0)
            self.ff.set(0)
            self.bp.set(0)
            self.brp.set(0)
            self.kb.set(0)
            self.sms.set(0)
            self.vm.set(0)
            self.sv.set(0)
            self.cb.set(0)
            self.snd.set(0)
            self.momo.set(0)
            self.gb.set(0)

            #=============main course variables=======
            self.bir.set(0)
            self.pbm.set(0)
            self.dam.set(0)
            self.msd.set(0)
            self.pap.set(0)
            self.chm.set(0)
            self.dlf.set(0)
            self.mtp.set(0)
            self.clc.set(0)
            self.kdc.set(0)
            self.c65.set(0)
            self.trt.set(0)
            self.plr.set(0)
            self.btrn.set(0)
            self.prc.set(0)
            self.vgp.set(0)

            #===============desserts var============
            self.ice.set(0)
            self.cus.set(0)
            self.cld.set(0)
            self.fal.set(0)
            self.cake.set(0)
            self.pudd.set(0)
            self.swt.set(0)
            self.srknd.set(0)

            #==============total product price var=== 
            self.tsp.set("")
            self.mcp.set("")
            self.dsp.set("")

            self.st.set("")
            self.sc.set("")
            self.gst.set("")

            #=============customer var=========
            self.c_name.set("")
            self.c_pno.set("")
            self.c_bill.set(0)
            x = random.randint(1000,9999)
            self.c_bill.set(str(x))

            self.search_bill.set(0)
            
            self.welcome_bill()


    def Exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()





root = Tk()
root.resizable(False, False)
#scrollbar = Scrollbar(root)
#scrollbar.pack( side = RIGHT, fill = Y )
obj = bill_app(root)
#scrollbar.config( command = obj)
root.mainloop()

