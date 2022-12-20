// https://leetcode.com/problems/two-sum/

package main

import "fmt"

func main() {
	// default values
	numbers := []int{2, 3, 5, 7, 11}
	var target = 8

	// find result
	fmt.Println(twoSum(numbers, target))
}

func twoSum(nums []int, target int) []int {
	numsMap := make(map[int]int)

	for itemIndex, item := range nums {
		numsMap[item] = itemIndex
	}

	for itemIndex, item := range nums {
		idealValue := target - item
		value, ok := numsMap[idealValue]
		if ok && itemIndex != value {
			// value present in the map
			return []int{itemIndex, value}
		}
	}
	return nil
}
