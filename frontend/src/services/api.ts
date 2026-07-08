import axios from "axios";

const api = axios.create({
    baseURL: "https://potential-dollop-4p9jgj4v9fj7rr-8000.app.github.dev/",
});

export default api;