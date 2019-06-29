
//THIS WILL ORIGINALLY POPULATE THE TABLE

// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the data from data.js
console.log(data);

//set variable tabledata and copy data so I dont change original data
var tableData = data;

//loop over data in data.js and add a new row for each point
tableData.forEach(function(sightings) {
  // console.log(sightings);
  var row = tbody.append("tr");
  Object.entries(sightings).forEach(function([key, value]) {
    // console.log(key, value);
    
    // Append a cell to the row for each value
    var cell = row.append("td");
    cell.text(value);
  });
})

//THIS WILL EXECUTE THE FUNCTION TO FILTER THE DATA

 //Sets variable to call the button from html
  var submit =d3.select("Button")
  
   //This will execute a function when the filter button is clicked
  function buttonfunction(){
    
    //stops page from refreshing and logs to console that button was pushed
    d3.event.preventDefault();
  console.log("Filter Button Clicked");

  //collect the text from the input text box
inputText = document.getElementById("datetime").value

//clears the table
  d3.selectAll("td").remove();

    //filters the data based on the input date and sets it to variable filtered data
    var filteredData = tableData.filter(sightingday => sightingday.datetime === inputText);
  
  //repopulates the data based on the filtered criteria

    filteredData.forEach(function(sightings) {
     
      var row = tbody.append("tr");
      Object.entries(sightings).forEach(function([key, value]) {
        
        // Append a cell to the row for each filtered value
        var cell = row.append("td");
        cell.text(value);
      });
    })
  }
  
  //execute function on click
  submit.on("click", buttonfunction);





 