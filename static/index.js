 function showSpinner() {
            document.getElementById('spinner-container').style.display = 'block';
        }

        // Function to hide spinner when done
        function hideSpinner() {
            document.getElementById('spinner-container').style.display = 'none';
        }

        // Hide the spinner on page load if no processing is needed
        window.onload = function() {
            hideSpinner();
        }