const username_field = document.getElementById("username-field");
const usernameFeedback = document.querySelector(".error-feedback small");
console.log(usernameFeedback);


// username validation
username_field.addEventListener("keyup", function (e) {
  e.preventDefault();
  const inputValue = e.target.value;
  console.log(inputValue);

  // reset the values
  username_field.classList.remove("warning");
  usernameFeedback.style.display = "none";

  // make an api call
  if (inputValue.length > 0) {
    fetch("/auth/username-validation/", {
      body: JSON.stringify({ username: inputValue }),
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        // error? change the field to red
        if (data.error) {
          username_field.classList.add("warning");
          usernameFeedback.style.display = "block";
          usernameFeedback.textContent = `${data.error}`;
        }
      });
  }
});


// Email validation