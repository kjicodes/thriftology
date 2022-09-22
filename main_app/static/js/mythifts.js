let aEl = document.querySelectorAll("h4")

aEl.addEventListener("click", toggleActive);

function toggleActive() {
    console.log("click")
    aEl.classList.toggle("active");
    preventDefault();
}