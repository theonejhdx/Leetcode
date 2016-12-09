int getSum(int a, int b) {
        int x = a^b;
        int y = a&b;
        if(y!=0){
            return getSum(x,y<<1);
        }else{
            return x;
        }
}
