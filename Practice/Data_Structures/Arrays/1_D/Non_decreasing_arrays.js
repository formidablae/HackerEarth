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
    const T = Number(inputLines[0]);
    for (let i = 0; i < T; i++) {
        const N = Number(inputLines[2 * i + 1]);
        const A = inputLines[2 * i + 2].split(" ").map(n => Number(n));

        let B = [A[0]]
        for (let j = 1; j < N; j++) {
            if (A[j] >= B[j - 1]) {
                B[j] = A[j];
            } else {
                B[j] = A[j] * (Math.ceil(B[j - 1] / A[j]));
            }
        }
        console.log(B.join(" "));
    }
}
