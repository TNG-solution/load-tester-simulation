const express = require("express");
const router = express.Router();
const User = require("../models/User");
const Role = require("../models/Role");


router.get("/", (req,res) => {
    res.json({"msg": "Database works!"})
})

router.post("/register", async (req,res) => {
    const {name, username} = req.body;
    console.log(name)
    console.log(username)

    let role = Role.findOne({"name": "common"})

    let new_user = new User({
        "name": name,
        "username": username,
        "role": role._id
    })

    new_user.save()
    .then(_=>{
        res.status(200).json({"oki": "doki"})

    }).catch(err=>{
        console.log(err);
        res.status(500).json({"error": err})
    })

})

router.get("/profile", async (req,res) => {
    const {name} = req.query;
    console.log(name);

    User.findOne({"name": name})
    .then( user =>{
        if(user !== null) {
            res.status(200).json({"oki": "doki"})
        }else {
            res.status(404).json({"error":"User not found"})
        }

    }).catch(err=>{
        console.log(err);
        res.status(500).json({"error": err})
    })

})

router.delete("/delete", async (req,res) => {
    const {name} = req.query;

    User.deleteOne({"name": name})
    .then( _ =>{
        res.status(200).json({"oki": "doki"})
    }).catch(err=>{
        console.log(err);
        res.status(500).json({"error": err})
    })

})



module.exports = router;