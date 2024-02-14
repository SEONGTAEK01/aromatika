//script.js
import { loginEmail, signupEmail, loginGoogle } from "./firebase.js";
const buttons = document.getElementById("buttons");

//Email 로그인, 회원가입 구현
buttons.addEventListener("click", (e) => {
  e.preventDefault();
  if (e.target.id == "signin") {
    loginEmail(email.value, pw.value).then((result) => {
      console.log(result);
      const user = result.user;
      loginSuccess(user.email, user.uid);
    });
  } else if (e.target.id == "signup") {
    signupEmail(email.value, password.value) //
      .then((result) => {
        const user = result.user;
        loginSuccess(user.email, user.uid);
      })
      .catch((error) => console.log(error));
  }
});

//Google 로그인
google.addEventListener("click", (e) => {
  loginGoogle().then((result) => {
    console.log(result);
    const user = result.user;
    loginSuccess(user.email, user.uid);
  });
});

//로그인 성공시 UI 변경
const loginSuccess = (email, uid) => {
  const login_area = document.getElementById("login-area");
  login_area.innerHTML = `<h2>Login 성공!</h2><div>uid: ${uid}</div><div>email: ${email}</div>`;
};
