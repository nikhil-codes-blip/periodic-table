# Import sleep function
from time import sleep

# Do in 'try' and except not to get error
try:
    # Print heading
    print("\n\t\t\t---  :Periodic Table: ---")
    print("\t\t\t =======================")
    print("\t\t\t\t\t\t\t\t---Created By Priyanshu Singh")
    # Global indentifiers used in program
    AtNo = ""
    atno = ""

    # define function to get data from user
    def get_input_at_no():
        global AtNo, atno
        atno = int(
            input("\n \t  Enter Atomic number of element..\n \t  ==================================\n\n\t>>>   "))
        print('')
        AtNo = atno
        sleep(5)


    # define function to get data from user


    def get_input_at_sym():
        global AtNo, atno
        symb = ['H', "He", 'Li', "Be", "B", "C", "N", "O", "F", 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
                'Ca', 'Sc', 'Ti', 'V',
                'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
                'Nb', 'Mo', 'Tc', 'Ru',
                'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
                'Sm', 'Eu', 'Gd', 'Tb',
                'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb',
                'Bi', 'Po', 'At', 'Rn',
                'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                'Rf', 'Ha', 'Unh', 'Ns',
                'Hs', 'Mt', 'Uun', 'Uuu', 'Uub', 'Uut', 'Uuq', 'Uup', 'UUh', 'Uus', "Uuo"]
        symbo = input("\n \t  Enter Atomic symbol of element..\n \t  =================================\n\n\t>>>   ")
        print('')
        if len(symbo) == 1:
            symbo = symbo.capitalize()
        elif len(symbo) == 2:
            symbo = symbo.__getitem__(0).capitalize() + symbo.__getitem__(1).lower()
        elif len(symbo) == 3:
            symbo = symbo.__getitem__(0).capitalize() + symbo.__getitem__(1).lower() + symbo.__getitem__(2).lower()

        AtNo = int(symb.index(symbo)) + 1
        atno = AtNo
        sleep(5)


    # define function for 3d electronic config


    def ele_con():
        global AtNo
        orb = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f',
               '6d', '7p']
        #--------------------------- EXCEPTIONAL CONFIGURATIONS ---------------------------#
        if AtNo == 24:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 5', '4s 1', sep=' , ')
        elif AtNo == 29:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 1', sep=' , ')
        elif AtNo == 41:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6', '4d 4', '5s 1', sep=' , ')
        elif AtNo == 42:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6',
                  '4d 5', '5s 1', sep=' , ')
        elif AtNo == 44:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6',
                  '4d 7', '5s 1', sep=' , ')
        elif AtNo == 45:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6',
                  '4d 8', '5s 1', sep=' , ')
        elif AtNo == 46:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6',
                  '4d 10', '5s 0', sep=' , ')
        elif AtNo == 47:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6',
                  '4d 10', '5s 1', sep=' , ')
        elif AtNo == 57:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6', '4d 10', '5s 2',
                  '5p 6',
                  '5d 1', '6s 2', sep=' , ')
        elif AtNo == 58:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6', '4d 10', '5s 2',
                  '5p 6',
                  '4f 1', '5d 1', '6s 2', sep=' , ')
        elif AtNo == 64:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6', '4d 10', '5s 2',
                  '5p 6',
                  '4f 7', '5d 1', '6s 2', sep=' , ')
        elif AtNo == 78:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6', '4d 10', '5s 2',
                  '5p 6',
                  '4f 14', '5d 9', '6s 1', sep=' , ')
        elif AtNo == 79:
            print(' 1s 2', '2s 2', '2p 6', '3s 2', '3p 6', '3d 10', '4s 2', '4p 6', '4d 10', '5s 2',
                  '5p 6',
                  '4f 14', '5d 10', '6s 1', sep=' , ')
        else:
            for i in orb:
                if i.__getitem__(1) == 's':
                    if AtNo <= 2:
                        print(i, AtNo)
                        break
                    else:
                        print(i, 2, end=' , ')
                        AtNo = AtNo - 2
                        if AtNo <= 0:
                            break

                elif i.__getitem__(1) == 'p':
                    if AtNo <= 6:
                        print(i, AtNo)
                        break
                    else:
                        print(i, 6, end=' , ')
                        AtNo = AtNo - 6
                        if AtNo <= 0:
                            break
                elif i.__getitem__(1) == 'd':
                    if AtNo <= 10:
                        print(i, AtNo)
                        break
                    else:
                        print(i, 10, end=' , ')
                        AtNo = AtNo - 10
                        if AtNo <= 0:
                            break
                elif i.__getitem__(1) == 'f':
                    if AtNo <= 14:
                        print(i, AtNo)
                        break
                    else:
                        print(i, 14, end=' , ')
                        AtNo = AtNo - 14
                        if AtNo <= 0:
                            break


    # define function for 2d electronic config


    def elecon():
        global AtNo
        if AtNo <= 2:
            if AtNo == 2:
                print("Noble gas Electrons per shell: ", AtNo)
            else:
                print("Electrons per shell: ", AtNo)
        elif 2 < AtNo <= 10:
            if AtNo == 10:
                print("Noble gas Electrons per shell:  2 ,", (AtNo - 2))
            else:
                print("Electrons per shell: 2 ,", (AtNo - 2))
        elif 10 < AtNo <= 18:
            if AtNo == 18:
                print("Noble gas Electrons per shell:  2 , 8 ,", (AtNo - 2 - 8))
            else:
                print("Electrons per shell: 2 , 8 ,", (AtNo - 2 - 8))
        elif 18 < AtNo <= 36:
            if AtNo == 36:
                print("Noble gas Electrons per shell:  2 , 8 , 18 ,", (AtNo - 2 - 8 - 18))
            elif 21 <= AtNo <= 30:
                print("Electrons per shell : Unavailable")
            elif AtNo == 19 or 20:
                print("Electrons per shell: 2 , 8 , 8 ,", (AtNo - 18))
            else:
                print("Electrons per shell : 2 , 8 , 18 ,", (AtNo - 2 - 18 - 8))
        elif 36 < AtNo <= 54:
            if AtNo == 54:
                print("Noble gas Electrons per shell:  2 , 8 , 18 , 18 ,", (AtNo - 2 - 8 - 18 - 18))
            elif 39 <= AtNo <= 48:
                print("Electrons per shell: Unavailable")
            elif AtNo == 37 or 38:
                print("Electrons per shell: 2 , 8 , 18 , 18 ,", (AtNo - 36))
            else:
                print("Electrons per shell: 2 , 8 , 18 , 18 ,", (AtNo - 2 - 8 - 18 - 18))
        elif 54 < AtNo <= 86:
            if AtNo == 86:
                print("Noble gas Electrons per shell:  2 , 8 , 18 , 32 , 18 ,", (AtNo - 2 - 8 - 18 - 32 - 18))
            elif 57 <= AtNo <= 80:
                print("Electrons per shell : Unavailable")
            elif AtNo == 55 or 56:
                print("Electrons per shell: 2 , 8 , 18 ,  32 , 18 ,", (AtNo - 54))

            else:
                print("Electrons per shell: 2 , 8 , 18 ,  32 , 18 ,", (AtNo - 2 - 8 - 18 - 32 - 18))

        elif AtNo > 87:
            print("Electrons per shell : Unavailable")

    #define function for metals or non metals

    def proper():
        global AtNo
        if AtNo <= 4:
             if AtNo == 1:
              print('non metal')
             elif AtNo == 2:
                 print('non metal')
             else:
                 print('metals')
        elif AtNo == 5:
            print('metalloids')

        elif 5 < AtNo <=20:
            if AtNo == 14:
                print('metalloids')
            elif 6 <= AtNo <= 10:
                print('non metals')
            elif 15 <= AtNo <= 18:
                print('non metals')
            else:
                print('metals')

        if 20 < AtNo <= 36:
            if  21 <= AtNo <= 31:
                print('metals')
            elif 34 <= AtNo <= 36:
                print('non metals')
            else:
                print('metalloids')

        if 36 < AtNo <= 54:
            if  37 <= AtNo <= 50:
                print('metals')
            elif 53 <= AtNo <= 54:
                print('non metals')
            else:
                print('metalloids')

        if 54 < AtNo <= 87:
            if 55 <= AtNo <= 84:
                print('metal')
            else:
                print('metalloids')



    # define function for symbols of element
 
    
    def symbol():
        global AtNo
        symb = ['H', "He", 'Li', "Be", "B", "C", "N", "O", "F", 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
                'Ca', 'Sc', 'Ti', 'V',
                'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
                'Nb', 'Mo', 'Tc', 'Ru',
                'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
                'Sm', 'Eu', 'Gd', 'Tb',
                'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb',
                'Bi', 'Po', 'At', 'Rn',
                'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                'Rf', 'Ha', 'Unh', 'Ns',
                'Hs', 'Mt', 'Uun', 'Uuu', 'Uub', 'Uut', 'Uuq', 'Uup', 'UUh', 'Uus', "Uuo"]
        print('\n Atomic Symbol :', symb.__getitem__(AtNo - 1), "\n\n Electronic Configurations : --")


    # define function for run all code


    def give_the_final_result():
        get_input = int(input("\n\t1. Get Electronic Configuration by Atomic No.\
        \n\n\t2. Get Electronic Configuration by Atomic Symbol.\n\n(1/2)>>>  "))
        if get_input == 1:
            get_input_at_no()
            if 0 >= AtNo > 118:
                print("Invalid Atomic No")

            else:

                elecon()
                proper()
                print()
                symbol()
                ele_con()
                print('\nAtomic No =', atno)
                sleep(2)
        elif get_input == 2:
            get_input_at_sym()
            elecon()
            proper()
            symbol()
            ele_con()
            print('\nAtomic No =', atno)
            sleep(2)
        else:
            sleep(2)
            print("\n Enter 1 or 2 not else..")

            give_the_final_result()


    def try_again_or_not(name):
        inn = input(f'\n Try {name} \n (y/n)>>>  ')
        if inn.lower() == 'y':
            give_the_final_result()
        elif inn.lower() == 'n':
            sleep(1)
        else:
            try_again_or_not('another')


    give_the_final_result()
    try_again_or_not('another')
except:
    print("Invalid Input")
    try_again_or_not('again')
    sleep(2)
