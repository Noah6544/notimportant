document.addEventListener('DOMContentLoaded', function() {
    // Function to get query string value by key
    function getQueryStringValue(key) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(key);
    }

    // Get the 'tier' value from the query string
    const tierValue = getQueryStringValue('tier');
    console.log(tierValue)

    // Set the 'tier' value as the value of the input with id 'tier'

    document.getElementById('tier').value = tierValue;

});