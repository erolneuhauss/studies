package main

import "fmt"

// declaring variable without assigning a value to it

func main() {

	var a int
	var b string
	var c float64
	var d bool

	fmt.Printf("%v \t %T \n", a, a)
	fmt.Printf("%v \t %T \n", b, b)
	fmt.Printf("%v \t %T \n", c, c)
	fmt.Printf("%v \t %T \n", d, d)

}
