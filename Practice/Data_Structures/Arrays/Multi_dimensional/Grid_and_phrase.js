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

// Write your code here
function main(input) {
    const inputLines = input.split("\n");
    const [n, m] = inputLines[0].split(" ").map(x => Number(x));
    const text = inputLines.slice(1, n + 1);
    let horizontally = 0;
    let vertically = 0;
    let diagonally = 0;

    if (m >= 4) {
        for (let i = 0; i < n; i++) {
            for (let j = 3; j < m; j++) {
                // console.log(text[i].substring(j - 3, j + 1) + "\n");
                if (text[i].substring(j - 3, j + 1) === "saba") {
                    horizontally++;
                }
            }
        }
    }

    if (n >= 4) {
        for (let i = 0; i < m; i++) {
            for (let j = 3; j < n; j++) {
                /*console.log(text[j - 3][i] + "\n" +
                           text[j - 2][i] + "\n" +
                           text[j - 1][i] + "\n" +
                           text[j][i] + "\n");*/
                if (text[j - 3][i] === "s" &&
                    text[j - 2][i] === "a" &&
                    text[j - 1][i] === "b" &&
                    text[j][i] === "a") {
                    vertically++;
                }
            }
        }
    }

    if (n >= 4 && m >= 4) {
        for (let i = 3; i < m; i++) {
            for (let j = 3; j < n; j++) {
                /*console.log(
                    " ".repeat(i - 3) + text[j - 3][i - 3] + "\n" +
                    " ".repeat(i - 2) + text[j - 2][i - 2] + "\n" +
                    " ".repeat(i - 1) + text[j - 1][i - 1] + "\n" +
                    " ".repeat(i) + text[j][i] + "\n");
                console.log(
                    " ".repeat(i) + text[j - 3][i] + "\n" +
                    " ".repeat(i - 1) + text[j - 2][i - 1] + "\n" +
                    " ".repeat(i - 2) + text[j - 1][i - 2] + "\n" +
                    " ".repeat(i - 3) + text[j][i - 3] + "\n");*/
                if (text[j - 3][i - 3] === "s" &&
                    text[j - 2][i - 2] === "a" &&
                    text[j - 1][i - 1] === "b" &&
                    text[j][i] === "a") {
                    diagonally++;
                } else if (text[j - 3][i] === "a" &&
                          text[j - 2][i - 1] === "b" &&
                          text[j - 1][i - 2] === "a" &&
                          text[j][i - 3] === "s") {
                    diagonally++;
                }
            }
        }
    }

    // console.log("horizontally", horizontally);
    // console.log("vertically", vertically);
    // console.log("diagonally", diagonally);
    console.log(horizontally + vertically + diagonally);
}
