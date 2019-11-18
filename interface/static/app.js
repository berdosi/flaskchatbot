(function () {
	const queryField = document.querySelector("#query");
	const output = document.querySelector("#replies>dl");

	queryField.addEventListener("keyup", (event) => {
		if (event.key === "Enter") {
			handleQuery();
		}
	});

	function handleQuery() {
		const query = queryField.value;

		const feedback = document.createElement("dt");
		const response = document.createElement("dd");

		output.prepend(feedback, response);
		feedback.innerText = query;

		fetch("/api/query/" + encodeURIComponent(query))
			.then(responseObject => responseObject.json())
			.then(value => response.innerText = JSON.stringify(value))
			.catch((e) => response.innerText = e);
	}
})()