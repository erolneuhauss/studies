package main

import "fmt"

// declaring variable without assigning a value to it
// var g string

// assign variable inside a func
//	a := 10

// declaring and assigning at the same time
// is an initialisation a variable to some value
var g string = "cowboy"

func main() {

	a := 10
	b := "golang"
	c := 4.17
	d := true

	fmt.Printf("%v \t %T \n", a, a)
	fmt.Printf("%v \t %T \n", b, b)
	fmt.Printf("%v \t %T \n", c, c)
	fmt.Printf("%v \t %T \n", d, d)
	fmt.Printf("%v \t %T \n", g, g)

}
