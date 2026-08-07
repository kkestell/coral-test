package fixture

// RoundToCents rounds a money amount to whole cents.
func RoundToCents(amount float64) float64 {
	return float64(int(amount*100+0.5)) / 100
}
