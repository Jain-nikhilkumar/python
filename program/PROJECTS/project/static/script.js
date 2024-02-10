document.addEventListener('DOMContentLoaded', function () {
    const queryForm = document.getElementById('query-form');
    const outputDiv = document.getElementById('output');

    queryForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Get the user's query from the input field
        const userQuery = document.getElementById('user-query').value;

        
        // Send a POST request to your Flask server to generate content
        fetch('/generate_content', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `user-query=${encodeURIComponent(userQuery)}`,
        })
        
            .then(response => response.json())
            .then(data => {
                // Check if the response contains generated content
                if (data && data.generated_content) {
                    const generatedContent = data.generated_content;
                    // Update the content of the 'output' div
                    outputDiv.innerHTML = generatedContent;
                } else {
                    // Handle the case where no content was received
                    outputDiv.innerHTML = 'No content generated.';
                }
            })
            .catch(error => {
                // Handle any errors that occur during the fetch
                console.error('Fetch error:', error);
                outputDiv.innerHTML = 'An error occurred while generating content.';
            });
    });
});
