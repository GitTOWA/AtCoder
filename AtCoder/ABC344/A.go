package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')

	count := 0
	var ans []rune

	for _, i := range s {
		if i == '|' {
			count++
		}
		if count == 1 || i == '|' {
			continue
		} else {
			ans = append(ans, i)
		}
	}

	result := string(ans)
	fmt.Println(result)
}
