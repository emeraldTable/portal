function convertToBase64() {
  var fileInput = document.getElementById("imageInput");
  var file = fileInput.files[0];
  var reader = new FileReader();

  reader.onloadend = function () {
    var base64String = reader.result;
    document.getElementById("base64Output").value = base64String;
  };

  reader.readAsDataURL(file);
}

function copyToClipboard() {
  var outputElement = document.getElementById("base64Output");
  outputElement.select();
  document.execCommand("copy");
}

//  Molecules Generator
        function generateMolecule() {
            var moleculeName = "CHEMDOOD" + String(Math.floor(Math.random() * 1000000000000)).padStart(11, '0');
            var atoms = [];
            var bonds = [];

            for (var i = 0; i < 14; i++) {
                var x = Math.round(Math.random() * 4 - 2, 4);
                var y = Math.round(Math.random() * 4 - 2, 4);
                var z = Math.round(Math.random() * 4 - 2, 4);
                var atomType = Math.random() < 0.33 ? "O" : Math.random() < 0.66 ? "C" : "N";
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
            //console.log(molecule);
            // Exibir o resultado no campo de texto
            var outputTextarea = document.getElementById("outputTextarea");
            outputTextarea.value = molecule; 
            
        }
        
        function saveMolecule() {
            var moleculeText = document.getElementById("outputTextarea").value;
            var blob = new Blob([moleculeText], { type: 'text/plain' });
            var url = URL.createObjectURL(blob);
            var link = document.createElement('a');
            link.href = url;
            link.download = 'molecule.mol';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

	   function copymolecule() {
			var outputElement = document.getElementById("outputTextarea");
			outputElement.select();
			document.execCommand("copy");
	   }
	   
	   
// Molecule Research
var iframe = null;

function toggleCrossSite() {
  var targetDiv = document.getElementById('divResize6');
  if (iframe) {
    iframe.parentNode.removeChild(iframe);
    iframe = null;
    //location.reload();
  } else {
    iframe = document.createElement('iframe');
    iframe.src = 'https://anonchatgpt.com/';
    iframe.style.width = '100%';
	iframe.style.height = '95%';
    targetDiv.appendChild(iframe);
  }
} 
// INPUT TO CSV
    function createCSV() {
      // Get form data
      const formulax = document.getElementById("formula").value;
      const molecularWeight = document.getElementById("molecular-weight").value;
      const hydrogenBondDonors = document.getElementById("hydrogen-bond-donors").value;
      const hydrogenBondAcceptors = document.getElementById("hydrogen-bond-acceptors").value;
      const percentComposition = document.getElementById("percent-composition").value;
      const canonicalSmiles = document.getElementById("canonical-smiles").value;
      const isomericSmiles = document.getElementById("isomeric-smiles").value;
      const inchikey = document.getElementById("inchikey").value;
      const inchi = document.getElementById("inchi").value;

      // Create CSV content
      const csvContent = `Formula,${formulax},,\n`
        + `Molecular weight,${molecularWeight},,\n`
        + `Hydrogen bond donors,${hydrogenBondDonors},,\n`
        + `Hydrogen bond acceptors,${hydrogenBondAcceptors},,\n`
        + `Percent composition,,\n${percentComposition},,\n`
        + `Canonical SMILES,${canonicalSmiles},,\n`
        + `Isomeric SMILES,${isomericSmiles},,\n`
        + `InChIKey,${inchikey},,\n`
        + `InChI,"${inchi}",,\n`;

      // Create Blob object
      const blob = new Blob([csvContent], {type: "text/csv;charset=utf-8;"});

      // Save file using FileSaver.js library
      saveAs(blob, "data.csv");
    }

// CSV TO HTML
  const csvFileInput = document.getElementById('csv-file');
    const tableContainer = document.getElementById('table-container');

    csvFileInput.addEventListener('change', (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        const csvData = reader.result;
        const parsedData = Papa.parse(csvData).data;
        const tableHtml = generateTableHtml(parsedData);
        tableContainer.innerHTML = tableHtml;
      };

      reader.readAsText(file);
    });

const saveButton = document.getElementById('save-button');
saveButton.addEventListener('click', () => {
  const htmlData = tableContainer.innerHTML;
  const blob = new Blob([htmlData], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'table.html';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
});

    function generateTableHtml(data) {
      let html = '<table>';
      html += '<thead><tr>';
      for (const header of data[0]) {
        html += `<th>${header}</th>`;
      }
      html += '</tr></thead>';
      html += '<tbody>';
      for (let i = 1; i < data.length; i++) {
        html += '<tr>';
        for (const value of data[i]) {
          html += `<td>${value}</td>`;
        }
        html += '</tr>';
      }
      html += '</tbody></table>';
      return html;
    }

// Function CopyVAR
function copyToClipboard(output) {
  const el = document.createElement('textarea');
  el.value = output;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
}

// STYLE EDITOR
const textarea = document.getElementById("outputTextarea");
textarea.style.backgroundColor = "black";
textarea.style.opacity = "0.5";
textarea.value = "";

// ViewMOL
        function generateURL() {
            var smilesInput = document.getElementById("vsmiles").value;
			const baseUrl = "https://embed.molview.org/v1/?mode=balls&smiles=";
			const smiles = document.getElementById("vsmiles").value.trim();
			const url = baseUrl + smiles;
			showMOL(url);
        }

        function showMOL(url) {
				var targetDiv = document.getElementById('divResize11');
					if (iframe) {
						iframe.parentNode.removeChild(iframe);
						iframe = null;
						//location.reload();
					} else {
						iframe = document.createElement('iframe');
						iframe.src = url;
						iframe.style.width = '100%';
						iframe.style.height = '95%';
						targetDiv.appendChild(iframe);
					}
		}
		
		function offMOL() {
				var targetDiv = document.getElementById('divResize11');
				var url = url
					if (iframe) {
						iframe.parentNode.removeChild(iframe);
						iframe = null;
						//location.reload();
					} else {
						iframe = document.createElement('iframe');
						iframe.src = url;
						iframe.style.width = '100%';
						iframe.style.height = '95%';
						targetDiv.appendChild(iframe);
					}
		}
//function vmol1() {
//	showContent('https://embed.molview.org/v1/?mode=balls&smiles=NCO(O)N');
//}
