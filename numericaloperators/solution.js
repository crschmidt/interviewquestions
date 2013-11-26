var ops = ["+", "-", "*", "/"];
function legal_op(num1, num2, op) {
  if (op == "/" && num2 == 0) {
    return false;
  } else if (op == "/" && (num1 % num2) != 0) {
    return false;
  }
  return true;
}
function search(numbers, target){
  for (var i=0; i< numbers.length; i++) {
    if (numbers[i] == target) {
      return true;
    }
    for (var j=i+1; j<numbers.length;j++){
      for (var k = 0; k< ops.length;k++) {
        var op = ops[k];
        if (!legal_op(numbers[i], numbers[j], op)) {
          continue;
        }
        var op_string = numbers[i] + op + numbers[j];
        var result = eval(op_string);
        new_numbers = numbers.slice();
        new_numbers.splice(new_numbers.indexOf(numbers[i],1));
        new_numbers.splice(new_numbers.indexOf(numbers[j],1));
        new_numbers.push(result);
        var result = search(new_numbers, target)
        if (result == true) {
          return true;
        }
      }
    }
  }
    return false;
} 

console.log(search([1,7],0));
console.log(search([1,7],8));
console.log(search([4,7],28));
