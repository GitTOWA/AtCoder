package main

import (
	"fmt"
)

func main() {
	fmt.Println(processing(sInput()))
}

func sInput() int {
	var s1 int
	fmt.Scan(&s1)
	return s1
}

func processing(s1 int) int {
	var s2 string
	var count int
	x := []string{}
	for i := 0; i < s1; i++ {
		fmt.Scan(&s2)
		x = append(x, s2)
	}
	for _, ch := range x {
		if ch == "Takahashi" {
			count++
		}
	}
	return count

}
