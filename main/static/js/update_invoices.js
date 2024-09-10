document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("editModalInvoices");
    var btn = document.querySelector(".edit-button");
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