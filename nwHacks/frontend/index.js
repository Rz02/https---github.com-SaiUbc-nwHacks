var searchButton = document.getElementById("go-btn");
var searchBar = document.getElementById("input-element");

searchButton.addEventListener("click", search);
    searchBar.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            search();
        }
    });

    function search() {
        var busStopNo = searchBar.value;
        if(isNaN(busStopNo)){
            alert("Please Enter A Valid Bus Stop No.");
        } else {
            console.log(busStopNo);
        }
    }