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
};

const handleToggleAvatarDropdown = () => {
    const userAvatar = document.getElementById("user-avatar");
    if (!userAvatar) return;
    userAvatar.addEventListener("click", () => {
        const avatarDropdown = document.getElementById("avatar-dropdown");
        avatarDropdown.classList.toggle("hidden");
    });
};

const handleLogout = () => {
    const logoutBtn = document.getElementById("logout-btn");
    if (!logoutBtn) return;
    logoutBtn.addEventListener("click", () => {
        window.location.replace("/logout");
    });
};

// Init JS
// TODO: Wrap all this shit in a an init wrapper
handleShowHidePassword();
handleToggleAvatarDropdown();
handleLogout();
