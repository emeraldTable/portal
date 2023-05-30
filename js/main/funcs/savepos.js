    // Function to save the position of elements with a specific ID into a JSON file
        function savePositionsToJson() {
            var positions = {};

            // Define the IDs of the elements whose positions you want to save
            var elementIds = ["divResize1", "divResize2", "divResize3", "divResize4", "divResize5", "divResize6", "divResize7", "divResize8", "divResize9", "divResize10", "divResize11", "divResize12", "divResize13", "divResize14", "divResize15", "divResize16", "divResize17", "divResize18", "divResize19", "divResize20", "divResize21", "divResize22", "divResize23", "divResize24", "divResize25", "divResize26", "divResize27", "divResize27", "divResize29", "divResize30", "divResize31", "divResize32", "divResize33", "divResize34", "divResize35", "divResize36", "divResize37", "divResize38", "divResize39", "divResize40", "divResize41", "divResize42", "divResize43", "divResize44", "divResize45", "divResize46", "divResize47", "divResize48", "divResize49", "divResize50", "divResize51"];

 elementIds.forEach(function(id) {
    var element = document.getElementById(id);
    if (element) {
      var position = {
        left: element.style.left,
        top: element.style.top,
        height: element.style.height,
        width: element.style.width
      };
      positions[id] = position;
    } else {
      console.error("Element with id " + id + " not found.");
    }
  });

  var json = JSON.stringify(positions);
  var blob = new Blob([json], { type: 'application/json' });

  var downloadLink = document.createElement('a');
  downloadLink.href = URL.createObjectURL(blob);
  downloadLink.download = 'positions.json';
  downloadLink.click();
}

        // Function to handle the file upload
        function handleFileUpload(event) {
            var file = event.target.files[0];
            var reader = new FileReader();

            reader.onload = function(e) {
                var json = e.target.result;
                importPositionsFromJson(json);
            };

            reader.readAsText(file);
        }

        // Function to import position values from JSON and update HTML elements
        function importPositionsFromJson(json) {
            var positions = JSON.parse(json);

            for (var id in positions) {
                if (positions.hasOwnProperty(id)) {
                    var element = document.getElementById(id);
                    var position = positions[id];
                    element.style.left = position.left;
                    element.style.top = position.top;
                    element.style.height = position.height;
                    element.style.width = position.width;
                }
            }
        }

        var savedJson = '{}';
        importPositionsFromJson(savedJson);
