const searchInput = document.querySelector("#searchInput");
const currenTable = document.querySelector(".table-show");
const outputTable = document.querySelector(".table-output");
const expensiveDiv = document.querySelector(".expenses");
const paginator = document.querySelector(".Page-navigation");
const paginator2 = document.querySelector(".paginator-class");

outputTable.style.display = "none";

searchInput.addEventListener("keyup", function (e) {
  inputValues = e.target.value;

  if (inputValues.trim().length > 0) {
    fetch("/search-expenses/", {
      body: JSON.stringify({ searchText: inputValues }),
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        currenTable.style.display = "none";
        outputTable.style.display = "block";
        if (data.length <= 0) {
          outputTable.innerHTML = "<h1>No expenses matches your search</h1>";
          paginator.style.display = "none";
          paginator2.style.display = "none";
        } else {
          paginator.style.display = "block";
          paginator2.style.display = "block";
        }
      });
  } else {
    currenTable.style.display = "block";
    outputTable.style.display = "none";
  }
});
