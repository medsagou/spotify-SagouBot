# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:37:53 2023

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:49:13 2023

@author: HP
"""

import requests
from bs4 import BeautifulSoup

from datetime import date



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from interaction import SpotifyGenerator
from class_fichier import C_Fichier

import os
import os.path
from os import chdir, mkdir


class C_Liste(list):
    
    def __init__(self,sep=';'):
        self.separateur = sep
    
    def afficher_Liste(self):
        for i in range(len(self)):
            print(self[i],'\n')
    
    def Str_to_List(self,Ligne_Chaine):
        return Ligne_Chaine.split(self.separateur) 
    
    def Liste_to_Str(self,Liste_Elements):
        return self.separateur.join(Liste_Elements) 

    def changer_element(self,E):
        Liste_Tempo=[]
        for i in range(len(self)):
            Element_courant=self[i]
            if E != Element_courant:
               Liste_Tempo=Liste_Tempo + [Element_courant]
            else:               
                print("Veuillez saisir un élément à la place de : ",E,"\n")
                E_modifie= input("Veuillez saisir un élément : ")
                Liste_Tempo=Liste_Tempo + [E_modifie]
        return Liste_Tempo 
    
    
    
    
    
class C_Dossier():

   
    def __init__(self,sep=""):
       self.separateur=sep
    
    def dossier_courant():
        return os.getcwd()

    def existe_dossier(Chemin):
        if os.path.exists(Chemin) :
            return True
        else:
            return False 
        
    def changer_dossier(Chemin):
        if C_Dossier.existe_dossier(Chemin):
            return(chdir(Chemin))
 
        
    def creer_dossier(Chemin):
        if not C_Dossier.existe_dossier(Chemin):
             return(mkdir(Chemin))
         
            
import os.path
from Module_Classe_Liste import C_Liste
            

class C_Fichier():
    #____________________________________________________________________________________________________________________________________________________________
    # Le constructeur d'une instance d'un fichier
    # Ce constructeur permet d'attribuer à une instance de fichier son nom (vide par défaut) 
    # Ce constructeur permet de spécifier le séparateur des éléments s'il existe (également vide par défauté)su
    # Un séparateur peut être un ";", une "," un "#', etc.  
    def __init__(self,NF="",sep="|", sep2="+"):
        self.nomFichier=NF
        self.separateur=sep
        self.separateur2=sep2
    
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def existe_fichier(self):
         if os.path.isfile(self.nomFichier):
             return True
         else:
             return False
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def specifier_Nom_fichier(self):
        while True:
            print("\n")
            print("Instanciation et saisie d'un nouveau fichier de travail :\n")
            self.nomFichier=input("Entrez le chemin de votre fichier : "+"\n")
            if self.existe_fichier():
                print("le fichier spécifié existe déjà dans le répertoire courant, veuillez recommencer")
            else:
                break  
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide sans supprimer le fichier de même nom s'il existe
    def creer_fichier_1(self):
        f = open(self.nomFichier,"x") #Création d'un fichier vide. Ici, le fichier n'est pas écrasé contrairement au mode 'w'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec suppression du fichier de même nom s'il existe
    def creer_fichier_2(self):
        f = open(self.nomFichier,"w") #Création d'un fichier vide. Ici, le fichier existant qui porte le même nom est écrasé contrairement mode 'x'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec possibilité de dialogue avant de supprimer un fichier de même nom s'il existe dans le même répertoire (dossier)
    def creer_fichier_3(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            print("Il existe un fichier qui porte le même nom"+"\n")
            print("Voulez-vous l'écraser ?")
            while True:                             # Itération (boucle infinie) pour prévenir les événetuelles erreurs de frappe (autre chose que '1' et '2') (Attention, il faut absolument provoquer quelque part dans la boucle une rupture avec "break" )
                # Menu local pour exposer les dexu cas de figures (on peut également créer une instance de la classe Menu ici)
                print("Veuillez choisir ce qu'il faut faire, selon les options suivantes : "+"\n")
                print("1. Ecraser le fichier existant")
                print("2. Garder le fichier")
                rep=input("Veuillez taper 1 ou 2 ")
                if rep=='1':                        # Cas où l'utilisateur choisit d'écraser le fichier existant 
                    self.creer_fichier_2()          # Appel à laméthode creer_fichier_2()
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                elif rep=='2':                      # Cas où l'utilisateur choisit de ne pas écraser le fichier existant (pas besoin dans ce cas de faire appel à la méthode creer_fichier_1()) 
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                else:                               # cas où l'utilisateur n'a tapé ni "1", ni"2"
                    print("Erreur de frappe"+"\n")
        else:                                       # cas où le fichier à créer n'existe pas dans le répertoire courant
            self.creer_fichier_1()                  # Appel à laméthode creer_fichier_1()
    
    #____________________________________________________________________________________________________________________________________________________________
    def ActiverFichier(self,Message):
        print(Message)
        self.specifier_Nom_fichier()
        self.creer_fichier_3()                      
 
    #____________________________________________________________________________________________________________________________________________________________
    # Supprimer un fichier
    def supprimer_fichier(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            os.remove(self.nomFichier)
            print("Le fichier a été supprimé")
        else:
            print("Le fichier spécifié n'existe pas dans le répertoire courant")

    #____________________________________________________________________________________________________________________________________________________________
    # Ajouter un élément
    def enregistrer_Element(self,Element):
        with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode lecture.
             F.write(Element)

    #____________________________________________________________________________________________________________________________________________________________
    # Ajouter un ensemble d'éléments sous forme de liste
    def Liste_to_Fichier(self,Liste): # 'creer_Fichier_Avec_Liste_Elements(self,ListeElements)' Créer d'un fichier à partir d'une liste : chaque élément de la liste représente une ligne du fichier
        with open(self.nomFichier,'w') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
            F.writelines(Liste)    

    def str_to_fichier(self,string):
        with open(self.nomFichier,'w') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
             F.write(string)
        return
             
             
    def Liste_to_str_to_Fichier(self,Liste_1): 
       Liste = self.Liste_to_Str1(Liste_1)
       with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
            
            F.writelines(Liste)   
            F.writelines('\n')
    #____________________________________________________________________________________________________________________________________________________________
    # Lire le contenu d'un fichier et le retourne en le plaçant dans une liste
    def Fichier_to_Liste(self):  # extration d'une liste depuis un fichier  : chaque ligne du fichier représente un élément de cette liste
            with open(self.nomFichier, 'r') as f:    # Ouverture du fichier en mode lecture.
                return f.readlines()
    def Fichier_to_str(self):
        with open (self.nomFichier,'r') as f:
            return f.read()

    def supprimer_element(self,element):
        ch = self.Fichier_to_str()
        print(ch)
        chh = ch.replace(element,'')
        print(chh)
        self.str_to_fichier(ch)
        
    #____________________________________________________________________________________________________________________________________________________________
    # Afficher un fichier ligne par ligne
    def afficher_lignes_fichier(self):
        print("\n Affichage des lignes du fichier \n")
        with open(self.nomFichier, 'r') as F:
            for ligne in F:
                print (ligne)               
        print("\n Fin affichage des lignes du fichier")

    #____________________________________________________________________________________________________________________________________________________________
    # Afficher un fichier ligne par ligne et pour chaque ligne mot par mot
    def afficher_mots_fichier(self):
        i=0 # uttiliser comme un simple compteur pour afficher dans un message afin de le rendre plus explicite
        with open(self.nomFichier, 'r') as F:
            for ligne in F:
               i+=1
               print("Affichage des éléments du contenu la ligne : ",i,"\n") # message explicite
               L=C_Liste(ligne.split(self.separateur)) # Création d'une instance de la classe 'C_Liste'
               L.afficher_Liste()  # ici on fait appel à la méthode 'afficher_Liste()' de la classe 'C_Liste'


    def existe_element_fichier(self,Element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element in Liste_Lignes_du_Fichier[i]:
                    return(True)
        return(False)
                 
    
    def existe_element_fichier2(self,element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                L=Liste_Lignes_du_Fichier[i].split(self.separateur)
                if element in L:
                    return(True)
        return(False)
    
    
    def existe_element_fichier3(self,element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                L=Liste_Lignes_du_Fichier[i].split(self.separateur)
                if element in L:
                    return(True, Liste_Lignes_du_Fichier[i])
        return(False,False)

    
    
    def modifier_element_fichier(self,Element):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                Ligne_Courante=Liste_Lignes_du_Fichier[i] # La variable 'Ligne_Courante' est utilisée pour donner plus de clarté sur le plan pédagogique, on peut à la place utiliser directement directement 'Liste_Lignes_du_Fichier[i]'
                Liste_Elements_Ligne_Courante=self.Str_to_List(Ligne_Courante) # Ici on transforme la chaîne de caractère 'Ligne_Courante'  en une liste 'Liste_Elements_Ligne_Courante' 
                if Element not in Liste_Elements_Ligne_Courante:
                    Nouvelle_Liste=Nouvelle_Liste+[Ligne_Courante+'\n']
                else:
                    Nouvelle_Liste=C_Liste(Liste_Elements_Ligne_Courante) # Nouvelle_Liste est une instance de la classe C_Liste
                    Nouvelle_Liste_Elements=Nouvelle_Liste.changer_element(Element)
                    Nouvelle_Ligne_Modifiee=self.Liste_to_Str(Nouvelle_Liste_Elements)
                    Nouvelle_Liste=Nouvelle_Liste+[Nouvelle_Ligne_Modifiee+'\n']    
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def ajouter_a_la_fin_de_la_ligne(self,ID,Element,sep):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                Ligne_Courante=Liste_Lignes_du_Fichier[i] # La variable 'Ligne_Courante' est utilisée pour donner plus de clarté sur le plan pédagogique, on peut à la place utiliser directement directement 'Liste_Lignes_du_Fichier[i]'
                Liste_Elements_Ligne_Courante=self.str_to_liste(Ligne_Courante) # Ici on transforme la chaîne de caractère 'Ligne_Courante'  en une liste 'Liste_Elements_Ligne_Courante' 
                if ID not in Liste_Elements_Ligne_Courante:
                    Nouvelle_Liste=Nouvelle_Liste+[Ligne_Courante+'\n']
                else:
                    Liste_Elements_Ligne_Courante[-1] = Liste_Elements_Ligne_Courante[-1].replace('\n','') +sep+ str(Element)
                    
                    Nouvelle_Liste_Elements=Liste_Elements_Ligne_Courante
                    Nouvelle_Ligne_Modifiee=self.Liste_to_Str1(Nouvelle_Liste_Elements)
                    Nouvelle_Liste=Nouvelle_Liste+[Nouvelle_Ligne_Modifiee+'\n']    
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
       
    
    def Liste_to_Str1(self,Liste_Elements):
        return self.separateur.join(map(str, Liste_Elements))
    
    def Liste_to_Str2(self,Liste_Elements):
        return self.separateur2.join(Liste_Elements)
    
    def supprimer_element_fichier(self,Element):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]+'\n']
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def supprimer_ligne_fichier(self,Element_ligne):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    continue
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def supprimer_ligne_fichier2(self,Element_ligne):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne+"\n" not in Liste_Lignes_du_Fichier[i].split(self.separateur)[-1].split(self.separateur2) and Element_ligne not in Liste_Lignes_du_Fichier[i].split(self.separateur)[-1].split(self.separateur2):
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    continue
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) #
            
    def modiffier_ligne(self,Element_ligne,nv_ligne):
        Nouvelle_Liste=[] 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() 
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    Nouvelle_Liste = Nouvelle_Liste+[nv_ligne + '\n']
            self.Liste_to_Fichier(Nouvelle_Liste) #
        return
        
            

    def str_to_liste(self, string):
        return string.split(self.separateur)
    
    
    def nbre_ligne(self):
        return len(self.Fichier_to_Liste())
       

    def str_to_liste2(self, string):
        return string.split(self.separateur2)





class CC_Class:
    def __init__(self,driver="",list_info_cc = ["","","",""]):
        
        self.driver = driver
        self.number = list_info_cc[0]
        self.date = list_info_cc[1]+"/"+list_info_cc[2][2:]
        self.code = list_info_cc[-1].replace("\n","")
        
        
    def fill_cc_input(self):
        iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[data-testid='pci-frame']")))
        self.driver.switch_to.frame(iframe)
        time.sleep(5)
        # Retrieve the credit card number input field and fill in the value
        try:
            cc_number = self.driver.find_element(By.CSS_SELECTOR, "input[id='cardnumber']")
        except:
            print('ERROR: CARDNUMBER NOTE FOUND')
        else:
            cc_number.send_keys(Keys.CONTROL + "a")
            cc_number.send_keys(Keys.DELETE)
            print("NOTE: CARDNUMBER INSERD")
            cc_number.send_keys(self.number)
            
        try:
            cc_date = self.driver.find_element(By.CSS_SELECTOR, "input[id='expiry-date']")
        except:
            print('ERROR: EXPIRYDATE NOTE FOUND')
        else:
            
            cc_date.send_keys(Keys.CONTROL + "a")
            cc_date.send_keys(Keys.DELETE)
            print("NOTE: EXPIRYDATE INSERD")
            cc_date.send_keys(self.date)
            
            
        try:
            cc_v_code = self.driver.find_element(By.CSS_SELECTOR, "input[id='security-code']")
        except:
            print('ERROR: SECURITYCODE NOTE FOUND')
        else:
            
            cc_v_code.send_keys(Keys.CONTROL + "a")
            cc_v_code.send_keys(Keys.DELETE)
            print("NOTE: SECURITYCODE INSERD")
            cc_v_code.send_keys(self.code)
        self.driver.switch_to.default_content()
        submit_button = self.driver.find_elements(By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0.bYgzuF.encore-bright-accent-set.sc-ksdxAp.fdYigH")
        submit_button[0].click()
        print("NOTE: CC FORM SUBMITED")
        
        
      



class SpotifyGenerator:
    def __init__(self, password="yourPassword"):
        self.driver = ""
        self.email = ""
        self.password = password
        self.cc_file_name = "cc.txt"
        self.regected_cc_file_name = "cc_regected.txt"
        self.data_file = "data.txt"

    def get_driver(self):
        # firefox_profile = webdriver.FirefoxProfile()
        # firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        # driver = webdriver.Firefox(firefox_profile=firefox_profile)
        '''
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'images': 2}}
        options.add_experimental_option('prefs', prefs)
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        '''
        driver = webdriver.Chrome()
        
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://open.spotify.com/")
        print("NOTE: DRIVER CONNECTED")
        return

    def get_Email_from_yopmail(self):

        yopmail_url = 'https://yopmail.com/email-generator'
        response = requests.get(yopmail_url)
        html_content = response.content

        soup = BeautifulSoup(html_content, 'html.parser')

        email_element_container = soup.find(id="geny")
        email = email_element_container.get_text()
        self.email = email
        print("NOTE: EMAIL DONE")
        return

    def go_to_signup(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".Button-sc-1dqy6lx-0.jjtmnk.sibxBMlr_oxWTfBrEz2G"))
            )
        finally:
            go_signup = self.driver.find_elements(
                By.CSS_SELECTOR, ".Button-sc-1dqy6lx-0.jjtmnk.sibxBMlr_oxWTfBrEz2G")
            if len(go_signup) != 0:
                go_signup[0].click()
                
        return
    
    
    def remove_descrections(self):

        policy_close_button = self.driver.find_elements(
            By.CSS_SELECTOR, ".onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon")
        if len(policy_close_button) != 0:
            policy_close_button[0].click()
            print("NOTE: REMOVED POLICY")

        try:
            cookies_button = self.driver.find_element(
                By.ID, "onetrust-accept-btn-handler")
        except:
            print('NOTE: No cookies there')
        else:
            cookies_button.click()
            print("REMOVE COOKIES")

        return

    def fill_displayed_name(self):
        display_name_field = self.driver.find_element(By.ID, "displayname")
        display_name_field.send_keys("your display name")
        return

    def fill_password(self):
        password = "yourPassword"
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        self.password = password
        return

    def fill_date_of_birth(self):
        day_field = self.driver.find_element(By.ID, "day")
        day_field.send_keys("01")

        year_field = self.driver.find_element(By.ID, "year")
        year_field.send_keys("1990")

        month_dropdown = Select(self.driver.find_element(By.ID, "month"))
        month_dropdown.select_by_index(2)
        return

    def fill_email_and_confrm(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
        finally:
            email_field = self.driver.find_element(By.ID, "email")
            email_field.send_keys(self.email)

        try:
            confirm_email_field = self.driver.find_element(By.ID, "confirm")
        except:
            print('NOTE: No confirm email there')
        else:
            confirm_email_field.send_keys(self.email)
        return

    def fill_gender(self):
        gender_radiobutton = self.driver.find_elements(By.CSS_SELECTOR, ".Indicator-sc-hjfusp-0.benotq"
                                                       )
        gender_radiobutton[0].click()

    def submit_form(self):
        # submit the form
        submit_button = self.driver.find_elements(
            By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0.dqLIWu.encore-bright-accent-set.SignupButton___StyledButtonPrimary-cjcq5h-1.jazsmO")
        submit_button[0].click()
        print("NOTE: FORM SUBMITED")
        return

    def cc_premium_activator(self):
        try:
            WebDriverWait(self.driver, 100).until(
                 EC.presence_of_element_located(
                     (By.CSS_SELECTOR, ".Type__TypeElement-sc-goli3j-0.bNyYSN.ellipsis-one-line.PDPsYDh4ntfQE3B4duUI"))
             ) 
        finally:
            go_premium = self.driver.find_elements(
                By.CSS_SELECTOR, ".Type__TypeElement-sc-goli3j-0.bNyYSN.ellipsis-one-line.PDPsYDh4ntfQE3B4duUI")
            if len(go_premium) != 0:
                go_premium[0].click()
                wid = self.driver.window_handles[1]
                #switch to active tab
                self.driver.switch_to().window(wid)
                try:
                    WebDriverWait(self.driver, 100).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, ".Button-sc-y0gtbx-0.iVrvaH.Upqw01TOXETOmR5Td7Dj"))
                    )
                finally:
                    go_to_plan_page = self.driver.find_elements(
                        By.CSS_SELECTOR, ".Button-sc-y0gtbx-0.iVrvaH.Upqw01TOXETOmR5Td7Dj")
                    if len(go_to_plan_page) != 0:
                        go_to_plan_page[0].click()
                        try:
                            WebDriverWait(self.driver, 100).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, ".Indicator-hjfusp-0.hJZAEs"))
                            )
                        finally:

                            go_to_cc_form = self.driver.find_elements(
                                By.CSS_SELECTOR, ".Indicator-hjfusp-0.hJZAEs")
                            if len(go_to_cc_form) > 1:
                                go_to_cc_form[1].click()
                            elif len(go_to_cc_form) == 1:
                                go_to_cc_form[0].click()

                            self.try_ccs()

            # driver.quit()
            print("NOTE: ACCOUNT IS CREATED")
        return

    def try_ccs(self):
        cc_file = C_Fichier(self.cc_file_name)
        regected_cc_file = C_Fichier(self.regected_cc_file_name)
        ccs = cc_file.Fichier_to_Liste()
        regected_ccs = regected_cc_file.Fichier_to_str()
        for cc in ccs:
            cc_splited = cc.split("|")
            print(cc_splited)
            if cc_splited[0] not in regected_ccs:
                credit_card = CC_Class(self.driver, cc_splited)
                credit_card.fill_cc_input()
                try:
                    WebDriverWait(self.driver, 100).until(
                        EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="loading-indicator"]'))
                    )
                finally:
                    try:
                        self.driver.find_element(
                            By.CSS_SELECTOR, "Wrapper-sc-62m9tu-0.jieDxt.encore-negative-set")
                    except:
                        print("NOTE: CC NOT ACCEPTED")
                        regected_cc_file.str_to_fichier(cc)
                    else:
                        self.export_account_data()
                        print("NOTE: ACCOUNT IS CREATED, CHECK THE FILE {}".format(
                            self.data_file))
                        return
            else:
                continue

    def export_data(self):
        return [self.email, self.password]

    def close_tab(self):
        self.driver.quit()

    def main_spotify(self):
        self.get_driver()
        self.get_Email_from_yopmail()
        self.remove_descrections()
        self.fill_email_and_confrm()
        self.fill_password()
        self.fill_displayed_name()
        self.fill_date_of_birth()
        self.fill_gender()
        self.submit_form()
        self.cc_premium_activator()
    pass



def main():
    sp = SpotifyGenerator()
    file = C_Fichier("data.txt")
    
    sp.get_driver()
    sp.get_Email_from_yopmail()
    sp.go_to_signup()
    sp.fill_email_and_confrm()
    sp.remove_descrections()
    sp.fill_password()
    sp.fill_displayed_name()
    sp.fill_date_of_birth()
    sp.fill_gender()
    sp.submit_form()
    sp.cc_premium_activator()
    L = sp.export_data()
    L.append(date.today())

    
    #file.creer_fichier_1()
    file.Liste_to_str_to_Fichier(L)
    
    
    
    
    return

main()