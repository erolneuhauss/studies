package main

import "fmt"

func main() {

	dogs := [...]string{"jackie",
		"sammy",
		"joe",
		"rudolf",
	}

	fmt.Printf("jackie addr: %p\n", &dogs[0])
	fmt.Printf("sammy  addr: %p\n", &dogs[1])
	fmt.Printf("joe    addr: %p\n", &dogs[2])
	fmt.Printf("rudolf addr: %p\n", &dogs[3])

	for index, dog := range dogs {
		fmt.Printf("The name of dog No.%d is %s with addr %p \n", index, dog, &dog)
	}

}
