const searchInput = document.querySelector("#searchInput");
const currenTable = document.querySelector(".table-show");
const outputTable = document.querySelector(".table-output");
const expensiveDiv = document.querySelector(".expenses");
const paginator = document.querySelector(".paginator-class-wrapper");
// const paginator2 = document.querySelector(".paginator-class");
const tBody = document.querySelector(".table-body");

outputTable.style.display = "none";

searchInput.addEventListener("keyup", function (e) {
  inputValues = e.target.value;

  if (inputValues.trim().length > 0) {
    paginator.style.display = "none";
    tBody.innerHTML = "";
    fetch("/search-expenses/", {
      body: JSON.stringify({ searchText: inputValues }),
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        currenTable.style.display = "none";
        outputTable.style.display = "block";
        if (data.length === 0) {
          outputTable.innerHTML = "<h1>No expenses matches your search</h1>";
          paginator.style.display = "none";
        } else {
          data.forEach((item) => {
            tBody.innerHTML += `
            <tr>
            <td>${item.amount}</td>
            <td>${item.category}</td>
            <td>${item.description}</td>
            <td>${item.date}</td>
            </tr>
          `;
          });
        }
      });
  } else {
    outputTable.style.display = "none";
    currenTable.style.display = "block";
    paginator.style.display = "flex";
  }
});
