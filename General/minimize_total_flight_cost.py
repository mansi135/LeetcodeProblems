# There will be a meeting at New York and San Francisco offices. We will have to fly the participants to either one of these two offices.
# Let's say each office can accommodate half of the participants. Our goal is to assign each participant to an office in a way
# that the total travel cost for the company is minimized. What is this minimal cost?
#    SF NY
# A 500 700
# B 200 600
# C 400 500
# D 600 200
# Output : 1400 (A:500 + B:200 + C:500 +D: 200)
#

#pseudo
# take n/2 smallest of sf and rest of ny
# take n/2 smallest of ny and rest of sf
# min of both



def min_cost(sf_arr, ny_arr):

    c = list(zip(sf_arr, ny_arr))

    # there is no need to make dict since we just have to return min sum, so use c as a list directly
    fares = {}

    for i in range(len(c)):
        fares[i] = c[i]

    # for i in range(len(sf_arr)):
    #     fares[i] = (sf_arr[i], ny_arr(i))

    sf = list(fares.values())
    sf.sort(key=lambda x: x[0])
    sum_sf = 0

    ny = list(fares.values())
    ny.sort(key=lambda x : x[1])
    sum_ny = 0

    n = len(sf)

    for i in range(int(n/2)):
        sum_sf += sf[i][0]
        sum_ny += ny[i][1]

    for i in range(int(n/2), n):
        sum_sf += sf[i][1]
        sum_ny += ny[i][0]

    return min(sum_sf, sum_ny)


print(min_cost([500, 200, 400, 600], [700, 600, 500, 200]))
