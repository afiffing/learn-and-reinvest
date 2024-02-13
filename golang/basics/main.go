package main

import "fmt"

type book struct {
	title string
}

type game struct {
	gamename string
}

type puzzles struct {
	puzzles string
}

func (b book) bookName(s string) (string, string) {
	return b.title, s
}

func superHeroName(s string) {
	fmt.Println("I am", s)
}

func main() {

	// Array or slice of bytes
	xs := [...]string{"d0", "d1", "d2", "d3"}
	fmt.Println(xs)
	for i, v := range xs {
		fmt.Printf("index: %d and value: %s\n", i, v)
	}

	//structs and methods
	b1 := book{title: "The secrets of dumbledore"}
	c1, d1 := b1.bookName("Fantastic beasts: ")
	fmt.Println(d1, c1)

	//anonymous struct
	b2 := struct {
		newtitle string
	}{newtitle: "The lord of the ring"}

	fmt.Println(b2.newtitle)

	//anonymous func with param/args and returns
	data := func(s string) int {
		//fmt.Println(s)
		return 5
	}("Who are you?")

	superHeroName("Batman")
	fmt.Println(data)

	// func (r receiver) identifier(p params) (r returns){}
	// must watch for interfaces https://www.youtube.com/watch?v=qJKQZKGZgf0
	// A type can only satisfy an interfaces when it implements all the methods of that interface.

	// Keep an eye on how an interface can be passed to a func and then underlying meth can be accessed

	// func saysSomething ( h human ){
	//  h.speak() //speak is common method of two structs  person and secretagent, watch interfaces and polymorphism, udemy Tod Mcleod
	// }

}
