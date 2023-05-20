function gerarHEsmiles() {
        var simbolosAtomos = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl'];
        var comprimentoMolecula = Math.floor(Math.random() * (15 - 5 + 1)) + 5;
        var smiles = '';
        for (var i = 0; i < comprimentoMolecula; i++) {
            var simbolo = simbolosAtomos[Math.floor(Math.random() * simbolosAtomos.length)];
            smiles += simbolo;
        }

        document.getElementById("outputTextarea3").innerHTML = smiles;
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

function copyOutput3() {
  const output = document.getElementById("outputTextarea3").textContent;
  navigator.clipboard.writeText(output);
}

function gerarHEsmiles() {
        var simbolosAtomos = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl'];
        var comprimentoMolecula = Math.floor(Math.random() * (15 - 5 + 1)) + 5;
        var smiles = '';
        for (var i = 0; i < comprimentoMolecula; i++) {
            var simbolo = simbolosAtomos[Math.floor(Math.random() * simbolosAtomos.length)];
            smiles += simbolo;
        }

        document.getElementById("outputTextarea3").innerHTML = smiles;
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

function copyOutput3() {
  const output = document.getElementById("outputTextarea3").textContent;
  navigator.clipboard.writeText(output);
}
