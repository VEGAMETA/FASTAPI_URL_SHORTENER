document.getElementById('stats-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    var shortLink = document.getElementById('short-link').value.split('/');
    shortLink = shortLink[shortLink.length - 1];
    const response = await fetch(`/api/v1/stats/${shortLink}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById('redirect-count').textContent = data.redirect_count;
        document.getElementById('created-at').textContent = data.created_at;
        document.getElementById('last-redirected-at').textContent = data.last_redirected_at;
        document.getElementById('result').style.display = 'block';
    } else {
        showToast();
    }
});

function showToast() {
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(function () {
        toast.classList.remove('show');
    }, 3000);
}