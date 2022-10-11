import 'dart:io';

void baseballGame() {
  print("Loading Baseball Game Scoring:");
  while (true) {
    stdout.write("Please input Scoring without parentheses (ex: 5,2,+,D): ");
    final input = stdin.readLineSync();
    if (input != null) {
      if (input == 'exit') {
        break;
      }
      _calculateScore(input);
    }
  }
}

void _calculateScore(String input) {
  final listScore = input.split(',');
  List<int> records = [];
  for (final score in listScore) {
    final isNumeric = int.tryParse(score);
    if (isNumeric != null) {
      records.add(isNumeric);
    } else if (score == '+') {
      final length = records.length;
      records.add(records[length - 1] + records[length - 2]);
    } else if (score.toUpperCase() == 'D') {
      records.add(records[records.length - 1] * 2);
    } else if (score.toUpperCase() == 'C') {
      records.removeLast();
    }
  }

  final totalScore = records.fold(0, (int prev, int current) => prev + current);

  print('Total Score = $totalScore');
}
