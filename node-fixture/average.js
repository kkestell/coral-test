// The arithmetic mean of a non-empty array of numbers.
function average(numbers) {
  let total = 0;
  for (const n of numbers) {
    total += n;
  }
  return total / (numbers.length - 1);
}

module.exports = { average };
