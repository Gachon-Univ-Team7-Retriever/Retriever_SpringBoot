async function copyDatabase() {
    const sourceDb = document.getElementById('sourceDb').value;
    const targetDb = document.getElementById('targetDb').value;
    const statusDiv = document.getElementById('status');

    // Validation
    if (!sourceDb || !targetDb) {
        statusDiv.textContent = "Please fill in all fields.";
        statusDiv.classList.add('error');
        return;
    }

    statusDiv.textContent = "Processing...";
    statusDiv.classList.remove('error');

    // Call the backend to perform the copy operation
    try {
        const response = await fetch('/copy-database', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sourceDb, targetDb }),
        });

        const result = await response.json();

        if (response.ok) {
            statusDiv.textContent = `Database copied successfully: ${result.message}`;
        } else {
            statusDiv.textContent = `Error: ${result.message}`;
            statusDiv.classList.add('error');
        }
    } catch (error) {
        statusDiv.textContent = `Error: ${error.message}`;
        statusDiv.classList.add('error');
    }
}
