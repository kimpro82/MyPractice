import java.util.Date;
import java.text.SimpleDateFormat;


public class DatePractice {

	public static void main(String[] args) {

		// java.util.Date() : old-fashioned class (deprecated)
		Date date = new Date();
		System.out.println(date); // original
		System.out.println(date.toLocaleString()); // print in Korean
		System.out.println(date.getYear() + 1900); // the year represented by this date, minus 1900
		System.out.println(date.getDay()); // int, 0 = Sunday

		// set a date
		Date date2 = new Date(2015-1900, 3-1, 7); // month : 0 = January
		System.out.println("\n" + date2);
		System.out.println(date2.getYear() + date2.getMonth() + date2.getDate()); // int + int + int
		// System.out.println(date2.getYear().toString() + date2.getMonth().toString() + date2.getDate().toString()); // error
		System.out.println(date2.getYear() + " " + date2.getMonth() + " " + date2.getDate());
		System.out.println((date2.getYear() + 1900) + "-" + (date2.getMonth() + 1) + "-" + date2.getDate());

		// set a date format
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-mm-dd");
		System.out.println("\n" + sdf.format(date2));
		SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd");
		System.out.println(sdf2.format(date2)); // crazy

		// minus(-) operation between two times different to each other
		long dateDiff = date.getTime() - date2.getTime();
		System.out.println("\nIt has been " + dateDiff/1000/60/60/24 + " days since we got married.");
		// 1 from getTime() means 1/1,000 second
	}

}
