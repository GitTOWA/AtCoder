use std::io;

fn main() {
  let mut nab_input = String::new();
  io::stdin().read_line(&mut nab_input).expect("");

  let nab: Vec<i32> = nab_input.split_whitespace().map(|s| s.trim().parse().expect("")).collect();

  let mut s = String::new();
  io::stdin().read_line(&mut s).expect("");

  let mut join = Vec::new();
  let mut a_count = 0;
  let mut b_count = 0;

  for i in s.trim().chars() {
    let mut result = String::from("No");

    if i == 'a' && a_count + b_count < nab[1] + nab[2] {
      result = String::from("Yes");
      a_count += 1;
    } else if i == 'b' && a_count + b_count < nab[1] + nab[2] && b_count < nab[2] {
      result = String::from("Yes");
      b_count += 1;
    }
    join.push(result);
  }

  for i in join {
    println!("{}", i);
  }
}