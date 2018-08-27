import "./scss/bulmaio_jinja2.scss";
import "./scss/pygments.css";

document.addEventListener("DOMContentLoaded", () => {

    const categories = document.querySelectorAll(".bd-category");

    Array.from(categories).forEach(category => {
        const toggle_el = category.querySelector(".bd-category-toggle");
        if (toggle_el) {
            toggle_el.addEventListener("click", () => {
                category.classList.toggle("is-active");
            });
        }
    });
});
