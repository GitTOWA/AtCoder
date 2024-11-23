// use std::io;

// fn main() {
//   let mut a = String::new();
//   let mut total: u32 = 0;
//   let mut count: u32 = 0;

//   io::stdin().read_line(&mut a).expect("");

//   if let Some(one) = a.chars().nth(0) {
//     let one_v = one as u32;
//       if let Some(two) = a.chars().nth(1) {
//         let two_v = two as u32;
//         println!("{}", two_v);
//         while total < two_v {
//           total += one_v;
//           count += 1;
//       }
//     }
//   }
//   println!("{}", count);

// }

use std::io;

fn main() {
  let mut input = String::new();
  io::stdin().read_line(&mut input).expect("");
  
  let s: Vec<i32> = input
    .split_whitespace()
    .map(|x| x.parse().unwrap())
    .collect();
  
  let mut total = 1;
  let mut count = 0;
  
  while total < s[1] {
    total += s[0] - 1;
    count += 1;
    // if count > 1 {
    //   total -= 1
    // }
  }
  
  println!("{}", count);
}
