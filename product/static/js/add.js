function verifyName(){
    var errorFlag = false;
    var input = removeSpaces(this.value);
    for (let character of input){
        if(!((character.charCodeAt >= 65 && character.charCodeAt <= 90) || (character.charCodeAt >= 97 && character.charCodeAt <= 122))){
            errorFlag = true;
            break;
        }
    }
    generateErrors(this , "Please input a valid name")
}
function removeSpaces(value){
    var output = "";
    for (let character of value){
        if(character !== " "){
            output += character
        }
    }
    return output;
}
function generateErrors(element , errormessage){
    if(element.nextElementSibling != null){
        var errorElement = document.createElement("p");
        errorElement.innerHTML = errormessage;
        errorElement.className = "error"
        element.insertAdjacentElement("afterend" , errorElement);
    }
    else{
        
    }
}