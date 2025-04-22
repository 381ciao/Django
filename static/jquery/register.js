$(function (){
    function bindCaptchaBtnClick(){
        $("#captcha-btn").click(function (event){
            let $this = $(this);
            let email = $("input[name='email']").val();
            if(!email){
                alert("请先输入邮箱");
                return;
            }
            $this.off('click');
            let countdown = 6;
            let timer = setInterval(function (){
                if (countdown <= 0){
                    $this.text('获取验证码');
                    clearInterval(timer);
                    bindCaptchaBtnClick();
                }else {
                    countdown--;
                    $this.text(countdown + "s")
                }
            },1000)
        })
    }

    bindCaptchaBtnClick();
})