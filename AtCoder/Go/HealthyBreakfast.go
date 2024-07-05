package main

import "fmt"

func main() {
	fmt.Println(breakfast(sInput()))
}

func sInput() string {
	var str string
	fmt.Scan(&str)
	return str
}

func breakfast(str string) string {
	var ls []string
	for i := 0; i < len(str); i++ {
		if string(str[i]) == "R" {
			ls = append(ls, string(str[i]))
		} else if string(str[i]) == "M" {
			ls = append(ls, string(str[i]))
		}
	}
	if string(ls[0]) == "R" {
		return "Yes"
	} else {
		return "No"
	}
}
