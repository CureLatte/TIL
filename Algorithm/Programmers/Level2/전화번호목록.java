import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);

        int current_len = phone_book[phone_book.length-1].length();
        String target = phone_book[phone_book.length-1];

        for(int i=0; i<phone_book.length; i++){
            if(current_len >= phone_book[i].length()){
                target = phone_book[i];
                current_len = phone_book[i].length();
            }
            else{
                if(target.compareTo(phone_book[i].substring(0, current_len)) == 0 ){
                    return false;
                }
            }

        }
        return true;
    }
}