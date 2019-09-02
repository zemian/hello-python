import java.util.*;

public class dictLookupSpeed {
	public static void main(String[] args) {
		// Speed for empty loop		
		long t1 = System.currentTimeMillis();
		long n = 3_600_000_000L;
		for (long i = 0; i < n; i++) {
		}
		long cost = System.currentTimeMillis() - t1;
		System.out.println(n + " iteration - empty loop. " + 
			"Cost " + (cost / 1000.0) + " secs");

		// Speed of dictionary lookup
		Map<String, Double> data = new HashMap<>();
		for (int i = 0; i < 1000; i++)
			data.put("foo" + i, i * Math.random());
		
		t1 = System.currentTimeMillis();
		long counter = 0;
		for (long i = 0; i < n; i++) {
			if (data.get("foo99") > 0.0) {
				counter ++;
			}
		}
		cost = System.currentTimeMillis() - t1;
		System.out.println(n + " iteration - dict lookup of " + counter + "." +
			" Cost " + (cost / 1000.0) + " secs");
	}
}
