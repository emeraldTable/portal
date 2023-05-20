function showContent(url) {
 var iframe = document.getElementById("content-iframe");
     iframe.src = url;
}

function mol1() {
	showContent('https://embed.molview.org/v1/?mode=balls&smiles=NCO(O)N');
  const files = [
    "./assets/docs/synthesis/molecules/molecules-procedural/desc/ArCmCuHMnOOsPaPtSeTmYb.html"
  ];
  const iframes = [
    document.getElementById("content-iframe")
  ];
  for (let i = 0; i < files.length; i++) {
    loaddesc(files[i], iframes[i]);
  }
}

function mol2() {
	showContent('https://embed.molview.org/v1/?mode=balls&smiles=[Pa-2][Se-][Mn][Pt+4][O-3][H+3][Cu][Yb][Cm+4][Tm-3][Os+][Ar+2]');
  const files = [
    "./assets/docs/synthesis/molecules/molecules-procedural/desc/ArCmCuHMnOOsPaPtSeTmYb.html"
  ];
  const iframes = [
    document.getElementById("content2-iframe")
  ];
  for (let i = 0; i < files.length; i++) {
    loaddesc(files[i], iframes[i]);
  }
}

function mol3() {
	showContent('https://embed.molview.org/v1/?mode=balls&smiles=[O-]O[N+][N-4][O-]O[O+][O-3][N-][N+][C-2][O+2]C[C-3]');
  const files = [
    "./assets/docs/synthesis/molecules/molecules-procedural/desc/C3H8N4O7.html"
  ];
  const iframes = [
    document.getElementById("content3-iframe")
  ];
  for (let i = 0; i < files.length; i++) {
    loaddesc(files[i], iframes[i]);
  }
}

function loaddesc(file, iframe) {
  Papa.parse(file, {
    download: true,
    header: true,
    complete: function(results) {
      const table = document.createElement("table");
      const headerRow = document.createElement("tr");
      for (const header of results.meta.fields) {
        const th = document.createElement("th");
        th.textContent = header;
        headerRow.appendChild(th);
      }
      table.appendChild(headerRow);
      for (const row of results.data) {
        const tr = document.createElement("tr");
        for (const field of results.meta.fields) {
          const td = document.createElement("td");
          td.textContent = row[field];
          tr.appendChild(td);
        }
        table.appendChild(tr);
      }
      iframe.contentDocument.body.innerHTML = "";
      iframe.contentDocument.body.appendChild(table);
    }
  });
}

// Security Cleaner

    // Retrieve all cookies
    var cookies = document.cookie.split(";");

    // Delete each cookie
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i];
      var eqPos = cookie.indexOf("=");
      var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
      document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
    }
    
    // Delete all items in localStorage
    localStorage.clear();
