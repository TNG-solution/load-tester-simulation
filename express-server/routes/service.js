const express = require("express");
const router = express.Router();

// @route   GET api/js
// @desc    Top level route    
// @access  Public
router.get("/", (req,res) => res.json({msg: "Handler Works!"}))

// @route   GET api/js/sum
// @desc    Sum two values    
// @access  Public
router.post("/sum", (req, res)=> {
    const {a, b} = req.body;

    res.status(200).json({"result": a + b})
})

// @route   GET api/js/substract
// @desc    Substract two values    
// @access  Public
router.post("/substract", (req,res) => {
    const {a,b} = req.body;
    res.status(200).json({"result": a - b})
})

// @route   GET api/js/multiply
// @desc    Multiply two values    
// @access  Public
router.post("/multiply", (req,res) => {
    const {a, b} = req.body;
    res.status(200).json({"result": a * b})
})

// @route   GET api/js/divide
// @desc    Divide two values    
// @access  Public
router.post("/divide", (req,res) => {
    const {a, b} = req.body;
    if(b === 0) 
        return res.status(400).json({"error": "Cannot divide by zero"})
    
    res.status(200).json({"result": a / b})
})

module.exports = router;