public class Main {
    public static void main(String[] args) {
        int flag = 1;
        for(int i = 1; i < 256; i++) {
            int res = i*i;
            String str = String.valueOf(res);
            for(int j = 0;j < str.length()/2; j++) {
                int k = str.length() - j - 1;
                char head = str.charAt(j);
                char tail = str.charAt(k);
                System.out.println("j="+j);
                System.out.println("k="+k);
                if(head == tail) {
                    continue;
                } else {
                    flag = 0;
                    break;
                }
            }
            if(flag == 1) {
                System.out.println(i);   
            }
        }
    }
}