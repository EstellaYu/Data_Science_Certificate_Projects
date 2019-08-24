// from data.js
var tableData = data;

// find different element
var tbody = d3.select("#ufo-table > tbody");
var button = d3.select("#filter-btn");
var button_reset = d3.select("#reset-btn")
var input_dt = d3.select("#datetime");
var input_ct = d3.select("#country");
var input_st = d3.select("#state");
var input_city = d3.select("#city");
var input_shape = d3.select("#shape");

// defalt: show all data
showData(tableData);

// when filter button is clicked
button.on("click", handelFind);
button_reset.on("click", handelReset);

// DROPDOWN OPTIONS
// dates
dates = {}
tableData.forEach(datum => {
    var date = datum.datetime;
    if (date in dates) dates[date] += 1;
    else dates[date] = 1;
})
// country
countries = {}
tableData.forEach(datum => {
    var ct = datum.country;
    if (ct in countries) countries[ct] += 1;
    else countries[ct] = 1;
})
// states
states = {}
tableData.forEach(datum => {
    var st = datum.state;
    if (st in states) states[st] += 1;
    else states[st] = 1;
})
// cities
cities = {}
tableData.forEach(datum => {
    var city = datum.city;
    if (city in cities) cities[city] += 1;
    else cities[city] = 1;
})

//-----------------------------------------------
//-------------FUNCTIONS-------------------------
//-----------------------------------------------

// function that append result from list to table 
function showData(dataList){
    dataList.forEach((datum) =>{
        var row = tbody.append("tr");
        Object.entries(datum).forEach(([key, val]) => {
            row.append("td").text(val);
        })
    })
}

// function that filter list based on date, 
// and show filtered list to table
function handelFind(){
    var date_input = input_dt.property("value");

    filtered = tableData.filter(filterDate).filter(filterCountry).filter(filterState).filter(filterCity).filter(filterShape);
    tbody.text("")
    showData(filtered);
}

// function that reset the table to all data
function handelReset(){
    tbody.text("");
    d3.selectAll(".form-control").property("value", "");
    showData(tableData);
}

// filter functions
function filterDate(table){
    text = input_dt.property("value");
    if ( text == "") return table;  
    else return table.datetime == text;
}
function filterCountry(table){
    text = input_ct.property("value");
    if ( text == "") return table; 
    else return table.country == text;
}
function filterState(table){
    text = input_st.property("value");
    if ( text == "") return table; 
    else return table.state == text;
}
function filterCity(table){
    text = input_city.property("value");
    if ( text == "") return table; 
    else return table.city == text;
}
function filterShape(table){
    text = input_shape.property("value");
    if ( text == "") return table; 
    else return table.shape == text;
}