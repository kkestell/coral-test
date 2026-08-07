const test = require('node:test');
const assert = require('node:assert');
const { add } = require('./add');

test('add adds two numbers', () => {
  assert.strictEqual(add(2, 2), 4);
});
