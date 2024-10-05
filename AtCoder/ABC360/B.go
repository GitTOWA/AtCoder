package main

import (
	"fmt"
	"strings"
)

func main() {
	s1, s2 := sInput()
	fmt.Println(processing(s1, s2))
}

func sInput() (string, string) {
	var s1, s2 string
	fmt.Scanf("%s %s", &s1, &s2)
	return s1, s2
}

// これじゃない
//
//	func processing(s1, s2 string) string {
//		var total strings.Builder
//		count := 0
//		for _, ch := range s1 {
//			count += 1
//			if count%2 == 0 {
//				total.WriteString(string(ch))
//			}
//		}
//		if total.String() == s2 {
//			return "Yes"
//		} else {
//			return "No"
//		}
//	}

// func processing(s1, s2 string) string {
//     var result string
//     for i := 1; i <= len(s1); i++ {
//         var total strings.Builder
//         for j, ch := range s1 {
//             if (j+1)%i == 0 {
//                 total.WriteString(string(ch))
//                 if total.String() == s2 {
//                     result = "Yes"
//                     break
//                 } else {
//                     result = "No"
//                 }
//             }
//         }
//         if result == "Yes" {
//             break
//         }
//     }
//     return result
// }

func processing(s1, s2 string) string {
	var result string
	for i := 1; i <= len(s1); i++ {
		var total strings.Builder
		for j, ch := range s1 {
			if i == len(s1) {
				break
			} else if i != 0 && (j+1)%i == 0 {
				total.WriteString(string(ch))
				fmt.Println(total.String())
				if total.String() == s2 {
					result = "Yes"
					break
				} else {
					result = "No"
				}
			}
		}
		if result == "Yes" {
			break
		}
	}
	return result
}
