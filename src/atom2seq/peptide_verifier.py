# import atom2seq


def verify_xyz(molecule):
    if len(molecule.atoms) < 10:
        return False
    else:
        h_counter = 0
        c_counter = 0
        o_counter = 0
        n_counter = 0
        for atom in molecule.atoms:
            if atom.symbol == "H":
                h_counter += 1
            elif atom.symbol == "C":
                c_counter += 1
            elif atom.symbol == "O":
                o_counter += 1
            elif atom.symbol == "N":
                n_counter += 1
            elif atom.symbol == "S":
                pass
            else:
                return False
        chon_counter = h_counter + c_counter + o_counter + n_counter
        if chon_counter < 4:
            return False
        else:
            return True
