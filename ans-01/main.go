// Advent of Code 2023 - Day 1 - https://adventofcode.com/2023/day/1
// Date: 22/04/2024

package main

import (
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

const calibrationDocument string = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
`

var expectedAnswers = [4]int{12, 38, 15, 77}
var expectedTotal = sum(expectedAnswers[:])

func sum(arr []int) int {
	sum := 0
	for _, v := range arr {
		sum += v
	}
	return sum
}

func calculateCalibrationValue(line string) int {
	var firstInt, secondInt string

	for i := 0; i < len(line); i++ {
		char := string(line[i])
		src := []byte(char)
		hexEncodedChar := hex.EncodeToString(src)
		if strings.HasPrefix(hexEncodedChar, "3") {
			firstInt = char
			break
		}
	}

	for i := len(line) - 1; i >= 0; i-- {
		char := string(line[i])
		src := []byte(char)
		hexEncodedChar := hex.EncodeToString(src)
		if strings.HasPrefix(hexEncodedChar, "3") {
			secondInt = char
			break
		}
	}

	calibrationValue, err := strconv.Atoi(firstInt + secondInt)

	if err != nil {
		panic(err)
	}

	return calibrationValue
}

func main() {
	var total int
	answers := [4]int{}

	line := ""
	i := 0

	for _, char := range calibrationDocument {
		line += string(char)
		if char == '\n' {
			calibrationValue := calculateCalibrationValue(line)
			answers[i] = calibrationValue
			line = ""
			i++
		}
	}

	total = sum(answers[:])

	fmt.Printf("Expected Answers: %v\n", answers)
	fmt.Printf("Expected Total: %d\n", total)
	fmt.Printf("\n")
	fmt.Printf("Answers: %v\n", answers)
	fmt.Printf("Total: %d\n", total)

	for i := 0; i < len(answers); i++ {
		if answers[i] != expectedAnswers[i] {
			panic("Answer at index " + strconv.Itoa(i) + " does not match")
		}
	}

	if total != expectedTotal {
		panic("Total does not match")
	}
}
