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
