public class MergeUtil {
	public static void main(String[] args) {
		new MergeUtil();
	}

	StringBuilder sb;
	public MergeUtil() {
		sb = new StringBuilder();

		int[] a = buildRandomArray(4);
		int[] b = a.clone();

		displayArray(a);
		//displayArray(b);

		System.out.println(findInversePair(a, b, 0, a.length-1));
		//mergeSort(a, b, 0, a.length-1);
		displayArray(a);
		//displayArray(b);
	}

	public int[] buildRandomArray(int size) {
		int[] a = new int[size];
		for(int i=0;i<size;i++) {
			a[i] = (int)(Math.random()*(size*3));
		}
		return a;
	}

	public void displayArray(int[] a) {
		sb.setLength(0);
		for(int i=0;i<a.length;i++) {
			sb.append(a[i]);
			sb.append(' ');
		}
		System.out.println(sb.toString());
	}

	public void mergeSort(int[] a, int[] b, int st, int ed) {
		if(st>=ed)
			return;

		int mid = (st+ed)/2;
		mergeSort(b,a,st,mid);
		mergeSort(b,a,mid+1,ed);
		merge(b,a,st,ed);
	}

	public void merge(int[] a, int[] b, int st, int ed) {
		int p, q, r, mid;
		mid = (st+ed)/2;
		p = st;
		q = mid+1;
		r = st;

		while(p<=mid && q<=ed) {
			if(a[p]<=a[q]){
				b[r++] = a[p++];
			}
			else {
				b[r++] = a[q++];
			}
		}

		while(p<=mid) {
			b[r++] = a[p++];
		}

		while(q<=ed) {
			b[r++] = a[q++];
		}
	}

	public int findInversePair(int[] a, int[] b, int st, int ed) {
		if(st>=ed)
			return 0;

		int mid = (st+ed)/2;
		int ip = findInversePair(b,a,st,mid);
		ip += findInversePair(b,a,mid+1,ed);
		ip += findInversePairMerge(b,a,st,ed);
		return ip;
	}

	public int findInversePairMerge(int[] a, int[] b, int st, int ed) {
		int p, q, r, mid, ip, ic;
		mid = (st+ed)/2;
		p = st;
		q = mid+1;
		r = st;
		ip = 0;
		ic = mid+1-st;

		while(p<=mid && q<=ed) {
			if(a[p]<=a[q]){
				b[r++] = a[p++];
				ic --;
			}
			else {
				b[r++] = a[q++];
				ip += ic;
			}
		}

		while(p<=mid) {
			b[r++] = a[p++];
		}

		while(q<=ed) {
			b[r++] = a[q++];
		}
		return ip;
	}
}
