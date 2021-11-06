// Sample code to perform I/O:

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;                               // Reading input from STDIN
});

process.stdin.on("end", function () {
   main(stdin_input);
});

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

function costOnlineTaxi(distance, O_c, O_f, O_d) {
    return O_c + O_d * (distance - O_f);
}

function costClassicTaxi(distance, C_s, C_b, C_m, C_d) {
    return C_b + C_m * (distance / C_s) + C_d * distance;
}

// Write your code here
function main(input) {
    const inputLines = input.split("\n");
    const D = Number(inputLines[0]);
    const [Oc, Of, Od] = inputLines[1].split(" ").map(n => Number(n));
    const [Cs, Cb, Cm, Cd] = inputLines[2].split(" ").map(n => Number(n));

    console.log(costOnlineTaxi(D, Oc, Of, Od) <= costClassicTaxi(D, Cs, Cb, Cm, Cd) ? "Online Taxi" : "Classic Taxi");
}
