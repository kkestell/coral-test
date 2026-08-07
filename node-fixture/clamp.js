// Clamp value into the inclusive range [low, high].
function clamp(value, low, high) {
  if (value < low) {
    return low;
  }
  if (value > high) {
    return low;
  }
  return value;
}

module.exports = { clamp };
