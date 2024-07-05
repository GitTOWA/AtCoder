package main

import (
	"fmt"
)

func main() {
	fmt.Println(unique(sInput()))
}

func sInput() []int {
	var s, x int
	ls := []int{}

	fmt.Scan(&s)
	for i := 0; i < s; i++ {
		fmt.Scan(&x)
		ls = append(ls, int(x))
	}

	return ls
}

func unique(nums []int) int {
	encountered := map[int]bool{}
	result := []int{}

	for v := range nums {
		if encountered[nums[v]] == false {
			encountered[nums[v]] = true
			result = append(result, nums[v])
		}
	}

	return len(result)
}
