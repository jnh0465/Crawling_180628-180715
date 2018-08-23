var fs = require('file-system'); //npm install file-system --save
var AWS = require("aws-sdk");    //npm install aws-sdk

AWS.config.update({
  region: "us-east-1" //aws dyonamodb 테이블이 있는 리전
});

var docClient = new AWS.DynamoDB.DocumentClient()
var dynamodb = new AWS.DynamoDB();

var Load = JSON.parse(fs.readFileSync('two_menu.json', 'utf8')); //json파일
Load.forEach(function(table) {
    var params = {
        TableName: "Table", //테이블이름
        Item: {
            "num": table.num,      //json파일 형식대로 나눠서 들어감.
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
