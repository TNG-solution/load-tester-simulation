const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json());

const connectDB = require("../config/db");
connectDB();

/*** routes ***/
const handler = require("../routes/service");
app.use("/api/js", handler);

const database = require("../routes/database");
app.use("/api/js/database", database);

app.get("*", (req,res) => res.json({msg: "Loads js Api!"}))

const port = process.env.PORT;

app.listen(port, () => console.log(`Server running on port ${port}`))