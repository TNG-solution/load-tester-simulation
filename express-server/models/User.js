const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const UserSchema = new Schema({
    "name": {
        "type": String,
        "required": true
    },
    "username": {
        "type": String,
        "required": true
    },
    "role" : {
        type: Schema.Types.ObjectId,
        "ref": "roles"
    }
});

module.exports = User = mongoose.model("users", UserSchema)