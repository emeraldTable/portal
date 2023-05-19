function generateMolecule2() {
    var moleculeName = "CHEMDOOD" + String(Math.floor(Math.random() * 1000000000000)).padStart(11, '0');
    var atoms = [];
    var bonds = [];

    var periodicTable = [
        { symbol: "H", minBonds: 1, maxBonds: 1 },
        { symbol: "He", minBonds: 0, maxBonds: 0 },
        { symbol: "Li", minBonds: 1, maxBonds: 1 },
        { symbol: "Be", minBonds: 2, maxBonds: 2 },
        { symbol: "B", minBonds: 3, maxBonds: 3 },
        { symbol: "C", minBonds: 4, maxBonds: 4 },
        { symbol: "N", minBonds: 3, maxBonds: 5 },
        { symbol: "O", minBonds: 2, maxBonds: 2 },
        { symbol: "F", minBonds: 1, maxBonds: 1 },
        { symbol: "Ne", minBonds: 0, maxBonds: 0 },
        { symbol: "Na", minBonds: 1, maxBonds: 1 },
        { symbol: "Mg", minBonds: 2, maxBonds: 2 },
        { symbol: "Al", minBonds: 3, maxBonds: 3 },
        { symbol: "Si", minBonds: 4, maxBonds: 4 },
        { symbol: "P", minBonds: 3, maxBonds: 5 },
        { symbol: "S", minBonds: 2, maxBonds: 6 },
        { symbol: "Cl", minBonds: 1, maxBonds: 1 },
        { symbol: "Ar", minBonds: 0, maxBonds: 0 },
        { symbol: "K", minBonds: 1, maxBonds: 1 },
        { symbol: "Ca", minBonds: 2, maxBonds: 2 },
        { symbol: "Sc", minBonds: 1, maxBonds: 3 },
        { symbol: "Ti", minBonds: 1, maxBonds: 4 },
        { symbol: "V", minBonds: 1, maxBonds: 5 },
        { symbol: "Cr", minBonds: 1, maxBonds: 6 },
        { symbol: "Mn", minBonds: 1, maxBonds: 7 },
        { symbol: "Fe", minBonds: 1, maxBonds: 8 },
        { symbol: "Co", minBonds: 1, maxBonds: 9 },
        { symbol: "Ni", minBonds: 1, maxBonds: 10 },
        { symbol: "Cu", minBonds: 1, maxBonds: 11 },
        { symbol: "Zn", minBonds: 2, maxBonds: 12 },
        { symbol: "Ga", minBonds: 3, maxBonds: 13 },
        { symbol: "Ge", minBonds: 4, maxBonds: 14 },
        { symbol: "As", minBonds: 3, maxBonds: 15 },
        { symbol: "Se", minBonds: 2, maxBonds: 16 },
        { symbol: "Br", minBonds: 1, maxBonds: 1 },
        { symbol: "Kr", minBonds: 0, maxBonds: 0 },
        { symbol: "Rb", minBonds: 1, maxBonds: 1 },
        { symbol: "Sr", minBonds: 2, maxBonds: 2 },
        { symbol: "Y", minBonds: 1, maxBonds: 3 },
        { symbol: "Zr", minBonds: 1, maxBonds: 4 },
        { symbol: "Nb", minBonds: 1, maxBonds: 5 },
        { symbol: "Mo", minBonds: 1, maxBonds: 6 },
        { symbol: "Tc", minBonds: 1, maxBonds: 7 },
        { symbol: "Ru", minBonds: 1, maxBonds: 8 },
        { symbol: "Rh", minBonds: 1, maxBonds: 9 },
        { symbol: "Pd", minBonds: 1, maxBonds: 10 },
        { symbol: "Ag", minBonds: 1, maxBonds: 11 },
        { symbol: "Cd", minBonds: 2, maxBonds: 12 },
        { symbol: "In", minBonds: 3, maxBonds: 13 },
        { symbol: "Sn", minBonds: 4, maxBonds: 14 },
        { symbol: "Sb", minBonds: 3, maxBonds: 15 },
        { symbol: "Te", minBonds: 2, maxBonds: 16 },
        { symbol: "I", minBonds: 1, maxBonds: 1 },
        { symbol: "Xe", minBonds: 0, maxBonds: 0 },
        { symbol: "Cs", minBonds: 1, maxBonds: 1 },
        { symbol: "Ba", minBonds: 2, maxBonds: 2 },
        { symbol: "La", minBonds: 1, maxBonds: 3 },
        { symbol: "Ce", minBonds: 1, maxBonds: 4 },
        { symbol: "Pr", minBonds: 1, maxBonds: 5 },
        { symbol: "Nd", minBonds: 1, maxBonds: 6 },
        { symbol: "Pm", minBonds: 1, maxBonds: 7 },
        { symbol: "Sm", minBonds: 1, maxBonds: 8 },
        { symbol: "Eu", minBonds: 1, maxBonds: 9 },
        { symbol: "Gd", minBonds: 1, maxBonds: 10 },
        { symbol: "Tb", minBonds: 1, maxBonds: 11 },
        { symbol: "Dy", minBonds: 1, maxBonds: 12 },
        { symbol: "Ho", minBonds: 1, maxBonds: 13 },
        { symbol: "Er", minBonds: 1, maxBonds: 14 },
        { symbol: "Tm", minBonds: 1, maxBonds: 15 },
        { symbol: "Yb", minBonds: 1, maxBonds: 16 },
        { symbol: "Hf", minBonds: 1, maxBonds: 4 },
        { symbol: "Ta", minBonds: 1, maxBonds: 5 },
        { symbol: "W", minBonds: 1, maxBonds: 6 },
        { symbol: "Re", minBonds: 1, maxBonds: 7 },
        { symbol: "Os", minBonds: 1, maxBonds: 8 },
        { symbol: "Ir", minBonds: 1, maxBonds: 9 },
        { symbol: "Pt", minBonds: 1, maxBonds: 10 },
        { symbol: "Au", minBonds: 1, maxBonds: 11 },
        { symbol: "Hg", minBonds: 1, maxBonds: 12 },
        { symbol: "Tl", minBonds: 1, maxBonds: 13 },
        { symbol: "Pb", minBonds: 2, maxBonds: 14 },
        { symbol: "Bi", minBonds: 3, maxBonds: 15 },
        { symbol: "Po", minBonds: 2, maxBonds: 16 },
        { symbol: "At", minBonds: 1, maxBonds: 1 },
        { symbol: "Rn", minBonds: 0, maxBonds: 0 },
        { symbol: "Fr", minBonds: 1, maxBonds: 1 },
        { symbol: "Ra", minBonds: 2, maxBonds: 2 },
        { symbol: "Ac", minBonds: 1, maxBonds: 3 },
        { symbol: "Th", minBonds: 1, maxBonds: 4 },
        { symbol: "Pa", minBonds: 1, maxBonds: 5 },
        { symbol: "U", minBonds: 1, maxBonds: 6 },
        { symbol: "Np", minBonds: 1, maxBonds: 7 },
        { symbol: "Pu", minBonds: 1, maxBonds: 8 },
        { symbol: "Am", minBonds: 1, maxBonds: 9 },
        { symbol: "Cm", minBonds: 1, maxBonds: 10 },
        { symbol: "Bk", minBonds: 1, maxBonds: 11 },
        { symbol: "Cf", minBonds: 1, maxBonds: 12 },
        { symbol: "Es", minBonds: 1, maxBonds: 13 },
        { symbol: "Fm", minBonds: 1, maxBonds: 14 },
        { symbol: "Md", minBonds: 1, maxBonds: 15 },
        { symbol: "No", minBonds: 1, maxBonds: 16 },
        { symbol: "Lr", minBonds: 1, maxBonds: 17 },
        { symbol: "Rf", minBonds: 1, maxBonds: 4 },
        { symbol: "Db", minBonds: 1, maxBonds: 5 },
        { symbol: "Sg", minBonds: 1, maxBonds: 6 },
        { symbol: "Bh", minBonds: 1, maxBonds: 7 },
        { symbol: "Hs", minBonds: 1, maxBonds: 8 },
        { symbol: "Mt", minBonds: 1, maxBonds: 9 },
        { symbol: "Ds", minBonds: 1, maxBonds: 10 },
        { symbol: "Rg", minBonds: 1, maxBonds: 11 },
        { symbol: "Cn", minBonds: 2, maxBonds: 12 },
        { symbol: "Nh", minBonds: 3, maxBonds: 13 },
        { symbol: "Fl", minBonds: 2, maxBonds: 14 },
        { symbol: "Mc", minBonds: 1, maxBonds: 15 },
        { symbol: "Lv", minBonds: 2, maxBonds: 16 },
        { symbol: "Ts", minBonds: 1, maxBonds: 17 },
        { symbol: "Og", minBonds: 0, maxBonds: 18 }
    ];

    for (var i = 0; i < 14; i++) {
        var x = Math.round(Math.random() * 4 - 2, 4);
        var y = Math.round(Math.random() * 4 - 2, 4);
        var z = Math.round(Math.random() * 4 - 2, 4);

        // Randomly select an element from the periodic table
        var element = periodicTable[Math.floor(Math.random() * periodicTable.length)];
        var atomType = element.symbol;

        atoms.push([x, y, z, atomType]);
    }

    for (var i = 1; i <= 14; i++) {
        var numBonds = Math.floor(Math.random() * 4);
        var connectedAtoms = [];

        while (connectedAtoms.length < numBonds) {
            var atom = Math.floor(Math.random() * 14 + 1);
            if (connectedAtoms.indexOf(atom) === -1 && atom !== i) {
                connectedAtoms.push(atom);
                var bondType = Math.random() < 0.5 ? 1 : 2;
                var bond = [i, atom, bondType];
                if (!bonds.find(function(existingBond) {
                    return existingBond[0] === bond[0] && existingBond[1] === bond[1] && existingBond[2] === bond[2];
                })) {
                    bonds.push(bond);
                }
            }
        }
    }

    var molecule = "Molecule Name\n  " + moleculeName + " 0   0.00000     0.00000     0\n[Insert Comment Here]\n 14 15  0  0  0  0  0  0  0  0  1 V2000\n";

    for (var i = 0; i < atoms.length; i++) {
        var atom = atoms[i];
        var x = atom[0];
        var y = atom[1];
        var z = atom[2];
        var atomType = atom[3];
        molecule += "   " + x.toFixed(4) + "    " + y.toFixed(4) + "    " + z.toFixed(4) + "   " + atomType + " 0  0  0  1  0  0  0  0  0  0  0  0\n";
    }

	for (var i = 0; i < bonds.length; i++) {
		var bond = bonds[i];
		var atom1 = bond[0];
		var atom2 = bond[1];
		var bondType = bond[2];
		molecule += " " + atom1 + " " + atom2 + " " + bondType + "  0  0  0  0\n";
	}

		molecule += "M  END\n> <DATE>\n07-08-2009\n";

// Exibir o resultado no campo de texto
		var outputTextarea = document.getElementById("outputTextarea2");
		outputTextarea.value = molecule;
}
        
        function saveMolecule2() {
            var moleculeText = document.getElementById("outputTextarea2").value;
            var blob = new Blob([moleculeText], { type: 'text/plain' });
            var url = URL.createObjectURL(blob);
            var link = document.createElement('a');
            link.href = url;
            link.download = 'molecule.mol';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

	   function copymolecule2() {
			var outputElement = document.getElementById("outputTextarea2");
			outputElement.select();
			document.execCommand("copy");
	   }
