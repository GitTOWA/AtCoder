use std::io;

fn main() {
  let mut input = String::new();
  io::stdin().read_line(&mut input).expect("");

  let _hw: Vec<i32> = input.split_whitespace().map(|s| s.parse().unwrap()).collect();

  // println!("{:?}", _hw);

  // let mut re = Vec::new();
  let mut count = 0;

  for i in 0.._hw[0] as usize {
    for j in 0.._hw[1] as usize {
      if (i + j) % 2 == 0 || (i as i32 - j as i32) % 2 == 0{
        // re.push([i, j]);
        count += 1;
      }
    }
  }
  println!("{}", count);
  // println!("{:?}", re);
}