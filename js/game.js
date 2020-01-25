var myJSON = '{"name":"John", "age": "89%", "city":"New York"}';
var myObj = JSON.parse(myJSON);
document.getElementById("demo").style.width = myObj.age;
document.getElementById("h-per").innerHTML = myObj.age;
var myManaScale = "60%"
document.getElementById("mana-scale").style.width = myManaScale;
document.getElementById("m-per").innerHTML = myManaScale;

var monsterHealth = "12%";
document.getElementById("monster-health").style.width = monsterHealth;
document.getElementById("h-per-monster").innerHTML = monsterHealth;

var monsterMana = "33%";
document.getElementById("monster-mana").style.width = monsterMana;
document.getElementById("m-per-monster").innerHTML = monsterMana;