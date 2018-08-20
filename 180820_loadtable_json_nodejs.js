var fs = require('file-system'); //npm install file-system --save
var AWS = require("aws-sdk");    //npm install aws-sdk

AWS.config.update({
  region: "us-east-1"
});

var docClient = new AWS.DynamoDB.DocumentClient()
var dynamodb = new AWS.DynamoDB();

var Load = JSON.parse(fs.readFileSync('two_menu.json', 'utf8'));
Load.forEach(function(table) {
    var params = {
        TableName: "Table",
        Item: {
            "num": table.num,
            "kname": table.kname,
            "ename": table.ename,
            "price": table.price,
            "url": table.url
      }
    };

    docClient.put(params, function(err, data) {
       if (err) {
           console.error("Error JSON:", JSON.stringify(err, null, 2));
       } else {
           console.log("PutItem succeeded:");
       }
    });
});
