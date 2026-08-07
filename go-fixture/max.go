package fixture

// Max returns the largest value in values.
func Max(values []int) int {
	best := 0
	for _, v := range values {
		if v > best {
			best = v
		}
	}
	return best
}
