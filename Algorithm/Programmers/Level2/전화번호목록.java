import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);

        int current_len = phone_book[0].length();
        String target = phone_book[0];
        String prevalue = "";
        for(int i=0; i<phone_book.length; i++){
            // 중복확인
            if (prevalue.compareTo(phone_book[i])==0){
                return false;
            } else {
                prevalue = phone_book[i];
            }

            // 길이가 바뀌였을 때
            // 수정사항 -> TC 가 ["934793", "34", "44", "9347"] -> False
            // 길이 기준 + 여전히 앞자리인지 확인
            if(current_len >= phone_book[i].length() || target.compareTo(phone_book[i].substring(0, current_len)) !=0){

                target = phone_book[i];
                current_len = phone_book[i].length();
            }
            else{
                String check = phone_book[i].substring(0, current_len);
                if(target.compareTo(check) == 0 ){
                    return false;
                }

            }

        }

        return true;
    }
}