import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (_req, res) => {
  res.send(`<h1>Hello from Lab02 (Express) 🎉</h1>`);
});

app.get("/health", (_req, res) => res.json({ status: "ok" }));

app.listen(PORT, "0.0.0.0", () => {
  console.log(`✅ Server running on http://0.0.0.0:${PORT}`);
});
