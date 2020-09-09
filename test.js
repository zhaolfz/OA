<script>
function fiboncci(a,b) {
    var nextNmum = a+b;
    console.log(nextNmum+"is in the Fibonacci sequence")
    if(nextNmum < 1000){
        fiboncci(b,nextNmum)
    }
}
fiboncci(1,1)
</script>