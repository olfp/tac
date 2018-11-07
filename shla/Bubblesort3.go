package main

import (
	"fmt"
	"strings"
	"strconv"
)

const testnums = "43 96 69 13 21 7 66 69 99 1"

type elem struct {
	v int
	next *elem
}

var data *elem

func parse(str string) (*elem, int) {
	var h, p, q *elem
	nums := strings.Split(str, " ")
	c := 0
	for _, num := range nums {
		p = new(elem)
		p.v, _ = strconv.Atoi(num)
		if(q != nil) {
			q.next = p
		} else {
			h = p
		}
		q = p
		c++
	}
	return h, c
}

func outlist(data *elem) {
	for data != nil {
		fmt.Print(data.v)
		if(data.next != nil) {
			fmt.Print(", ");
		}
		data = data.next
	}
	fmt.Println()
}

func main() {
	data, n := parse(testnums);
	// got list, now sort
	o := n - 1
	for o > 1 {
		on := 1
		this := data
		next := this.next
		for i := 0; i < o; i++ {
                        if this.v > next.v {
                                this.v, next.v = next.v, this.v
                                on = i+1
                        }
			this = next
			next = this.next
                }
                o = on
	}
	// print sorted list
        outlist(data)
}
