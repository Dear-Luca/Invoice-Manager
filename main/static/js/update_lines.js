document.addEventListener("DOMContentLoaded", function(){
    var modal = document.getElementById("editModalLines");
    var closeButton = modal.querySelector(".close");
    var editButtons = document.getElementsByClassName("edit-line-button");

    Array.from(editButtons).forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            console.log("Edit button clicked!");
            var lineDetails = this.closest('.items-result').querySelector('.line-details');

            if (lineDetails) {
                var currency = lineDetails.querySelector('strong:nth-of-type(2)').nextSibling.textContent.trim();
                var rcCenter = lineDetails.querySelector('strong:nth-of-type(3)').nextSibling.textContent.trim();
                var category = lineDetails.querySelector('strong:nth-of-type(4)').nextSibling.textContent.trim();
                var idLine = lineDetails.querySelector('strong:nth-of-type(5)').nextSibling.textContent.trim();
                
                document.getElementById('edit-currency').value = currency;
                document.getElementById('edit-rc_center').value = rcCenter;
                document.getElementById('edit-category').value = category;
                document.getElementById('edit-id-line').value = idLine;

                modal.style.display = "block";
            } else {
                console.error("lineDetails not found!");
            }
        });
    });

    closeButton.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});