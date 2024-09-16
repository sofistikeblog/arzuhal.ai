document.getElementById('dilekce-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const kisiAdi = document.getElementById('kisiAdi').value;
    const anahtarKelime = document.getElementById('anahtarKelime').value;
    
    const response = await fetch('/generate-dilekce', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ kisiAdi, anahtarKelime })
    });
    
    const data = await response.json();
    document.getElementById('output').innerText = data.generated_text;
});
