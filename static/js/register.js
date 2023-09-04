const username_field = document.getElementById("username-field");
const usernameFeedback = document.querySelector(
  ".error-username-feedback small"
);

const form = document.forms['reg-form']
console.log(form);

// submit btn
const submitBtn = document.querySelector(".submit-btn");

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
        console.log(data);
        // error? change the field to red
        if (data.error) {
          submitBtn.disabled = true;
          username_field.classList.add("warning");
          usernameFeedback.style.display = "block";
          usernameFeedback.textContent = `${data.error}`;
        } else {
          submitBtn.disabled = false;
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
          submitBtn.disabled = true;
          email_field.classList.add("warning");
          emailFeedback.style.display = "block";
          emailFeedback.textContent = `${data.error}`;
        } else {
          submitBtn.disabled = false;
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
    showIcon.textContent = "Hide";
  } else {
    showIcon.textContent = "Show";
    passwordInput.type = "password";
  }
});
