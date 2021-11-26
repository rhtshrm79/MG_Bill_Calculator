function loadXMLDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("result").innerHTML =
        this.responseText;
      }
    };
    var cmr = document.getElementById('cmr').value;
    var pmr = document.getElementById('pmr').value;
    xhttp.open("GET", "/bill-calculate/?cmr="+cmr+"&pmr="+pmr, true);
    xhttp.send();
  }