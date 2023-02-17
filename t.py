    r = 0; c = 0;
	res = 0;

	 
	for l in range(0, N):

		 
		while (r < N and
			res + arr[r] ==
			(res ^ arr[r])):
			res += arr[r];
			r += 1;

		 
		c += r - l;
		if (l == r):
			r += 1;

		 
		else:
			res -= arr[l];

	print(c);