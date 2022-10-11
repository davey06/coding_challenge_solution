import 'dart:io';

import 'package:coding_challenge/baseball_game/solution.dart';
import 'package:coding_challenge/validating_parentheses/solution.dart';

void main(List<String> arguments) {
  print("Welcome to Coding Challenge Test");
  print("Please Select Challenge:");
  print("1. Validating Parentheses");
  print("2. Baseball Game");
  print("3. Fibonacci");
  bool validSelection = false;
  String? input;
  while (!validSelection) {
    stdout.write("\nYour Selection: ");
    input = stdin.readLineSync();

    switch (input) {
      case '1':
      case '2':
        // case '3':
        validSelection = true;
        break;
      default:
        print('Invalid Choice, please enter again. to exit use CTRL + C');
    }
  }
  switch (input) {
    case '1':
      validatingParentheses();
      break;
    case '2':
      baseballGame();
      break;
    case '3':
    default:
      break;
  }
  print("FINISHED");
  exit(0);
}
