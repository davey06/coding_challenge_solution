import 'dart:io';

final bracketCouple = [
  '()',
  '{}',
  '[]',
];

void _checkParenthesesValid(String input) {
  var temp = input;
  while (input.length <= 104 && temp.length > 1) {
    for (final bracket in bracketCouple) {
      temp = temp.replaceAll(bracket, '');
    }
    if (temp.length == input.length) {
      break;
    } else {
      input = temp;
    }
    print(temp);
  }
  print(temp.isEmpty ? 'Valid' : 'Invalid');
}

void validatingParentheses() {
  print("Loading Validating Parentheses () {} []:");
  while (true) {
    stdout.write("Please input Parentheses: ");
    final input = stdin.readLineSync();
    if (input != null) {
      if (input == 'exit') {
        break;
      }
      _checkParenthesesValid(input);
    }
  }
}
