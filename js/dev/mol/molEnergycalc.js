var tabelaPeriodica = {
   'H':{'energia': 4.5},
   'He':{'energia': 24.6},
   'Li':{'energia': 5.4},
   'Be':{'energia': 9.3},
   'B':{'energia': 8.3},
   'C':{'energia': 7.5},
   'N':{'energia': 10.0},
   'O':{'energia': 12.0},
   'F':{'energia': 15.0},
   'Ne':{'energia': 21.6},
   'Na':{'energia': 5.1},
   'Mg':{'energia': 7.6},
   'Al':{'energia': 5.9},
   'Si':{'energia': 8.2},
   'P':{'energia': 10.5},
   'S':{'energia': 10.4},
   'Cl':{'energia': 12.0},
   'Ar':{'energia': 15.8},
   'K':{'energia': 4.3},
   'Ca':{'energia': 6.1},
   'Sc':{'energia': 6.6},
   'Ti':{'energia': 6.8},
   'V':{'energia' :6.7},
   'Cr':{'energia' :6.8},
   'Mn':{'energia' :7.4},
   'Fe':{'energia' :7.9},
   'Co':{'energia' :7.7},
   'Ni':{'energia' :7.6},
   'Cu':{'energia' :7.7},
   'Zn':{'energia' :9.4},
   'Ga':{'energia' :5.9},
   'Ge':{'energia' :7.9},
   'As':{'energia' :9.8},
   'Se':{'energia' :9.8},
   'Br':{'energia' :11.8},
   'Kr':{'energia' :14.0},
   'Rb':{'energia' :4.2},
   'Sr':{'energia' :5.0},
   'Y':{'energia' :6.2},
   'Zr':{'energia' :6.6},
   'Nb':{'energia' :6.8},
   'Mo':{'energia' :7.1},
   'Tc':{'energia' :7.3},
   'Ru':{'energia' :7.2},
   'Rh':{'energia' :7.5},
   'Pd':{'energia' :8.3},
   'Ag':{'energia' :7.6},
   'Cd':{'energia' :8.9},
   'In':{'energia' :5.8},
   'Sn':{'energia' :7.3},
   'Sb':{'energia' :8.6},
   'Te':{'energia' :9.0},
   'I':{'energia' :10.5},
   'Xe':{'energy':12},
   'Ga':{'energia': 5.9},
   'Ge':{'energia': 7.9},
   'As':{'energia': 9.8},
   'Se':{'energia': 9.8},
   'Br':{'energia': 11.8},
   'Kr':{'energia': 14.0},
   'Rb':{'energia': 4.2},
   'Sr':{'energia': 5.0},
   'Y':{'energia': 6.2},
   'Zr':{'energia': 6.6},
   'Nb':{'energia': 6.8},
   'Mo':{'energia': 7.1},
   'Tc':{'energia': 7.3},
   'Ru':{'energia': 7.2},
   'Rh':{'energia': 7.5},
   'Pd':{'energia': 8.3},
   'Ag':{'energia': 7.6},
   'Cd':{'energia': 8.9},
   'In':{'energia': 5.8},
   'Sn':{'energia': 7.3},
   'Sb':{'energia': 8.6},
   'Te':{'energia': 9.0},
   'I':{'energia': 10.5},
   'Xe':{'energia': 12.0},
   'Cs':{'energia': 3.9},
   'Ba':{'energia': 5.2},
   'La':{'energia': 5.7},
   'Ce':{'energia': 5.5},
   'Pr':{'energia': 5.5},
   'Nd':{'energia': 5.5},
   'Pm':{'energia': 5.6},
   'Sm':{'energia': 5.6},
   'Eu':{'energia': 5.7},
   'Gd':{'energia': 6.0},
   'Tb':{'energia': 5.9},
   'Dy':{'energia': 5.9},
   'Ho':{'energia': 6.0},
   'Er':{'energia': 6.1},
   'Tm':{'energia': 6.2},
   'Yb':{'energia': 6.2},
   'Lu':{'energia': 5.4},
   'Hf':{'energia': 6.8},
   'Ta':{'energia': 7.0},
   'W':{'energia': 7.5},
   'Re':{'energia': 7.6},
   'Os':{'energia': 8.0},
   'Ir':{'energia': 8.2},
   'Pt':{'energia': 8.9},
   'Au':{'energia': 9.2},
   'Hg':{'energia': 10.4},
   'Tl':{'energia': 6.1},
   'Pb':{'energia': 7.4},
   'Bi':{'energia': 7.3},
   'Th':{'energia': 6.1},
   'Pa':{'energia': 5.9},
   'U':{'energia': 6.2}
};

function calcularEnergiaMolecula() {
  var smiles = document.getElementById("smiles").value;
  var molecula = converterSMILESParaMolecula(smiles);
  var energiaMolecula = calcularEnergia(molecula);
  document.getElementById("outputMolEnergy").innerHTML = "A energia total da molécula é: " + energiaMolecula + " eV";
  
  // Get the existing button element by its ID
  var existingButton = document.getElementById("molEnergycaleV");
  
  // Attach an event listener to the button that calls navigator.clipboard.writeText()
  existingButton.addEventListener("click", function() {
    navigator.clipboard.writeText(energiaMolecula);
  });
}


    function converterSMILESParaMolecula(smiles) {
        var molecula = {};
        var i = 0;
        while (i < smiles.length) {
            var elemento = '';
            var quantidade = 1;
            if (smiles[i].toUpperCase() === smiles[i]) {
                elemento = smiles[i];
                i++;
                if (i < smiles.length && smiles[i].toLowerCase() === smiles[i]) {
                    elemento += smiles[i];
                    i++;
                }
            }
            if (i < smiles.length && !isNaN(parseInt(smiles[i]))) {
                quantidade = parseInt(smiles[i]);
                i++;
            }
            if (elemento in molecula) {
                molecula[elemento] += quantidade;
            } else {
                molecula[elemento] = quantidade;
            }
        }
        return molecula;
    }

    function calcularEnergia(molecula) {
        var energiaTotal = 0;
        for (var elemento in molecula) {
            if (molecula.hasOwnProperty(elemento)) {
                var quantidade = molecula[elemento];
                var energiaAtomo = tabelaPeriodica[elemento]['energia'];
                energiaTotal += energiaAtomo * quantidade;
            }
        }
        return energiaTotal;
    }
