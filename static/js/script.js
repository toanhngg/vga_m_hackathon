document.querySelectorAll('.image-container img').forEach(image => {
    image.onclick = () => {
        document.querySelector('.pop-image').style.display = 'block';
        document.querySelector('.pop-image img').src = image.getAttribute('src');
    }
});

document.querySelector('.pop-image span').onclick = () => {
    document.querySelector('.pop-image').style.display = 'none';
}


document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Gửi thông tin đăng nhập đến server Python bằng Ajax
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onload = function () {
        var result = JSON.parse(xhr.responseText);
        if (result.success) {
            document.getElementById('login-result').innerHTML = 'Đăng nhập thành công!';
        } else {
            document.getElementById('login-result').innerHTML = 'Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin đăng nhập.';
        }
    };
    xhr.send(JSON.stringify({ username: username, password: password }));
});
