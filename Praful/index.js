const express = require('express')
const app = express();
var bodyParser = require("body-parser");
var mongoose = require("mongoose");


//body-parser
app.use (bodyParser.urlencoded({extended: true}));

app.set('view engine', 'ejs');
app.use(express.static(__dirname + "/public"));



//mongoose connnections
mongoose.connect("mongodb://localhost/mcq");
var TestSchema = new mongoose.Schema({
    contestName: String,
    tag : String,
    question : String,
    op1: String,
    op2 : String,
    op3: String,
    op4: String,
    ans: String
});
var Test = mongoose.model("Contest", TestSchema);

var SignUpSchema = new mongoose.Schema({
	name : String,
    mail: String,
    password: String,  
});
var SignUp = mongoose.model("SignUp", SignUpSchema);


var ScoreSchema = new mongoose.Schema({
	userName : String,
    tag: String,
    score: String,  
});
var Score = mongoose.model("Scorecard", ScoreSchema);
//mongoose connection ends











//list definations
var accountList = [
    {name : "salmond", mail:"salmond@gmail.com", password: "12345"}
];
var contestList = [
    {contestName : "salmond", time:"2:30"}
];
Test.distinct("tag", function(err, listTest){
    if (err){
        console.log(err);
    }else{
        console.log("Test command executed Successful!!!");
        console.log(listTest);
        contestList = listTest;  
    }
});
var testList = [
    {question : "",op1: "", op2 : "", op3: "",op4: ""}
];

var answerList = [
    {question: 0, ans: 0,score: 0}
];
var tagName="";
var userName="";


//post requests
app.post('/next',function (req, res) {
    var name = req.body.tag;
    tagName = name;
    Test.find({tag: name}, function(err, TestList){
		if (err){
			console.log(err);
		}else{
            console.log("testList command executed Successful!!!");
            //contests   
            console.log(TestList[1]);
                testList =  TestList;
                res.render("test",{contest: contestList,test: testList, account: accountList, answer: answerList});
                console.log("testlist successful!!!");
                console.log(name);
		}
	});
});

app.post('/check',function (req, res) {
    var score = req.body.putScore;
    console.log(score);
    var newScore = [{userName: userName, tag: tagName, score: score}];
    Score.create(newScore,function(err, newlyCre){
		if(err)
		{
			console.log(err);
		}
		else{
            console.log("score created!!!");
            res.redirect("/user");
        }
       
	});
});

//login command starts
app.post('/login',function (req, res) {
    var name = req.body.username;
    var password = req.body.pass;
    
   
    SignUp.find({$and: [{name: name}, {password: password}]}, function(err, listSignUp){
		if (err){
			console.log(err);
		}else{
            console.log("login command executed Successful!!!");
            if (listSignUp.length != 0){
                userName =  name;
                //contests
                Test.distinct("tag", function(err, listTest){
                    if (err){
                        console.log(err);
                    }else{
                        console.log("Test command executed Successful!!!");
                        console.log(listTest);
                        contestList = listTest;  
                    }
                });

                accountList = listSignUp;
                res.render("user",{contests: contestList, account: accountList});
                console.log("login successful!!!");
                
            }else{ 
                res.redirect("login");
                console.log("login failed!!!");
            }
		}
	});
});
//login post request ends


//signup post request starts
app.post('/signup',function (req, res) {
    //var dbo = db.db("mcq");
    var name = req.body.name;
    var mail = req.body.mail;
    var password = req.body.pass;
	var newAccount = new SignUp({
        name: name, mail: mail, password: password
        });

	newAccount.save(function(err, newlyCre){
		if(err)
		{
			console.log(err);
		}
		else{
            console.log("account created!!!");
			res.redirect("/home");
        }
       
	});
	
	
});
//signup post request ends

app.post('/setter',function (req, res) {

    var contestName = req.body.contestName;
    var tag = req.body.tag;
    var question = req.body.question;
    var op1 = req.body.op1;
    var op2 = req.body.op2;
    var op3 = req.body.op3;
    var op4 = req.body.op4;
    var ans = req.body.ans;

	var newContest = {contestName: contestName, tag: tag, question: question, op1: op1, op2: op2, op3: op3, op4: op4, ans: ans};

	Test.save(newContest,function(err, newlyCre){
		if(err)
		{
			console.log(err);
		}
		else{
            console.log("contest created!!!");
            res.redirect("/setter");
        }
       
	});
	
	
});






app.get('/', function(req, res) { 
    //res.send('Hello World!')
    console.log("Home page");
    res.render("home");}
);

app.get('/home', function(req, res) { 
    //res.send('Hello World!')
    console.log("Home page");
    res.render("home");}
);

app.get('/signup',function (req, res) {
    console.log("Signup page");
    res.render("signup");}
);

app.get('/login',function (req, res) {
    console.log("Login page");
    res.render("login");}
);

//test taker
app.get('/user',function (req, res) {
    console.log("User profile");
    Test.distinct("tag", function(err, listTest){
        if (err){
            console.log(err);
        }else{
            console.log("Test command executed Successful!!!");
            console.log(listTest);
            contestList = listTest;  
        }
    });
    res.render("user", {contests: contestList, account: accountList});
});

app.get('/test',function (req, res) {
    console.log("User profile");
    res.render("test", {account: accountList, contest: contestList, test: testList, answer: answerList});
});

app.get('/setter',function (req, res) {
    console.log("User profile");
    res.render("setter");}
);

app.listen(4000, () => console.log('App server starting at port 3000!'))
