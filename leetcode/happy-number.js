// https://leetcode.com/problems/happy-number/

function isHappyNumber(n) {
  let sum = 0;
  // extract digits
  while (n > 0) {
    const d = n % 10;
    n = Math.floor(n / 10);
    sum += d * d;
  }
  if (sum === 1) return true;
  else if (sum > 1 && sum <= 4) return false;
  return isHappyNumber(sum);
}

console.log(isHappyNumber(1));
console.log(isHappyNumber(2));
console.log(isHappyNumber(3));
console.log(isHappyNumber(4));
console.log(isHappyNumber(19));
