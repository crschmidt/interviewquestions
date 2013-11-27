// Ported from Python

function reset(matrix, x, y) {
    if (matrix[x][y]) {
        matrix[x][y] = 0;
        if (x+1 < matrix.length) {
            reset(matrix, x+1, y);
        }
        if (y+1 < matrix.length) {
            reset(matrix, x, y+1);
        }
        if (y>0) {
            reset(matrix, x, y-1);
        }
        if (x>0) {
            reset(matrix, x-1, y);
        }
    }
}

function con(matrix) {
    var con = 0;
    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < matrix.length; j++) {
            if (matrix[i][j]) {
                con += 1;
                reset(matrix, i, j);
            }
        }
    }
    return con;
}

var input = [
   [1, 1, 0, 0],
   [1, 0, 0, 1],
   [0, 0, 1, 1],
   [1, 0, 0, 0]];
console.log(con(input));
