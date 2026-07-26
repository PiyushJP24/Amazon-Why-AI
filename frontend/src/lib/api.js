import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

const client = axios.create({ baseURL: API, timeout: 60_000 });

export const fetchProducts = () => client.get("/products").then((r) => r.data);
export const fetchProduct = (id) => client.get(`/products/${id}`).then((r) => r.data);
export const whyaiGenerate = (body) => client.post("/whyai/generate", body).then((r) => r.data);
export const whyaiTellMore = (body) => client.post("/whyai/tell-more", body).then((r) => r.data);
export const whyaiFeedback = (body) => client.post("/whyai/feedback", body).then((r) => r.data);
export const whyaiHealth = () => client.get("/whyai/health").then((r) => r.data);
