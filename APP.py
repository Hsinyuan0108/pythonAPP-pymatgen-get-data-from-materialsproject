from tkinter import *

from PIL import Image, ImageTk

import matplotlib.pyplot as plt

import os

from pymatgen.ext.matproj import MPRester

from funcs_about_mp import *

import json

class App:
    def __init__(self, master):
        self.master = master

        self.e1 = Entry(self.master,width=15)
        self.e2 = Entry(master,width=15)
        self.e3 = Entry(master,width=40)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)
        self.e3.grid(row=0, column=4, padx=10, pady=5)

        
        # scroll = Scrollbar(root, command=self.t1.yview)
        # scroll.grid(row=2,column = 0,sticky = N + S + E)
        # self.t1.configure(yscrollcommand=scroll.set)
        self.initText()
        self.initTextLabels()
        self.initPics()
        self.initButton()
        self.get_API_KEY()

        self.data_query = data_query(self.key)

    def initText(self) :

        self.t1 = Text( self.master, width=20, height = 20)
        self.t2 = Text( self.master, width=20, height=20)
        self.t3 = Text(self.master,width=20, height=20)
        self.t4 = Text(self.master,width=20, height=20)
        self.t5 = Text(self.master,width=20, height=20)
        self.t6 = Text(self.master,width=10, height=1)
        self.t7 = Text(self.master,width=10, height=1)
        self.t8 = Text(self.master,width=10, height=1)

        self.t1.grid(row=3, padx=10, pady=5)
        self.t2.grid(row=3, column=2, padx=10, pady=5)
        self.t3.grid(row=3, column=3, padx=10, pady=5)
        self.t4.grid(row=5, column=2, padx=10, pady=5)
        self.t5.grid(row=5, column=3, padx=10, pady=5)
        self.t6.grid(row=7, column=1, padx=10, pady=5)
        self.t7.grid(row=7, column=2, padx=10, pady=5)
        self.t8.grid(row=7, column=3, padx=10, pady=5)
    def initTextLabels(self):     
                   
        Label(self.master, text="你想查询的元素或化学式：").grid(row=0)
        Label(self.master, text="你想查询的mpid：").grid(row=1)
        Label(self.master, text="该元素或化学式对应的mpids：").grid(row=2)
        Label(self.master, text="diel：").grid(row=2,column=2)
        Label(self.master, text="blessed_tasks：").grid(row=2,column=3)
        Label(self.master, text="spacegroup：").grid(row=4,column=2)
        Label(self.master, text="structure：").grid(row=4,column=3)
        Label(self.master, text="band_width：").grid(row=6,column=1)
        Label(self.master, text="density：").grid(row=6,column=2)
        Label(self.master, text='pretty_formula' ).grid(row=6,column=3)
        Label(self.master, text="输入获得多个mpid数据（mpid间，分隔）").grid(row=0,column=3)

    def initPics(self):  
                         
        self.init_img_open = Image.open('pics/init_pic.png')
        new_x = 360
        new_y = 360
        self.out = self.init_img_open.resize((new_x, new_y), Image.ANTIALIAS)
        self.init_img = ImageTk.PhotoImage(self.out)
        self.bs_dos_label_img = Label( self.master )
        self.bs_dos_label_img.config(image=self.init_img)
        self.bs_dos_label_img.grid( row = 3, column = 5 )  
        self.bs_dos_label_img.image=self.init_img
        self.bs_label_img = Label( self.master )
        self.bs_label_img.grid(row = 3, column = 4)
        self.bs_label_img.config(image=self.init_img)  
        self.bs_label_img.image=self.init_img     
  
    def initButton(self):  

        self.b1 = Button(self.master, text='查找mpids', font=('Arial',12), width=10, height=1, command = lambda : self.get_ids())#,// command=get_ids()
        self.b1.grid(row=0, column=2, padx=10, pady=5)
        self.b4 = Button(self.master, text='得到基本信息', font=('Arial',12), width=10, height=1,command = lambda : self.get_basic_information()) # , command=get_basic_information
        self.b4.grid(row=1, column=2, padx=10, pady=5)
        self.b2 = Button(self.master, text='得到能带图', font=('Arial',12), width=10, height=1, command = lambda : self.get_basic_band_structure()).grid(row=2, column=4, padx=10, pady=5) #, command=get_basic_band_tructure
        self.b3 = Button(self.master, text='得到能带与态密度图', font=('Arial',12), width=20, height=1, command = lambda : self.get_bs_dos()).grid(row=2, column=5, padx=10, pady=5) # , command=get_bs_dos
        self.b4 = Button(self.master, text='获取全部数据', font=('Arial',12), width=10, height=1, command = lambda : self.get_mulitple_data()).grid(row=0, column=5, padx=10, pady=5)

 
    def get_basic_band_structure(self):     
        id = (self.e2.get())
        self.data_query.gen_bs_plot(id)
        img_open = Image.open('pics/basic_band_structure.png')
        new_x = 360
        new_y = 180
        out = img_open.resize((new_x, new_y), Image.ANTIALIAS)
        self.bbt = ImageTk.PhotoImage(out)
        self.bs_label_img.config(image=self.bbt)  
        self.bs_label_img.image=self.bbt

    def get_bs_dos(self):                     
        id = (self.e2.get())
        self.data_query.gen_bs_dos(id)
        img_open = Image.open('pics/bs_dos.png')
        new_x = 360
        new_y = 360
        out = img_open.resize((new_x, new_y), Image.ANTIALIAS)
        self.bd = ImageTk.PhotoImage(out)
        self.bs_dos_label_img.config(image=self.bd)  
        self.bs_dos_label_img.image=self.bd 

    def get_ids( self ):                 
        input = self.e1.get()
        data = self.data_query.IDandPrettyFormula(input)
        if "*" in input:         #当带有*时会输出所有相关化合物的id和化学式
            self.t1.delete('1.0', 'end')
            self.t1.insert('end',"all material_ids and pretty formula:")
            self.t1.insert(INSERT, '\n')
            for i in data:
                self.t1.insert('end',i['material_id'])
                self.t1.insert('end',i['pretty_formula'])
                self.t1.insert(INSERT, '\n')
        else:                      #不带有*时输出所有单质的id
            self.t1.delete('1.0', 'end')
            self.t1.insert('end',"all material_ids")
            self.t1.insert(INSERT, '\n')
            for i in data:
                self.t1.insert('end',i['material_id'])
                self.t1.insert(INSERT, '\n')

    def get_basic_information(self):           
        self.id = self.e2.get()


        self.spacegroup = self.data_query.getSpaceGroup(self.id)
        self.structure = self.data_query.getStructure(self.id)
        self.diel = self.data_query.getDiel(self.id)
        self.blessedtasks = self.data_query.getBlessedTasks(self.id)
        self.bondvalence = self.data_query.getBondValence(self.id)
        self.magnetictype = self.data_query.getMagneticType(self.id)
        self.oxidetype = self.data_query.getOxideType(self.id)


        self.prettyformula = self.data_query.getPrettyFormula(self.id)
        self.band_gap = self.data_query.getBandGap(self.id)
        self.density = self.data_query.getDensity(self.id)
        self.formation_energy_per_atom = self.data_query.getFormation_energy_per_atom(self.id)
        self.deltavolume = self.data_query.getDeltaVolume(self.id)
        self.eabovehull = self.data_query.getEAboveHull(self.id)

        self.make_json()
        self.show_info()

        


    def get_mulitple_data(self):

        strvar = self.e3.get()
        List = strvar.split(",")
        i = 0
        for i in range(len(List)):
            id = List[i]
            dic = self.make_dict(id)
            Exist = os.path.exists(id)
            if not Exist:
                os.makedirs(id)
            with open(id + '/' + 'basic_information' + '.json', 'w') as file:
                json.dump(dic, file)
            
    def show_info ( self ):

        self.t2.delete('1.0', 'end')

        for key, value in self.diel[0]['diel'].items():
            self.t2.insert('end', str(key) + ':'+ str(value) )
            self.t2.insert(INSERT, '\n')

        
        self.t3.delete('1.0', 'end')
        for key, value in self.blessedtasks[0]['blessed_tasks'].items():
            self.t3.insert('end', str(key) + ':'+ str(value) )
            self.t3.insert(INSERT, '\n')

        self.t4.delete('1.0', 'end')
        for key, value in self.spacegroup[0]['spacegroup'].items():
            self.t4.insert('end', str(key) + ':'+ str(value) )
            self.t4.insert(INSERT, '\n')


        self.t5.delete('1.0', 'end')
        self.t5.insert('end', self.structure[0]['structure']) 
        self.t6.delete('1.0', 'end')
        self.t6.insert('end', self.band_gap[0]['band_gap']) 
        self.t7.delete('1.0', 'end')
        self.t7.insert('end', self.density[0]['density']) 
        self.t8.delete('1.0', 'end')
        self.t8.insert('end', self.prettyformula[0]['pretty_formula'])

    def make_json ( self ):
        Exist = os.path.exists(self.id)

        if not Exist:
            os.makedirs(self.id)

        dic1 = {'structure': str(self.structure[0]['structure'])}
        dic2 = {'diel': str(self.diel[0]['diel'])}
        dic3 = {'blessedtasks': str(self.blessedtasks[0]['blessed_tasks'])}
        dic4 = {'bondvalence': str(self.bondvalence[0]['bond_valence'])}
        dic5 = {'spacegroup': str(self.spacegroup[0]['spacegroup'])}
        

        dic = dict(**self.prettyformula[0], **self.band_gap[0], **self.deltavolume[0], **self.density[0], **self.eabovehull[0], **self.formation_energy_per_atom[0], **self.magnetictype[0], **self.oxidetype[0],**dic1, **dic2, **dic3, **dic4, **dic5)

        with open(self.id + '/' + 'basic_information' + '.json', 'w') as file:
            json.dump(dic, file)

    def make_dict ( self, id ):

        spacegroup =self. data_query.getSpaceGroup(id)
        structure = self.data_query.getStructure(id)
        diel = self.data_query.getDiel(id)
        blessedtasks = self.data_query.getBlessedTasks(id)
        bondvalence = self.data_query.getBondValence(id)

        prettyformula = self.data_query.getPrettyFormula(id)
        band_gap = self.data_query.getBandGap(id)
        density = self.data_query.getDensity(id)
        formation_energy_per_atom = self.data_query.getFormation_energy_per_atom(id)
        deltavolume = self.data_query.getDeltaVolume(id)
        eabovehull = self.data_query.getEAboveHull(id)
        magnetictype = self.data_query.getMagneticType(id)
        oxidetype = self.data_query.getOxideType(id)

        dic1 = {'structure': str(structure[0]['structure'])}
        dic2 = {'diel': str(diel[0]['diel'])}
        dic3 = {'blessedtasks': str(blessedtasks[0]['blessed_tasks'])}
        dic4 = {'bondvalence': str(bondvalence[0]['bond_valence'])}
        dic5 = {'spacegroup': str(spacegroup[0]['spacegroup'])}

        return dict(**prettyformula[0], **band_gap[0], **deltavolume[0], **density[0], **eabovehull[0], **formation_energy_per_atom[0], **magnetictype[0], **oxidetype[0], **dic1, **dic2, **dic3, **dic4, **dic5)

    def get_API_KEY( self ):
        with open("API_KEY.txt", "r") as f:
            self.key = f.readline()


def start_app():
    root = Tk()
    root.title('材料数据自动化获取软件')
    root.geometry("1920x1080")
    App(root)
    root.mainloop()

