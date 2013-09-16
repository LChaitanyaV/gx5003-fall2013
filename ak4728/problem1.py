def memoized(fn):
        memoized_lengths = [0] * 1000000
        def fn2(n):
            if not memoized_lengths[n]:
                memoized_lengths[n] = fn(n)
            return memoized_lengths[n]
        return fn2
    def cycle_length(n):
        if n == 1: return 1
        if n % 2:
            return cycle_length(n * 3 + 1) + 1
        return cycle_length(n / 2) + 1
    
    def problem(i,j):
        return max([cycle_length(x) for x in range(i, j+1)])
        
    def test_cycle_length():
        assert cycle_length(22) == 16
        assert cycle_length(10) == 7
        assert cycle_length(11) == 15
        print 'OK'
    
    def test_problem():
        print 1, 10, problem(1, 10)
        print 100, 200, problem(100, 200)
        print 201, 210, problem(201, 210)
        print 900, 100, problem(900, 1000)
    
    if __name__ == '__main__': test_problem()