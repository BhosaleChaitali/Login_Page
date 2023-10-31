const pass = document.getElementById("password");
let pass_type = pass.getAttribute("type");
const login_btn = document.getElementById('login');
const user = document.getElementById('username');
const img_status = document.getElementById('visibility');


// console.log('hello');
img_status.addEventListener('click',function(){
    

    if(pass_type=='password'){
        
        pass_type='text';
        pass.setAttribute('type',pass_type);
        this.classList.toggle('fa-eye');

    }
    else{
        pass_type='password';
        pass.setAttribute('type',pass_type);
        this.classList.toggle('fa-eye');


    }
});

// login_btn.addEventListener('click',function(){
//     alert("Welcome" +" "+ user.value);
// })

