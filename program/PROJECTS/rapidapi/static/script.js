// Wait for the DOM to be fully loaded before running JavaScript
document.addEventListener('DOMContentLoaded', function () {
    // Get references to HTML elements
    const form = document.querySelector('form');
    const metadataSection = document.getElementById('metadata');

    // Add an event listener to the form submission
    form.addEventListener('submit', async function (event) {
        event.preventDefault(); // Prevent the default form submission behavior
        
        // Get the URL input value from the form
        const urlInput = form.querySelector('input[type="url"]');
        const url = urlInput.value;

        // Send a POST request to the server to fetch OpenGraph metadata
        try {
            const response = await fetch('/fetch_metadata', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `url=${encodeURIComponent(url)}`,
            });

            if (response.ok) {
                const data = await response.json();
                displayMetadata(data);
            } else {
                metadataSection.innerHTML = 'Error fetching metadata.';
            }
        } catch (error) {
            metadataSection.innerHTML = 'An error occurred.';
        }
    });

    // Function to display OpenGraph metadata
    function displayMetadata(data) {
        const { title, description, image_url } = data;

        // Update the HTML elements with metadata
        metadataSection.innerHTML = `
            <h2>Metadata:</h2>
            <p><strong>Title:</strong> ${title}</p>
            <p><strong>Description:</strong> ${description}</p>
            <img src="${image_url}" alt="Image">
        `;
    }
});
// Wait for the DOM to be fully loaded before running JavaScript
document.addEventListener('DOMContentLoaded', function () {
    // Get references to HTML elements
    const form = document.querySelector('form');
    const metadataSection = document.getElementById('metadata');

    // Add an event listener to the form submission
    form.addEventListener('submit', async function (event) {
        event.preventDefault(); // Prevent the default form submission behavior
        
        // Get the URL input value from the form
        const urlInput = form.querySelector('input[type="url"]');
        const url = urlInput.value;

        // Send a POST request to the server to fetch OpenGraph metadata
        try {
            const response = await fetch('/fetch_metadata', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `url=${encodeURIComponent(url)}`,
            });

            if (response.ok) {
                const data = await response.json();
                displayMetadata(data);
            } else {
                metadataSection.innerHTML = 'Error fetching metadata.';
            }
        } catch (error) {
            metadataSection.innerHTML = 'An error occurred.';
        }
    });

    // Function to display OpenGraph metadata
    function displayMetadata(data) {
        const { title, description, image_url } = data;

        // Update the HTML elements with metadata
        metadataSection.innerHTML = `
            <h2>Metadata:</h2>
            <p><strong>Title:</strong> ${title}</p>
            <p><strong>Description:</strong> ${description}</p>
            <img src="${image_url}" alt="Image">
        `;
    }
});
