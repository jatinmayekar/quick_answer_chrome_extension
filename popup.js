document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('sendMessageButton').addEventListener('click', () => {
        // Fetch the current tab's URL
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            const activeTab = tabs[0];
            const url = activeTab.url;

            fetch('http://localhost:5000/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url })
            })
            .then(response => response.json())
            .then(data => {
                const output = data.output;
                console.log(output); 
                document.getElementById('response').textContent = output;
            })
            .catch(error => console.error('Error:', error));
        });
    });
});