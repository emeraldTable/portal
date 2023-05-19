    document.addEventListener('keydown', function(e) {
        // Block Ctrl+S shortcut
        if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
            e.preventDefault();
        }
    });

    document.addEventListener('keydown', function(e) {
        // Block Ctrl+A and Ctrl+W shortcuts
        if ((e.keyCode == 65 || e.keyCode == 87) && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
            e.preventDefault();
        }
    });

    document.addEventListener('contextmenu', function(e) {
        // Block ability to select all
        e.preventDefault();
    });

    document.addEventListener("mousedown", function(event) {
        if (event.button === 0 && !event.ctrlKey) {
        event.preventDefault();
    }
    });

    document.addEventListener('mousedown', function(event) {
        if (event.shiftKey) {
        event.preventDefault();
    }
    });

  // desativa a seleção de texto na página
  function disableSelection() {
    if (typeof document.onselectstart!="undefined") {
      document.onselectstart=new Function("return false");
    }
    else {
      document.onmousedown=new Function("return false");
      document.onmouseup=new Function("return true");
    }
  }

  // ativa a seleção de texto na página
  function enableSelection() {
    if (typeof document.onselectstart!="undefined") {
      document.onselectstart=new Function("return true");
    }
    else {
      document.onmousedown=null;
      document.onmouseup=null;
    }
  }

  // desativa a seleção de texto quando o mouse é arrastado
  function blockSelectAll() {
    disableSelection();
    document.addEventListener("mousemove", disableSelection);
  }

  // ativa a seleção de texto quando o mouse é solto
  function unblockSelectAll() {
    enableSelection();
    document.removeEventListener("mousemove", disableSelection);
  }

  // adiciona os listeners aos eventos de mouse
  document.addEventListener("mousedown", blockSelectAll);
  document.addEventListener("mouseup", unblockSelectAll);

////DEV ZONE
function protectBrowser() {
  // Disable right-click context menu
  document.addEventListener('contextmenu', event => event.preventDefault());

  // Disable text selection
  document.addEventListener('selectstart', event => event.preventDefault());

  // Disable drag and drop
  document.addEventListener('dragstart', event => event.preventDefault());

  // Disable the ability to copy and paste
  document.addEventListener('copy', event => event.preventDefault());
  document.addEventListener('cut', event => event.preventDefault());
  document.addEventListener('paste', event => event.preventDefault());

  // Disable the ability to open the developer console
  document.addEventListener('keydown', event => {
    if (event.keyCode === 123) {
      event.preventDefault();
    }
  });
  document.addEventListener('contextmenu', event => {
    if (event.target.nodeName === 'HTML') {
      event.preventDefault();
    }
  });
}

