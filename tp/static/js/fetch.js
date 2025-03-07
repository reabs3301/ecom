
function send_data(url, json={}) {
	csrf_token = document.getElementById("csrf_token").value;
	fetch(url, {
		method: "POST",
		headers: {
			"X-CSRFToken": csrf_token,
			"Content-Type": "application/x-www-form-urlencoded"
		},
		body: new URLSearchParams(json)
	})
	.then(response => response.text()) // HTML response
	.then(html => {
		document.open();
		document.write(html);
		document.close();
	});
}