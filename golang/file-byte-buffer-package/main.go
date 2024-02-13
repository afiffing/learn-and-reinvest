package main

import (
	"bytes"
	"log"
	"os"
)

func main() {
	// file creation, defer close and writing
	f, err := os.Create("") // Create
	if err != nil {
		//log.Fatalf("error creating the file: %s", err)
		log.Println("error creating the file:", err)
	}
	defer func(f *os.File) {
		err := f.Close()
		if err != nil {
			//log.Fatalf("error closing the file: %s", err)
			log.Println("error closing the file:", err)
		}
	}(f)

	_, err = f.Write([]byte("Hello Gophers writing the slice of bytes to this file"))
	if err != nil {
		//log.Fatalf("error opening the file: %s", err)
		log.Println("error opening the file:", err)
	}

	// introduction to byte buffers, you can write to the buffer without making use of the variable.
	b := bytes.NewBufferString("Hello gophers from the byte string")
	b.WriteString(" String appended")
	//pointer to byte buffer
	log.Printf("%T\n", b)
	log.Println(b)
	log.Printf("%T\n", &b)
	log.Println(&b)
	//String
	log.Printf("%T\n", b.String())
	log.Println(b.String())

	//buffer reset
	b.Reset()
	b.WriteString("New data")
	log.Println(b.String())

}
