import numpy as np

# all possible 2 digit numbers => 10x10 matrix
# Make matrix sparse by removing all numbers that are not prime
# To sim replacing first digit, find row with most prime numbers
# To sim replacing second digit, find column with most prime numbers

# all possible 3 digit numbers => 10x10x10 matrix
# Make matrix sparse by removing all numbers that are not prime
# To sim replacing only one digit, find row with most prime numbers
# To sim replacing two digits, find plane with most prime numbers


def seive(n):
    prime = np.ones(n, dtype=bool)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n, p):
                prime[i] = False
        p += 1
    return prime


def sparse_digit_matrix(values, digits):
    matrix = {}
    for v in values:
        node = matrix
        for d in (int(d) for d in str(v).zfill(digits)):
            if d not in node:
                node[d] = {}
            node = node[d]
        node["value"] = v
    return matrix


def sparse_count(matrix: dict, axis=None):
    if axis is None:
        if "value" in matrix:
            return 1
        return sum(sparse_count(v) for v in matrix.values())

    try:
        axis = list(axis)
    except TypeError:
        axis = [axis]

    if 0 in axis:
        if len(axis) == 1:
            return {k: sparse_count(v) for k, v in matrix.items()}
        axis = [a - 1 for a in axis if a != 0]
        return {k: sparse_count(v, axis) for k, v in matrix.items()}
    else:
        axis = [a - 1 for a in axis]
        counts = {}
        for v in matrix.values():
            for ck, cv in sparse_count(v, axis).items():
                if ck not in counts:
                    counts[ck] = 0
                counts[ck] += cv
        return counts


def sparse_reduce_eq_digit(matrix: dict, axis=None, digit=None):
    if axis is None:
        if "value" in matrix:
            return [matrix["value"]]
        if digit is not None:
            return [
                v
                for k, v in matrix.items()
                for v in sparse_reduce_eq_digit(v, digit=digit)
                if k == digit
            ]
        return [
            v for k, v in matrix.items() for v in sparse_reduce_eq_digit(v, digit=k)
        ]

    try:
        axis = list(axis)
    except TypeError:
        axis = [axis]

    if 0 in axis:
        # Fixed axis
        if len(axis) == 1:
            return {
                str(k): sparse_reduce_eq_digit(v, digit=digit)
                for k, v in matrix.items()
            }
        axis = [a - 1 for a in axis if a != 0]
        return {
            str(k) + str(k2): v
            for k, v in matrix.items()
            for k2, v in sparse_reduce_eq_digit(v, axis=axis, digit=digit).items()
        }
    else:
        # Reduce axis
        axis = [a - 1 for a in axis]
        counts = {}
        for k, v in matrix.items():
            if digit is not None and k != digit:
                # If digit is fixed, skip all other digits
                continue
            # k is the digit, either from here or passed down
            for ck, cv in sparse_reduce_eq_digit(v, axis=axis, digit=k).items():
                if ck not in counts:
                    counts[ck] = []
                counts[ck] += cv
                # TODO: Single axis issue?
        return counts


def check_primes(primes, digits, last_digit):
    count = 0
    for p in primes:
        if p >= 10 ** (digits - 1) and p < 10**digits and p % 10 == last_digit:
            p = str(p)
            if len(set(p[:-1])) == 1:
                print(p)
                count += 1
    return count


def try_dim_seq(digits, seq_len):
    n = 10**digits
    primes = seive(n)

    primes = np.flatnonzero(primes)
    matrix = sparse_digit_matrix(primes, digits)

    min_prime = None
    sel_dims = None
    for fixed in range(1, digits):
        for dims in combs(digits, fixed):
            dim_sums = sparse_reduce_eq_digit(matrix, axis=dims)
            for _, seq in dim_sums.items():
                if (
                    len(seq) == seq_len
                    and (min_prime is None or min(seq) < min_prime)
                    and min(seq) >= 10 ** (digits - 1)
                ):
                    sel_seq = seq
                    sel_dims = dims
                    min_prime = min(seq)
    print(len(sel_seq))
    print(sel_seq)
    print(sel_dims)
    print(min_prime)


def combs(n, k):
    if k == 0:
        return [[]]
    if n == 0:
        return []
    return [c + [n - 1] for c in combs(n - 1, k - 1)] + combs(n - 1, k)


def main():
    try_dim_seq(6, 8)


if __name__ == "__main__":
    main()
