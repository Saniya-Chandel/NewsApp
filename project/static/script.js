function updateInputName(){
    var filterValue = document.getElementById("filterx").value;
   


    if(filterValue == "publishedAt"){
     document.getElementById("calendarInput").setAttribute('name',filterValue)
      document.getElementById("searchInput").style.display = "none";
      document.getElementById("calendarInput").style.display = "block";

    }
    else{
      document.getElementById("searchInput").setAttribute('name',filterValue)
      document.getElementById("searchInput").style.display = "block";
      document.getElementById("calendarInput").style.display = "none";
    }
  }
  