document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('sendMessageButton').addEventListener('click', () => {
        // Fetch the current tab's URL
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            const activeTab = tabs[0];
            const activeTabURL = activeTab.url;

            fetch('http://localhost:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    model: "llama3",
                    messages: [
                        {
                            role: "system",
                            content: `
                                'Given the title and link to an article, provide a short, terse, and precise answer to the question or topic posed in the title. '
                                'Extract only the core information necessary to directly address the topic. Ensure the answer is concise and clear. '
                                'Example Response: '
                                'Title: "25 Years Ago, Steve Jobs Saved Apple From Collapse - It's a Lesson for Every Tech CEO Today" '
                                'Core Answer: '
                                'Steve Jobs saved Apple by streamlining the product line, securing a $150 million partnership with Microsoft, 
                                'focusing on customer experience, and unifying company goals.' `
                        },
                        {
                            role: "user",
                            content: `Hi, the current tab URL is: ${activeTabURL}`
                        }
                    ],
                    stream: false
                })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').textContent = data.message.content;
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
