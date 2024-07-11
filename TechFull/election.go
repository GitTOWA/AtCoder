// s1 = list(map(int,input().split()))

// ls = []

// for i in range(s1[1]):
//     x = int(input())
//     ls.append(x)

// total = 0
// for i in range(s1[0]):
//     x = ls.count(i)
//     if total < x:
//         total = x
//         num = i
// print(num)

package main

import (
	"fmt"
)

func main() {
	s1, s2 := sInput()
	fmt.Println(processing(s1, s2))
}

func sInput() (int, int) {
	var s1, s2 int
	fmt.Scanf("%d %d", &s1, &s2)
	return s1, s2
}

func processing(s1, s2 int) int {
	var x int
	ls := []int{}
	for i := 0; i < s2; i++ {
		fmt.Scan(&x)
		ls = append(ls, x)
	}
	count := 0
	total := 0
	num := 0
	for i, j := range ls {
		if i == j {
			count++
			if total < count {
				total = count
				num = i
			}
		} else {
			count = 0
		}
	}
	return num
}

// ソートしないとだめ
