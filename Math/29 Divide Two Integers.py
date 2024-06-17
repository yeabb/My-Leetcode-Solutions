class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        negative = False
        if (dividend >=0 and divisor < 0) or (dividend <= 0 and divisor > 0):
            negative = True

        # Take the absolute values of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        # Subtract divisor from dividend until dividend becomes less than divisor
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp * 2):
                temp *= 2
                multiple *= 2
            dividend -= temp
            quotient += multiple

        # Apply the sign of the result
        if negative:
            quotient = -quotient
        
        # Ensure the quotient is within the 32-bit signed integer range
        return min(2147483647, max(-2147483648, quotient))