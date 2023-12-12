// breeds.js
function searchFunction() {
  // Get the input field and its value
  var input = document.getElementById("searchBar");
  var filter = input.value;

  // Make an AJAX call to your search route
  fetch("/dog/breeds/search?q=" + filter)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Clear the breed list container
      var container = document.getElementById("breedList");
      container.innerHTML = "";

      // Loop through the search results and add them to the breed list container
      for (var i = 0; i < data.length; i++) {
        var breed = data[i];

        var breedLink = document.createElement("a");
        breedLink.href = "/dog/breeds/" + breed.id;
        breedLink.className = "breed-link";

        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";

        var breedName = document.createElement("p");
        breedName.className = "breed-name";
        breedName.textContent = breed.name;

        // Optionally, display additional information like breed origin
        var breedOrigin = document.createElement("p");
        breedOrigin.textContent = breed.origin;

        gridItem.appendChild(breedName);
        // Optionally, append breed origin to grid item
        gridItem.appendChild(breedOrigin);
        breedLink.appendChild(gridItem);
        container.appendChild(breedLink);
      }
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
}
