use std::io;

fn main() {
  let mut input = String::new();
  io::stdin().read_line(&mut input).unwrap();
  let nm: Vec<usize> = input.trim().split_whitespace().map(|s| s.parse().unwrap()).collect();
  let n = nm[0];
  let m = nm[1];
  
  input.clear();
  io::stdin().read_line(&mut input).unwrap();
  let a: Vec<i32> = input.trim().split_whitespace().map(|s| s.parse().unwrap()).collect();
  
  input.clear();
  io::stdin().read_line(&mut input).unwrap();
  let b: Vec<i32> = input.trim().split_whitespace().map(|s| s.parse().unwrap()).collect();

  for i in 0..m {
    let mut none = true;
    for j in 0..n {
      if b[i] >= a[j] {
        println!("{}", j + 1);
        none = false;
        break;
      }
    }
    if none {
      println!("-1");
    }
  }
}
