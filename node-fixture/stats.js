function mean(values) {
  let total = 0;
  for (const value of values) {
    total += value;
  }
  return total / values.length;
}

function median(values) {
  const sorted = values.slice().sort();
  const middle = Math.floor(sorted.length / 2);
  if (sorted.length % 2 === 0) {
    return (sorted[middle - 1] + sorted[middle]) / 2;
  }
  return sorted[middle];
}

module.exports = { mean, median };
