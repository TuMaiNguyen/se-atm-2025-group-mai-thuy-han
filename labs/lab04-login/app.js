const USERS = { demo: "demo123", admin: "123456" };
function $(s){return document.querySelector(s);}
function showToast(msg, ok=true){ const t=$("#toast"); t.textContent=msg; t.style.borderColor= ok?"#16a34a":"#ef4444"; t.classList.add("show"); setTimeout(()=>t.classList.remove("show"),2200); }
function validateUsername(u){ if(!u) return "Username không được rỗng"; if(u.length<3) return "Username ≥ 3 ký tự"; if(!/^[a-zA-Z0-9_]+$/.test(u)) return "Chỉ chữ, số, gạch dưới (_)"; return ""; }
function validatePassword(p){ if(!p) return "Password không được rỗng"; if(p.length<6) return "Password ≥ 6 ký tự"; return ""; }

document.addEventListener("DOMContentLoaded",()=>{
  const f=$("#loginForm"), u=$("#username"), p=$("#password"), uE=$("#userErr"), pE=$("#passErr"),
        r=$("#rememberMe"), t=$("#togglePw"), c=$("#cancelBtn");

  const saved=localStorage.getItem("rememberedUser");
  if(saved){ u.value=saved; r.checked=true; }

  t.addEventListener("click",()=>{ const type=p.type==="password"?"text":"password"; p.type=type; t.textContent= type==="password"?"👁":"🙈"; });

  f.addEventListener("submit",(e)=>{
    e.preventDefault(); uE.textContent=""; pE.textContent="";
    const um=validateUsername(u.value.trim()), pm=validatePassword(p.value);
    if(um) uE.textContent=um; if(pm) pE.textContent=pm; if(um||pm) return;

    const ok = USERS[u.value.trim()] === p.value;
    if(!ok){ pE.textContent="Sai username hoặc password (xem tài khoản demo bên dưới)"; showToast("Đăng nhập thất bại",false); return; }

    if(r.checked) localStorage.setItem("rememberedUser",u.value.trim()); else localStorage.removeItem("rememberedUser");
    showToast("Đăng nhập thành công ✅",true);
    setTimeout(()=>{ f.reset(); p.type="password"; },1500);
  });

  c.addEventListener("click",()=>{ uE.textContent=""; pE.textContent=""; });
});
