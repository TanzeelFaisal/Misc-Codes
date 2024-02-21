int modifiedbinsearch(int X, int V[], int n,int low,int high){

    int low, high, mid;
    low = 0;
    high = n - 1;

    while (low <= high) {
        mid = (low + high)/2;
        if (X < V[mid]) {
            high = mid - 1;
            mid = mid - 1;
        }

        else if (X > V[mid])
            low = mid + 1;
        else
            return mid;
    }

    return -1;
}