package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// 標準入力のためのスキャナを作成
	scanner := bufio.NewScanner(os.Stdin)

	// 1行目の入力（スペースで区切られた整数のリスト）
	scanner.Scan()
	line := scanner.Text()                 // 入力された行を取得
	strNumbers := strings.Split(line, " ") // スペースで区切ってリストにする

	// 整数リストに変換
	var x []int
	for _, str := range strNumbers {
		num, _ := strconv.Atoi(str) // 文字列を整数に変換
		x = append(x, num)
	}

	// 2行目の入力（2つの整数 x, y）
	scanner.Scan()
	line = scanner.Text()              // 入力された行を取得
	pair := strings.Split(line, " ")   // スペースで区切る
	xValue, _ := strconv.Atoi(pair[0]) // 1つ目の整数
	yValue, _ := strconv.Atoi(pair[1]) // 2つ目の整数

	// 出力例（必要に応じて処理する）
	fmt.Println("List x:", x)
	fmt.Println("x:", xValue, "y:", yValue)
}
