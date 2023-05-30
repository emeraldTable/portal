// Função para ler e exibir o conteúdo do arquivo readme.md em uma div
function exibirReadme() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      var readmeContent = this.responseText;
      var converter = new showdown.Converter();
      var html = converter.makeHtml(readmeContent);
      document.getElementById("divResize24").innerHTML = html;
      
      // Adicionar um evento de clique a todos os links do conteúdo
      var links = document.getElementsByTagName("a");
      for (var i = 0; i < links.length; i++) {
        var link = links[i];
        link.addEventListener("click", function(e) {
          e.preventDefault();
          var readmeFilePath = this.getAttribute("href");
          lerReadmeLocal(readmeFilePath);
        });
      }
    }
  };
  xhttp.open("GET", "README.md", true);
  xhttp.send();
}

// Função para ler e exibir o conteúdo de um arquivo readme.md local
function lerReadmeLocal(filePath) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      var readmeContent = this.responseText;
      var converter = new showdown.Converter();
      var html = converter.makeHtml(readmeContent);
      document.getElementById("divResize24").innerHTML = html;
    }
  };
  xhttp.open("GET", filePath, true);
  xhttp.send();
}
