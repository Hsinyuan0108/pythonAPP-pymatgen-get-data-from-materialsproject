from pymatgen.ext.matproj import MPRester
from pymatgen.ext.matproj import Composition, Element
from pymatgen.electronic_structure.plotter import BSDOSPlotter, DosPlotter, BSPlotter

import os
import json


class data_query:

    def __init__(self, KEY):

        self.m = MPRester(KEY)


    def getBandGap(self, ID):
        the_list = self.m.query(criteria={"task_id": ID }, properties=["band_gap"])
        if the_list[0]['band_gap'] is None:
            return ([{'band_gap':{'band_gap':'None'}}])
        else:
            return the_list


    def getDensity(self, ID):
        the_list = self.m.query(criteria={"task_id": ID }, properties=["density"])
        if the_list[0]['density'] is None:
            return ([{'density':{'density':'None'}}])
        else:
            return the_list
    def getSpaceGroup(self, ID):
        the_list = self.m.query(criteria={"task_id": ID }, properties=["spacegroup"] ) 
        if the_list[0]['spacegroup'] is None:
            return ([{'spacegroup':{'spacegroup':'None'}}])
        else:
            return the_list
    def getStructure(self, ID):
        the_list = self.m.query(criteria={"task_id": ID }, properties=['structure'])
        if the_list[0]['structure'] is None:
            return ([{'structure':{'structure':'None'}}])
        else:
            return the_list
    def getFormation_energy_per_atom(self, ID):
        the_list = self.m.query(criteria={"task_id": ID }, properties=['formation_energy_per_atom'])
        if the_list[0]['formation_energy_per_atom'] is None:
            return ([{'formation_energy_per_atom':{'formation_energy_per_atom':'None'}}])
        else:
            return the_list
    def getPrettyFormula(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['pretty_formula'])
        if the_list[0]['pretty_formula'] is None:
            return ([{'band_gap':{'pretty_formula':'None'}}])
        else:
            return the_list
    def getBlessedTasks(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['blessed_tasks'])
        if the_list[0]['blessed_tasks'] is None:
            return ([{'blessed_tasks':{'blessed_tasks':'None'}}])
        else:
            return the_list
    def getBondValence(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['bond_valence'])
        if the_list[0]['bond_valence'] is None:
            return ([{'bond_valence':{'bond_valence':'None'}}])
        else:
            return the_list
    def getDeltaVolume(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['delta_volume'])
        if the_list[0]['delta_volume'] is None:
            return ([{'delta_volume':{'delta_volume':'None'}}])
        else:
            return the_list

    def getDiel(self, ID):
        the_list = self.m.query(criteria={"task_id": ID }, properties=['diel'])
        
        if the_list[0]['diel'] is None:
            return ([{'diel':{'diel':'None'}}])
        else:
            return the_list
    def getEAboveHull(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['e_above_hull'])
        if the_list[0]['e_above_hull'] is None:
            return ([{'e_above_hull':{'e_above_hull':'None'}}])
        else:
            return the_list
    def getMagneticType(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['magnetic_type'])
        if the_list[0]['magnetic_type'] is None:
            return ([{'magnetic_type':{'magnetic_type':'None'}}])
        else:
            return the_list
    def getOxideType(self, ID):
        the_list =  self.m.query(criteria={"task_id": ID }, properties=['oxide_type'] )   
        if the_list[0]['oxide_type'] is None:
            return ([{'oxide_type':{'oxide_type':'None'}}])
        else:
            return the_list
    def print_plot_band_structure (self, ID):
        bs = self.m.get_bandstructure_by_material_id(ID)
        bs_plotter = BSPlotter(bs)
        return bs_plotter.get_plot()

    def IDandPrettyFormula(self, target):
        id_prettyformula = self.m.get_data(target, prop="pretty_formula")

        return id_prettyformula

    def gen_bs_plot(self, ID):
        bs = self.m.get_bandstructure_by_material_id(ID)
        bs_plotter = BSPlotter(bs)
        plt_bs = bs_plotter.get_plot()
        plt_bs.savefig('pics/basic_band_structure.png', format='png')

    def gen_bs_dos(self, ID):
        bs = self.m.get_bandstructure_by_material_id(ID)
        dos  = self.m.get_dos_by_material_id(ID)
        bs_dos = BSDOSPlotter(bs_projection='elements', dos_projection='elements',\
                                vb_energy_range=5, fixed_cb_energy=5)
        plt_bs_dos = bs_dos.get_plot(bs, dos)
        plt_bs_dos.savefig('pics/bs_dos.png', format='png')



def CMD_get_data( target_file ):
    with open("API_KEY.txt", "r") as f:
        key = f.readline()

    d_q = data_query(key)
    with open ( target_file ) as t_f:
        ids = t_f.readline()
        print(ids)
        ids = ids.replace('/n','')
        id_list = ids.split(",")

    for id in id_list:
        print(id)
        spacegroup = d_q.getSpaceGroup(id)
        structure = d_q.getStructure(id)
        diel = d_q.getDiel(id)
        blessedtasks = d_q.getBlessedTasks(id)
        bondvalence = d_q.getBondValence(id)

        magnetictype = d_q.getMagneticType(id)
        oxidetype = d_q.getOxideType(id)
        prettyformula = d_q.getPrettyFormula(id)
        band_gap = d_q.getBandGap(id)
        density = d_q.getDensity(id)
        formation_energy_per_atom = d_q.getFormation_energy_per_atom(id)
        deltavolume = d_q.getDeltaVolume(id)
        eabovehull = d_q.getEAboveHull(id)

        dic1 = {'structure': str(structure[0]['structure'])}
        dic2 = {'diel': str(diel[0]['diel'])}
        dic3 = {'blessedtasks': str(blessedtasks[0]['blessed_tasks'])}
        dic4 = {'bondvalence': str(bondvalence[0]['bond_valence'])}
        dic5 = {'spacegroup': str(spacegroup[0]['spacegroup'])}

        dic = dict(**prettyformula[0], **band_gap[0], **deltavolume[0], **density[0], **eabovehull[0], **formation_energy_per_atom[0], **magnetictype[0], **oxidetype[0], **dic1, **dic2, **dic3, **dic4, **dic5)

        Exist = os.path.exists(id)
        if not Exist:
            os.makedirs(id)

        with open(id + '/' + 'basic_information' + '.json', 'w') as file:
            json.dump(dic, file)

# dos_plotter = DosPlotter()
# dos_plotter.add_dos_dict(dos.get_spd_dos())
# dos_plotter.show()


#print(type(bs_plotter))

#band_fig = BSPlotter(bs)

