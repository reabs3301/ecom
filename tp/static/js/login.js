function save_username_role(username, role) {
	console.log("save_username_role " + username + " " + role);
}


function local_storage_get(key) {
	return localStorage.getItem(key);
}

function local_storage_set(key, value) {
	localStorage.setItem(key, value);
	console.log("local_storage_set " + key + " " + local_storage_get(key));
}