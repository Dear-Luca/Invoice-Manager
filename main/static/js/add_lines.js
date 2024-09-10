document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("addModalLines");
    var btn = document.querySelector(".add-line-button");
    var closeButton = modal.querySelector(".close");

    btn.onclick = function() {
        modal.style.display = "block";
    }

    closeButton.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});