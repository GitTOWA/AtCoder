use std::io;

fn main() {
  let mut nmc_input = String::new();
  io::stdin().read_line(&mut nmc_input).expect("");

  let nmc: Vec<i32> = nmc_input.split_whitespace().map(|s| s.parse().unwrap()).collect();

  let mut b_input = String::new();
  io::stdin().read_line(&mut b_input).expect("");

  let _b: Vec<i32> = b_input.split_whitespace().map(|s| s.parse().unwrap()).collect();

  let mut a = Vec::new();

  for _i in 0..nmc[0] as i32 {
    let mut a_input = String::new();
    io::stdin().read_line(&mut a_input).expect("");
    let a_list: Vec<i32> = a_input.split_whitespace().map(|s| s.parse().unwrap()).collect();
    a.push(a_list);
  }

  let mut count = 0;

  for i in 0..nmc[0] as i32 {
    let mut ans = 0;
    for j in 0..nmc[1] as i32 {
      let x = a[i as usize][j as usize] * _b[j as usize];
      ans += x;
    }
    let _result = ans + (nmc[2] as i32);
    if _result > 0 {
      count += 1;
    }
  }

  println!("{}", count);
}