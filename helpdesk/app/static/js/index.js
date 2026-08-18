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

const handleDismissNotification = () => {
    window.onload = () => {
        const notificationContainer = document.getElementById(
            "notification-container",
        );
        if (!notificationContainer) return;
        notificationContainer.addEventListener("click", (event) => {
            const notifDismissBtn = event.target.closest(".dismiss-btn");
            if (!notifDismissBtn) return;
            const notif = notifDismissBtn.closest("div .notification");
            if (!notif) return;
            notif.remove();
        });
    };
};

// Init JS
// TODO: Wrap all this shit in a an init wrapper
handleShowHidePassword();
handleToggleAvatarDropdown();
handleLogout();
handleDismissNotification();
