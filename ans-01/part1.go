// Advent of Code 2023 - Day 1 - Part 1 - https://adventofcode.com/2023/day/1
// Date: 22/04/2024

package main

import (
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
	"strings"
)

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
	answers := [1000]int{}

	calibrationDocument, err := os.ReadFile("input")

	if err != nil {
		panic(err)
	}

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

	// fmt.Printf("Answers: %v\n", answers)
	fmt.Printf("Total: %d\n", total)
}
