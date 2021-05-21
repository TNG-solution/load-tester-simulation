const mongoose = require ('mongoose');
const Schema = mongoose.Schema;

const RoleSchema = new Schema ({

	name: {
		type: String,
		required: true
	},

	actions: [
		{
			type: String,
			default: 'null'
		}
	]

});

module.exports = Role = mongoose.model("roles", RoleSchema)