use std::io;

fn main() {

  let mut n_input = String::new();
  io::stdin().read_line(&mut n_input).expect("");

  let n: i32 = n_input.trim().parse().expect("");

  let mut x_input = String::new();
  io::stdin().read_line(&mut x_input).expect("");

  let x: Vec<i32> = x_input.split_whitespace().map(|x| x.parse().unwrap()).collect();

  let sum: i32 = x.iter().sum();
  let center = (sum as f64 / n as f64).round() as i32;

  let mut ans = Vec::new();

  for i in 0..n as usize {
    let score = (x[i] - center).pow(2);
    ans.push(score);
  }
  let result: i32 = ans.iter().sum();
  println!("{}", result);
}