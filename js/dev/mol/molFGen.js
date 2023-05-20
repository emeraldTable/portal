function generateFissionMolecule() {
  var moleculeName = "FissionMolecule";
  var atoms = [];
  var bonds = [];

  var periodicTable = [
    { symbol: "U", minBonds: 1, maxBonds: 6 },
    { symbol: "Pu", minBonds: 1, maxBonds: 6 },
    { symbol: "Np", minBonds: 1, maxBonds: 6 },
    { symbol: "Am", minBonds: 1, maxBonds: 6 },
    { symbol: "Cm", minBonds: 1, maxBonds: 6 },
    { symbol: "Bk", minBonds: 1, maxBonds: 6 },
    { symbol: "Cf", minBonds: 1, maxBonds: 6 },
    { symbol: "Es", minBonds: 1, maxBonds: 6 },
    { symbol: "Fm", minBonds: 1, maxBonds: 6 },
    { symbol: "Md", minBonds: 1, maxBonds: 6 },
    { symbol: "No", minBonds: 1, maxBonds: 6 },
    { symbol: "Lr", minBonds: 1, maxBonds: 6 }
  ];

  for (var i = 0; i < 12; i++) {
    var x = i - 6;
    var y = 0;
    var z = 0;

    var element = periodicTable[i];
    var atomType = element.symbol;

    atoms.push([x, y, z, atomType]);
  }

  for (var i = 0; i < 11; i++) {
    var atom1 = i;
    var atom2 = i + 1;
    var bondType = 1;
    bonds.push([atom1, atom2, bondType]);
  }

  var molecule = "Molecule Name\n  " + moleculeName + " 0   0.00000     0.00000     0\n[Insert Comment Here]\n 12 11  0  0  0  0  0  0  0  0  1 V2000\n";

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
    var atom1 = bond[0] + 1;
    var atom2 = bond[1] + 1;
    var bondType = bond[2];
    molecule += " " + atom1 + " " + atom2 + " " + bondType + "  0  0  0  0\n";
  }
  
  		molecule += "M  END\n> <DATE>\n07-08-2009\n";

// Exibir o resultado no campo de texto
		var outputTextarea = document.getElementById("outputTextarea3");
		outputTextarea.value = molecule;
}

        function saveMolecule3() {
            var moleculeText = document.getElementById("outputTextarea3").value;
            var blob = new Blob([moleculeText], { type: 'text/plain' });
            var url = URL.createObjectURL(blob);
            var link = document.createElement('a');
            link.href = url;
            link.download = 'molecule.mol';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

	   function copymolecule3() {
			var outputElement = document.getElementById("outputTextarea3");
			outputElement.select();
			document.execCommand("copy");
	   }
