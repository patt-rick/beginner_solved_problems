String.prototype.replaceAt = function(index, replacement){
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
//created a funstion for the class String to replace at exact index
}

const list = ["manicure", "pedicure", "alright", "chair", "schoolbag", "crates", "bottle","market","house", "unpredictable"];






const word = list[Math.floor(Math.random()*10)]
let blanks = "-".repeat(word.length);
let input = "";
let lives = 5;

function hasBlank(blanks){
    //console.log(blanks.length);

    for (let i = 0;i< blanks.length; i ++){
        if (blanks[i] === "-"){
            return true;
        }
    }
    return false;
}
function haveLives(){
    if(lives > 0){
        return true;
    }
    return false;
}

let demo = document.getElementById("blanks");
let life = document.getElementById("lives");

demo.innerHTML = blanks;
life.innerHTML = `lives : ${lives}`;
function doHangman(){
    let guess = document.getElementById("guess").value;
    input = guess;
    if (!hasBlank(blanks) && haveLives()){
        alert("YOU WIN...")
    }else if(hasBlank(blanks) && haveLives()){
        function fillword(){
            let index = [];
            for (var i = 0; i<word.length;i++){
                if (word[i] === input){
                    index.push(i);//gets the indexes for the input word
                }
            }
            console.log(index);
            if (index.length == 0){//index is 0 when guess is not in the word
                lives--;
            }
            //console.log(`lives = ${lives} `);
            life.innerHTML = `lives : ${lives}`;
            for (var i=0;i<index.length;i++){
                //console.log(index[i]);
                let a = index[i];
                //console.log(blanks[a]);
                blanks = blanks.replaceAt(a, input)
                //console.log(blanks);
                demo.innerHTML = blanks;
            }
        }
        fillword();
    }
    if (!hasBlank(blanks) && haveLives()){
        //demo.innerHTML = blanks;
        alert("YOU WIN...");
    }
    if(hasBlank(blanks) && !haveLives()){
        alert("GAME OVER!!!");
    }
}



// var str1 = document.getElementById("btn").value;
// console.log(typeof(str1));