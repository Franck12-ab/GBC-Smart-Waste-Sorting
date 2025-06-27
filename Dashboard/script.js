document.getElementById('analyze-btn').addEventListener('click', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('image-input');
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Processing...';
    resultDiv.classList.remove('hidden');

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        if (response.ok) {
            resultDiv.textContent = `Prediction: ${data.predicted_class} (confidence: ${data.confidence})`;
        } else {
            resultDiv.textContent = data.error || 'Prediction failed.';
        }
    } catch (err) {
        resultDiv.textContent = 'Error connecting to backend.';
    }
});