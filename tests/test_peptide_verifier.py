from atom2seq.classes import Atom, Mol
from atom2seq.peptide_verifier import verify_xyz

test_molecule = Mol(
    [Atom("H", (0, 0, 0)), Atom("O", (0, 0, 0)), Atom("H", (0, 0, 0))], []
)

assert not verify_xyz(test_molecule)
