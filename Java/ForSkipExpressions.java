class ForSkipExpressions
{
    public static void main(String[] args)
    {
        int i, sum;

        // 1. Use two parameters in the 1st expression
        for(i = 0, sum = 0; i <= 10; i++) sum += i;
        System.out.println(sum);

        // 2. Skip the 1st expression
        for( ; i <= 100; i++) sum += i;
        System.out.println(sum);

        // 3. Skip the 1st and 2nd expressions
        for( ; ; i++)
        {
            sum += i;
            if(i >= 1000) break;
        }
        System.out.println(sum);

        // 4. Skip all the expressions
        for( ; ; )
        {
            i++;
            sum += i;
            if(i >= 10000) break;
        }
        System.out.println(sum);
    }
}