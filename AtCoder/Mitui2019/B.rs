use std::io;

fn main() {
  let mut n_input = String::new();
  io::stdin().read_line(&mut n_input).expect("");

  let n: f32 = n_input.trim().parse().expect("");

  // let tax_out: i32 = (n / 1.08).round() as i32;

  // let tax_in: i32 = ((tax_out as f32) * 1.08) as i32;

  // if n as i32 == tax_in {
  //   println!("{}", tax_out);
  // } else {
  //   println!(":(");
  // }

  let mut result = String::from(":(");

  for i in 1..n as i32 {
    let tax: i32 = ((i as f32) * 1.08) as i32;
    if tax == n as i32 {
      result = i.to_string();
      break
    }
  }

  println!("{}", result);
}