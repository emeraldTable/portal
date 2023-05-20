function showContent3(url) {
 var iframe = document.getElementById("content3-iframe");
     iframe.src = url;
}
function ChemicalGroupBlock() {
	showContent3('./assets/docs/utils/ptables/ptables_ChemicalGroupBlock.png');
}

function mol2() {
	showContent('https://embed.molview.org/v1/?mode=balls&smiles=[Pa-2][Se-][Mn][Pt+4][O-3][H+3][Cu][Yb][Cm+4][Tm-3][Os+][Ar+2]');
}

function mol3() {
	showContent('https://embed.molview.org/v1/?mode=balls&smiles=[O-]O[N+][N-4][O-]O[O+][O-3][N-][N+][C-2][O+2]C[C-3]');
}
localStorage.clear();
