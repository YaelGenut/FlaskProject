function inputValidity() {
    console.log('start');
        const inpObj = document.getElementById("Name");
        const inpObj2 = document.getElementById("Pass");
        if (!inpObj.checkValidity()) {
        document.getElementById("errorName").innerHTML = inpObj.validationMessage;
        } 
        if (!inpObj2.checkValidity()) {
            document.getElementById("errorPass").innerHTML = inpObj.validationMessage;
            } 
        if(inpObj2.checkValidity()& inpObj.checkValidity())
        document.getElementById("errorPass").innerHTML = "Input OK";
    } 