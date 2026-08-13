

const handleShowHidePassword = () => {
	const eyeIcons = document.querySelectorAll(".eye-icon");
    if (!eyeIcons.length) return;
    eyeIcons.forEach((icon) => {
        const field = icon.previousElementSibling;
        const slash = icon.querySelector(".eye-slash");
        icon.addEventListener("click", () => {
            field.type = field.type === "password" ? "text" : "password";
            slash.classList.toggle("hidden");
        });
    });
}

// TODO: Display logout when user_avatar is clicked

// Init JS
handleShowHidePassword();
