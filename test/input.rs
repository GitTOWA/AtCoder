use std::io;

fn main() {
  // 最初の入力を読み込む (単一の整数値 t)
  let mut t = String::new();
  io::stdin().read_line(&mut t).expect("Failed to read line");

  // t を整数に変換
  let t: i32 = t.trim().parse().expect("Please enter a number");

  // Tのリストを読み込む
  let mut input = String::new();
  io::stdin().read_line(&mut input).expect("Failed to read line");

  // 空白区切りの文字列を整数のベクターに変換
  let numbers: Vec<i32> = input
  .trim()
      .split_whitespace()
      .map(|s| s.parse().expect("Please enter a valid number"))
      .collect();

  // 出力
  println!("{}", t);
  println!("{:?}", numbers); // Vecの内容を表示
}
