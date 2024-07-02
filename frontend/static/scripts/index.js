document.getElementById('shorten-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    const url = document.getElementById('url').value;
    const response = await fetch('/api/v1/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    });
    const data = await response.json();
    const currentSite = window.location.origin;
    const fullShortUrl = `${currentSite}/${data.short_url}`;
    document.getElementById('short-url').textContent = fullShortUrl;
    document.getElementById('short-url').href = fullShortUrl;
    document.getElementById('result').style.display = 'block';
});

document.getElementById('copy-button').addEventListener('click', function () {
    const shortUrl = document.getElementById('short-url').textContent;
    navigator.clipboard.writeText(shortUrl).then(function () {
        showToast();
    }, function (err) {
        console.error('Could not copy text: ', err);
    });
});

function showToast() {
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(function () {
        toast.classList.remove('show');
    }, 3000);
}