let txt = "abcdefghijklmnopqrstuvwxyz";
let txt0 = txt.length;
console.log(txt0);

let txt1 = "Please visit Microsoft!";
let txt2 = txt1.replace("Please visit Microsoft!", "BGU");

console.log(txt2);




function great(){
    const d = new Date(); /* Var is global, const is for the specific block */
    var h = d.getHours();
    console.log(h);
    if (h<12) {
        let greeting = "Good morning";
        console.log(greeting);
        document.getElementById("1").innerHTML = 'greeting';
    } else if(h>12 & h<18){
        let greeting2 = "Good afternoon";
        console.log(greeting);
        document.getElementById("1").innerHTML = greeting2;
    } else {
        let greeting3 = "good evening";
        document.getElementById("1").innerHTML = greeting3;
    }
}

let cars = ['Toyota', 'Honda', 'Mazda'];
console.log(cars);
text="";
text+= cars[0];
console.log(text);

var i;
for (i = 0; i < cars.length; i++) {
    text += cars[i] + "<br>";
    console.log(text);
}

// variables for the function:

var imgs=[
    "imgs/a.jpg",
    "imgs/b.jpg",
    "imgs/c.jpg"
];

var i=0;

// functions:

function StopMotion() {
    setTimeout(() => {
            document.getElementById("SMimg").src = imgs[i];
            i++;
            if (i<imgs.length) {
                StopMotion();
            }
            else {
                i=0 ;
            }
    }, 500);
}

var person = {
    firstName: "John",
    lastName: "Doe",
    id: "444",
    fullName: function() {return this.firstName + "  " + this.lastName;}
};

console.log(person.fullName());