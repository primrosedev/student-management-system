// StudentMS - small UI interactions
function confirmDelete(name) {
    return confirm("Are you sure you want to delete " + name + "?");
}

// Auto-dismiss flash messages after 4 seconds
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".flash").forEach(function (el) {
        setTimeout(function () {
            el.style.transition = "opacity 0.5s";
            el.style.opacity = "0";
            setTimeout(function () { el.remove(); }, 500);
        }, 4000);
    });
});
