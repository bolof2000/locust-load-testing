const express = require("express");
const app = express();
const PORT = 3000;

app.get("/hello", (req, res) => {
  res.send("Hello endpoint is fast");
});

app.get("/slow", (req, res) => {
  setTimeout(() => {
    res.send("Slow endpoint here ");
  }, 2000);
});

app.listen(PORT, () => {
  console.log("Server is up");
});