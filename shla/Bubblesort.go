package main

import "fmt"


func main() {
	data := []int{43, 96, 69, 13, 21, 7, 66, 69, 99, 1}
	o := len(data) - 1
	for o > 1 {
		no := 1
		for i := 0; i < o; i++ {
			if data[i] > data[i+1] {
				data[i], data[i+1] = data[i+1], data[i]
				no = i+1
			}
		}
		o = no
	}
	fmt.Println(data)
}
