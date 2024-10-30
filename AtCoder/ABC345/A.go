package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(processing(sImport()))
}

func sImport() string {
	var s string
	fmt.Scan(&s)
	return s
}

func processing(s string) string {
	if strings.HasPrefix(s, "<") && strings.HasSuffix(s, ">") {
		inner := s[1 : len(s)-1]
		// fmt.Println(inner)
		if !strings.Contains(inner, "<") && !strings.Contains(inner, ">") {
			return "Yes"
		}
	}
	return "No"
}
