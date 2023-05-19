function showContent(url) {
 var iframe = document.getElementById("content-iframe");
     iframe.src = url;
}

//function showContent2(url) {
// var iframe = document.getElementById("content2-iframe");
//     iframe.src = url;
//}

function mol1() {
	showContent('https://embed.molview.org/v1/?mode=balls&smiles=NCO(O)N');
	loaddesc();
	//showContent2('https://embed.molview.org/v1/?mode=balls&smiles=NCO(O)N');
	
}

function loaddesc() {
    // Load CSV file
    Papa.parse("https://raw.githubusercontent.com/c2V2ZW4K/nukeportal/main/assets/docs/synthesis/molecules/molecules-procedural/csv/data.csv", {
      download: true,
      header: true,
      complete: function(results) {
        // Convert results to HTML table
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

        // Display HTML table inside iframe
        const iframe = document.getElementById("content2-iframe");
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        doc.body.innerHTML = "";
        doc.body.appendChild(table);
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
