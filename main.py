import random, time
import tabulate


def qsort_fixed(a, pivot_fn):
    if len(a) == 0:
        return a
    else:
        pivot = pivot_fn_fixed()
        a1 = [i for i in a if i < a[pivot]]
        a2 = [i for i in a if i == a[pivot]]
        a3 = [i for i in a if i > a[pivot]]
        s1, s3 = qsort_fixed(a1, pivot_fn), qsort_fixed(a3, pivot_fn)
        return s1 + a2 + s3


def qsort_random(a, pivot_fn):
    if len(a) == 0:
        return a
    else:
        pivot = pivot_fn_random(a)
        a1 = [i for i in a if i < a[pivot]]
        a2 = [i for i in a if i == a[pivot]]
        a3 = [i for i in a if i > a[pivot]]
        s1, s3 = qsort_random(a1, pivot_fn), qsort_random(a3, pivot_fn)
        return s1 + a2 + s3


def python_sorted(a, pivot_fn):
  return sorted(a)
def pivot_fn_fixed():
    return 0


def pivot_fn_random(a):
    length = len(a)
    spot = random.randrange(0, length)
    return spot


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist, sort_fn)
    return (time.time() - start) * 1000
    ###

#1000, 2000, 2500, 3000, 3500

def compare_sort(sizes=[100, 200, 300, 400, 500, 600, 700, 800, 900, 990]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = qsort_fixed
    qsort_random_pivot = qsort_random
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        random.shuffle(mylist)
        # shuffles list if needed
        # random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(python_sorted, mylist),
        ])
    return result
    ###


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'pythons sorted'],
                            floatfmt=".9f",
                            tablefmt="github"))


def test_print():
    print_results(compare_sort())
    

if __name__ == "__main__":
  random.seed()
  test_print()
   


