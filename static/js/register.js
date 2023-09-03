const username_field = document.getElementById("username-field");
const usernameFeedback = document.querySelector(
  ".error-username-feedback small"
);

// username validation
username_field.addEventListener("keyup", function (e) {
  e.preventDefault();
  const inputValue = e.target.value;

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
const email_field = document.getElementById("email-field");
const emailFeedback = document.querySelector(".error-email-feedback small");

email_field.addEventListener("keyup", function (e) {
  const emailValue = e.target.value;

  // reset the email field
  email_field.classList.remove("warning");
  emailFeedback.style.display = "none";

  if (emailValue.length > 0) {
    fetch("/auth/email-validation/", {
      body: JSON.stringify({ email: emailValue }),
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.error) {
          email_field.classList.add("warning");
          emailFeedback.style.display = "block";
          emailFeedback.textContent = `${data.error}`;
        }
      });
  }
});

// password toggle fucntionality
const showIcon = document.querySelector(".eye-icon small");
const passwordInput = document.querySelector("#password-field");
const toggleIconclose = document.querySelector(".eye-icon .fa-eye-slash");

showIcon.addEventListener("click", () => {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showIcon.textContent = 'Hide'
  } else {
    showIcon.textContent = 'Show'
    passwordInput.type = "password";
  }
});
