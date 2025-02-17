// async await fetch
async function fetchData() {
    try {
        let response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        let data = await response.json();
        console.log(data);
    } catch(error) {
        console.error("Error:", error);
    }
}

fetchData();